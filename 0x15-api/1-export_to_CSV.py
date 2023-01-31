#!/usr/bin/python3
"""
Script from 0-gather_data_from_an_API.py, that
exports data in csv format
"""
import csv
import json
import sys
import urllib.request


def export_to_csv(employee_id):
    """Make request for todolist"""
    url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
           .format(employee_id))
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    """Mae API request for employee name"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = urllib.request.urlopen(url)
    employee_data = json.loads(response.read())
    employee_name = employee_data["name"]

    """create csv and write to it"""
    csv_file = ("{}.csv".format(employee_id))
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])
        for task in data:
            writer.writerow([employee_id, employee_name, task["completed"],
                             task["title"]])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
