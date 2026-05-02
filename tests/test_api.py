import requests
import sys

def test_workflow():
    url = "http://localhost:5000/tasks"
    
    # 1. Test Create
    print("Testing POST /tasks...")
    r = requests.post(url, json={"name": "Integration Test Task"})
    if r.status_code != 201:
        print(f"Failed POST: {r.text}")
        sys.exit(1)

    # 2. Test Read
    print("Testing GET /tasks...")
    r = requests.get(url)
    tasks = r.json()
    if not any(t[1] == "Integration Test Task" for t in tasks):
        print("Failed GET: Task not found in list")
        sys.exit(1)

    print("All integration tests passed!")
    sys.exit(0)

if __name__ == "__main__":
    test_workflow()
