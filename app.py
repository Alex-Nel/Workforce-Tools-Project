from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

# Database connection config from environment variables
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'tasks_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'password')

def get_db_connection():
    # Simple retry mechanism for the database container startup
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME,
                user=DB_USER, password=DB_PASS
            )
        except:
            print("Database not ready, retrying in 2 seconds...")
            time.sleep(2)
    return conn

# Create table if it doesn't exist (Simple for prototype)
conn = get_db_connection()
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tasks (id serial PRIMARY KEY, name varchar(100) NOT NULL);')
conn.commit()
cur.close()
conn.close()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json['name']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (name) VALUES (%s) RETURNING id;', (new_task,))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": task_id, "name": new_task}), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s;', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
