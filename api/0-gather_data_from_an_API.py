#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API URL with the employee ID
    base_url = "https://jsonplaceholder.typicode.com"
    endpoint = f"/users/{employee_id}"
    user_url = f"{base_url}{endpoint}"

    # Make a GET request to retrieve user information
    response = requests.get(user_url)
    user_data = response.json()

    if response.status_code != 200:
        print(f"Employee with ID {employee_id} not found")
        return

    # Extract user name
    employee_name = user_data['name']

    # Make a GET request to retrieve the user's TODO list
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)
    num_completed_tasks = len(completed_tasks)

    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

