#!/usr/bin/python3
"""
Task 3 ------
"""

import json
import requests


def api():
    user_link = 'https://jsonplaceholder.typicode.com/users'
    todos_link = "https://jsonplaceholder.typicode.com/todos"

    answer = requests.get(user_link)

    if (answer.ok):
        users = json.loads(answer.content)
    else:
        answer.raise_for_status

    tasks = {}

    for user in users:
        user_id = str(user["id"])
        EMPLOYEE_NAME = user["username"]

        query = {'userId': user_id}

        answer = requests.get(todos_link, params=query)
        if (answer.ok):
            jData = json.loads(answer.content)

            tasks = []
            for task in jData:
                tasks.append({
                    "username": EMPLOYEE_NAME, "task": task.get("title"),
                    "completed": task.get("completed")
                })

            tasks[user_id] = tasks
        else:
            answer.raise_for_status()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks, json_file)


if __name__ == "__main__":
    api()
