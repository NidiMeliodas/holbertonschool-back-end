#!/usr/bin/python3
"""
Task 0 ------
"""

import json
import requests
import sys


def api():
    user_link = 'https://jsonplaceholder.typicode.com/users' + sys.argv[1]
    todos_link = "https://jsonplaceholder.typicode.com/todos"

    answer = requests.get(user_link)

    if (answer.ok):
        jData = json.loads(answer.content)
        EMPLOYEE_NAME = jData["name"]
    else:
        answer.raise_for_status

    query = {'userId': sys.argv[1]}

    answer = requests.get(todos_link, params=query)
    if (answer.ok):
        jData = json.loads(answer.content)
        TOTAL_NUMBER_OF_TASKS = len(jData)

        NUMBER_OF_DONE_TASKS = 0
        for todo in jData:
            if todo["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1

        print("Employee " + EMPLOYEE_NAME + " is done with tasks(" +
              str(NUMBER_OF_DONE_TASKS) +
              "/" + str(TOTAL_NUMBER_OF_TASKS) + ")")
        for todo in jData:
            if todo["completed"] is True:
                print("\t " + todo["title"])
    else:
        answer.raise_for_status()


if __name__ == "__main__":
    api()
