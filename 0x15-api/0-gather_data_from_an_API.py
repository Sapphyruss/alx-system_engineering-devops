#!/usr/bin/python3
"""This script retrieves and displays a user's TODO list from a REST API."""
from requests import get
from sys import argv


if __name__ == "__main__":
    employee_ID = argv[1]
    api = f"https://jsonplaceholder.typicode.com/"
    user_info = f"users/{employee_ID}"
    to_do_list = f"todos?userId={employee_ID}"

    response = get(api + user_info)
    employee_info = response.json()
    response = get(api + to_do_list)
    tasks = response.json()

    employee_name = f"Employee {employee_info['name']}"
    completed_task = [task for task in tasks if task['completed']]
    no_comp_task = len(completed_task)
    no_tasks = len(tasks)

    print(f"{employee_name} is done with tasks({no_comp_task}/{no_tasks}):")

    for task in completed_task:
        print(f"\t {task['title']}")
