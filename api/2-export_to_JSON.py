#!/usr/bin/python3
"""
Task 2 ------
"""

import json
import requests
import sys


def api(user_id):
    """
    YES sirrr
    """
    user_link = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    todos_link = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
    
    user_name = user_link.json()['username']

    task_todo = []

    for todo in todos_link.json():
        task_dict = {}
        task_title = todo['title']
        task_status = todo['completed']
        task_dict = {"task": task_title,
                     "completed": task_status, "username": user_name}
        task_todo.append(task_dict)

    with open(f"{user_id}.json", "w") as file:
        json.dump({user_id: task_todo}, file)


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        api(user_id)
    except Exception as e:
        pass