#!/usr/bin/python3
"""
Task 1 ------
"""


import csv
import requests
import sys


def api(user_id):
    """
    YES sirrr
    """
    user_link = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_link = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    user_name = user_link.json()['username']

    for todo in todos_link.json():
        task = todo['title']
        task_status = todo['completed']
        with open(f'{user_id}.csv', mode='a', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow([user_id, user_name, task_status, task])


if __name__ == '__main__':
    try:
        user_id = sys.argv[1]
        api(user_id)
    except Exception as e:
        pass