#!/usr/bin/python3
"""This script retrieves and displays a user's TODO list from a REST API."""
from requests import get
from sys import argv


if __name__ == "__main__":
    employee_ID = argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    user_info = f"users/{employee_ID}"
    to_do_list = f"todos?userId={employee_ID}"

    # Retrieve user information
    response = get(api + user_info)
    employee_info = response.json()
    employee_name = f"Employee {employee_info['name']}"
    padded_employee_name = employee_name.ljust(18)  # Ensure 18 characters length

    # Retrieve tasks information
    response = get(api + to_do_list)
    tasks = response.json()
    
    completed_tasks = [task for task in tasks if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(tasks)

    # Display information
    print(f"{padded_employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

