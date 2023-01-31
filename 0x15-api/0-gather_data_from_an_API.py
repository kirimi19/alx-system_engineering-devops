#!/usr/bin/python3
"""
Script, using REST API, that gives TODO list progress
rusing given eomplyee ID
"""
import json
import urllib.request


def todo_list_progress(employee_id):
    """Make API request"""
    url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
           .format(employee_id))
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    """get to filter complete tasks"""
    complete_tasks = [tasks for tasks in data if tasks["completed"]]
    num_done_tasks = len(complete_tasks)
    num_total_tasks = len(data)
    """Getting employee name"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = urllib.request.urlopen(url)
    employee_data = json.loads(response.read())
    employee_name = employee_data["name"]
    """printing the output in a specific format"""
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          num_done_tasks,
                                                          num_total_tasks))
    for task in complete_tasks:
        print("\t{}['title']".format(task))
if __name__ == "__main__":
    employee_id = 2
    todo_list_progress(employee_id)
