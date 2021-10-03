import time
from pprint import pprint
last_msg = {}
first_msg = None
limits = {
    "pls beg": 45,
    "pls hunt": 40,
    "pls fish": 40,
    "pls dig": 40,
    "pls dep all": 300,
}

stats = {
    "success": {},
    "fail": {}
}
throttle_stats = {
    "success": [],
    "fail": []
}

msg_time=-3600

while True:
    msg=input(str(msg_time)+">")
    if not first_msg:
        first_msg = int(time.time())
    msg_time = int(time.time())-first_msg

    if msg not in last_msg:
        last_msg[msg] = time.time()-max(limits.values())

    last_msg_type = time.time()-last_msg[msg]
    print("You last said this",round(last_msg_type,3),"seconds ago.")
    if msg in limits and last_msg_type < limits[msg]:
        print("WARNING\nWARNING\nWARNING\n=====\nYou did to fast!!\n=====\nWARNING\nWARNING\nWARNING")
        if msg in stats["fail"]:
            stats["fail"][msg].append([last_msg_type,time.time()])
        else:
            stats["fail"][msg] = [[last_msg_type,time.time()]]
    else:
        if msg in stats["success"]:
            stats["success"][msg].append([last_msg_type,time.time()])
        else:
            stats["success"][msg] = [[last_msg_type,time.time()]]
        
    last_msg_total = time.time()-max(last_msg.values())
    print("You talked",round(last_msg_total,3),"seconds ago.")
    if last_msg_total < 0.5:
        print("WARNING\nWARNING\nWARNING\n=====\nYou are likely to be throttled!!\n=====\nWARNING\nWARNING\nWARNING")
        throttle_stats["fail"].append([last_msg_total,time.time()])
    else:
        throttle_stats["success"].append([last_msg_total,time.time()])
    last_msg[msg] = time.time()
    
