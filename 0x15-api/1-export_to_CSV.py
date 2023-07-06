#!/usr/bin/python3
"""Module that gets information of an employee's TODO list progress
based on the ID given and converts it to CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    task_url = user_url + "/todos"

    # Get the JSON dictionaries for requested user and all TODOs
    user = requests.get(user_url).json()
    todos = requests.get(task_url).json()

    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    username = user.get("username")

    # Create a list to later convert to csv format
    csv_list = []
    for task in todos:
        row = {}
        row["USER_ID"] = task.get("userId")
        row["USERNAME"] = username
        row["TASK_COMPLETED_STATUS"] = task.get("completed")
        row["TASK_TITLE"] = task.get("title")
        csv_list.append(row)

    # Convert list to CSV file
    with open("{}.csv".format(uid), "w") as csv_file:
        csv_ins = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                 quoting=csv.QUOTE_ALL)
        csv_ins.writerows(csv_list)
