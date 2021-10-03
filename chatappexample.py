import time
from pprint import pprint
last_msg = {}
first_msg = None
STACKABLES_WAIT = 601

_discord_dank_memer_wait_times = {
    "pls beg": 46,
    "pls hunt": 41,
    "pls fish": 41,
    "pls dig": 41,
    "pls dep all": STACKABLES_WAIT,
    "pls sell boar all": STACKABLES_WAIT,
    "pls sell cookie all": STACKABLES_WAIT,
    "pls sell dear all": STACKABLES_WAIT,    
    "pls sell duck all": STACKABLES_WAIT,
    "pls sell fish all": STACKABLES_WAIT,
    "pls sell junk all": STACKABLES_WAIT,
    "pls sell rabbit all": STACKABLES_WAIT,
    "pls sell seaweed all": STACKABLES_WAIT,
    "pls sell skunk all": STACKABLES_WAIT,
    "pls sell work all": STACKABLES_WAIT,
}

limits = _discord_dank_memer_wait_times

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
    
