#!/usr/bin/python3
"""
Script that export 0-gather_data_from_an_API.py
It exports the data in JSON format
"""
import json
import sys
import urllib.request


def export_to_json(employee_id):
    """Make API request to get information"""
    url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
           .format(employee_id))
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    """Make API request to get employee name"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = urllib.request.urlopen(url)
    employee_data = json.loads(response.read())
    employee_name = employee_data["name"]

    """create dicitonary to store information"""
    task_data = {}
    task_list = []
    for task in data:
        task_info = {"task": task["title"], "completed": task["completed"],
                     "username": employee_name}
        task_list.append(task_info)
    task_data[str(employee_id)] = task_list

    """write the information to JSON file"""
    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(task_data, json_file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
