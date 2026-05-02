import requests
import sys

BASE_URL = "http://127.0.0.1:5000/tasks"

def test_create_task():
    """POST a new task and verify it returns 201 with the data."""
    r = requests.post(BASE_URL, json={"name": "Integration Test Task"})
    if r.status_code != 201:
        print(f"FAIL - POST returned {r.status_code}: {r.text}")
        sys.exit(1)

    data = r.json()
    if data.get("name") != "Integration Test Task":
        print(f"FAIL - POST response not expected name: {data}")
        sys.exit(1)

    task_id = data["id"]
    print(f"PASS - created task with id {task_id}")
    return task_id


def test_read_tasks(expected_name):
    print("Testing GET /tasks...")
    r = requests.get(BASE_URL)
    if r.status_code != 200:
        print(f"FAIL - GET returned {r.status_code}: {r.text}")
        sys.exit(1)

    tasks = r.json()
    if not any(t[1] == expected_name for t in tasks):
        print(f"FAIL - Task '{expected_name}' not found in response: {tasks}")
        sys.exit(1)

    print(f"PASS - Found '{expected_name}' in task list")


def test_delete_task(task_id):
    print(f"Testing DELETE /tasks/{task_id}...")
    r = requests.delete(f"{BASE_URL}/{task_id}")
    if r.status_code != 204:
        print(f"FAIL - DELETE returned {r.status_code}: {r.text}")
        sys.exit(1)

    print(f"PASS - deleted task {task_id}")


def test_verify_deletion(task_id):
    print(f"Testing that task {task_id} is gone...")
    r = requests.get(BASE_URL)
    if r.status_code != 200:
        print(f"FAIL - GET returned {r.status_code}: {r.text}")
        sys.exit(1)

    tasks = r.json()
    if any(t[0] == task_id for t in tasks):
        print(f"FAIL - Task {task_id} still present after deletion: {tasks}")
        sys.exit(1)

    print(f"PASS - Task {task_id} confirmed deleted")


def run_all_tests():
    print("Running integration tests...")
    task_id = test_create_task()
    test_read_tasks("Integration Test Task")
    test_delete_task(task_id)
    test_verify_deletion(task_id)

    print("All integration tests passed")

if __name__ == "__main__":
    run_all_tests()
