'''
Author: your name
Date: 2021-01-31 21:55:59
LastEditTime: 2021-01-31 22:10:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\bfs.py
'''
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque
search_queue = deque()
search_queue += graph["you"]

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-1] =="m"
search ("you")