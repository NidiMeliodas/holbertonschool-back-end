#!/usr/bin/python3
"""
Task 0 ------
"""


import requests
import sys


def api(employee_id):
    """
    YES sirrr
    """
    user_link = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_link = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    
    data_user = user_link.json()
    data_todo = todos_link.json()

    usrname = data_user['name']
    
    nb_tasks = len(data_todo)

    done_tasks = len(
        [todo for todo in data_todo if todo['Completed']]
    )

    str1 = f"Employee {usrname} is done with tasks"
    str2 = f"({done_tasks}/{nb_tasks}):"
    print(str1 + str2)

    for todo in data_todo:
        if todo['Completed']:
            print('\t '+ todo['title'])

if __name__ == "__main__":
    try:
        employee_id = sys.argv[1]
        api(employee_id)
    except Exception as e:
        pass
