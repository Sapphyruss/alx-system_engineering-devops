import requests
import sys
"""todo list of employee"""
def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task["completed"]]
        num_done_tasks = len(done_tasks)

        # Display information
        print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

