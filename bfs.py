'''
Author: your name
Date: 2021-01-31 21:55:59
LastEditTime: 2021-01-31 22:45:52
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
graph["jonny"] = []# ‘thom’、‘jonny’，‘peggy’没有邻居节点

from collections import deque
search_queue = deque()
search_queue += graph["you"]

def search(name):
    search_queue = deque()
    search_queue += graph[name]#graph["you"]是一个数组，其中包含你的所有邻居
    searched = []# 用于标记已经检查过的人
    while search_queue:# 只要队列不为空
        person = search_queue.popleft() # 从队列中弹出最左边的一个元素
        if person not in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]# 将当前节点的邻居放入队列中待检查
                searched.append(person)
    return False
def person_is_seller(name):#判断是不是销售商的函数
    return name[-1] =="m"#如果姓名以m结尾，就是

search ("you")