#!/usr/bin/python3
"""Retrieve a user's TODO list from a REST API."""
import json
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

    file_name = f"{employee_ID}.json"
    data = {employee_ID: [{"task": task['title'],
                           "completed": task['completed'],
                           "username": employee_info['username'],
                           } for task in tasks]}
    with open(file_name, 'w', ) as file:
        file = json.dump(data, file)
