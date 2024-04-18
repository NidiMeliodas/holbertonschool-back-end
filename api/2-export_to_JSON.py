#!/usr/bin/python3
"""
Task 2 ------
"""

import json
import requests
import sys


def api(user_id):
    user_link = 'https://jsonplaceholder.typicode.com/users' + user_id
    todos_link = "https://jsonplaceholder.typicode.com/todos"

    answer = requests.get(user_link)

    if (answer.ok):
        jData = json.loads(answer.content)
        EMPLOYEE_NAME = jData["name"]
    else:
        answer.raise_for_status

    query = {'userId': user_id}

    answer = requests.get(todos_link, params=query)
    if (answer.ok):
        jData = json.loads(answer.content)

        tasks = []
        for task in jData:
            tasks.append({
                "task": task.get("title"), "completed": task.get("completed"),
                "username": EMPLOYEE_NAME
            })

        with open("{}.json".format(user_id), "w") as json_file:
            json.dump({user_id: tasks}, json_file)
    else:
        answer.raise_for_status()


if __name__ == "__main__":
    api(sys.argv[1])
