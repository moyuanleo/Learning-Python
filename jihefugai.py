'''
Author: moyuanleo
Date: 2021-02-01 14:30:44
LastEditTime: 2021-02-01 14:54:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\jihefugai.py
'''
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
#你传入一个数组，它被转化为一个集合 以上为所有要考虑的州

stations = {}
stations["kone"] = set(["id","nv","ut"])#每个站台所覆盖的州
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

final_stations = set()#最终可以包含的站台

while states_needed:
    best_station = None
    states_covered = set()
    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station  
        #已经被覆盖的州为需要被覆盖的州与当前站台覆盖的州的交集
        if len(covered) > len(states_covered):
            #如果当前站台可以覆盖的州大于已经考虑可覆盖的州的个数
            best_station = station # 当前站台为最好的站台
            states_covered = covered # 当前可覆盖的州

states_needed -= states_covered # 留下还没有被覆盖的州
final_stations.add(best_station)  # 添加需要的站台

print(final_stations)
#理想输出 选择set(['ktwo','kthree','kone','kfive'])