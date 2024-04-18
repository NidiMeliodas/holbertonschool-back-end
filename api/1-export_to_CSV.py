#!/usr/bin/python3
"""
Task 1 ------
"""

import json
import requests
import sys
import csv


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

        with open("{}.csv".format(user_id), "w", encoding='utf-8') as f:
            csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in jData:
                csv_writer.writerow([user_id, EMPLOYEE_NAME,
                                    task.get("completed"),
                                    task.get("title")])
    else:
        answer.raise_for_status()


if __name__ == "__main__":
    api(sys.argv[1])
