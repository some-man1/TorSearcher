import requests
import random, string
import re
from sys import exit

print("""\033[95m
  _______         _____                     _               
 |__   __|       / ____|                   | |              
    | | ___  _ _| (___   ___  __ _ _ __ ___| |__   ___ _ __ 
    | |/ _ \| '__\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
    | | (_) | |  ____) |  __/ (_| | | | (__| | | |  __/ |   
    |_|\___/|_| |_____/ \___|\__,_|_|  \___|_| |_|\___|_|   
                                                            
             \033[94m telegram : @linuxdebain                                                  
""")


search = input("Enter your search : ")
try:
    number = int(input("how many websits you want? "))
except Exception as err:
    print("\033[0;31;40m" , err)
    exit(0)
if " " in search:
    search = search.replace(" ", "+")
url = f"https://ahmia.fi/search/?q={search}"

with open("user-agents.txt", "r+") as a: # This file include many user agents for Not get banned from ahmia.fi
    users = random.choice(a.readlines()).strip()  

header = {
    "User-Agent": users
}
results_limt = number
result_collected = 0
webs = requests.get(url, headers=header).text
reg = "\w+\.onion"
data = re.findall(reg, webs)
filename = ''.join(random.choice(string.ascii_letters + string.digits)for i in range(5))
data = list(dict.fromkeys(data))

with open(f"{filename}.txt", "a+") as f:
    for i in data:
        if result_collected >= results_limt:
            break  
        i = i + "\n"
        f.write(i)
        result_collected += 1
    print(f"\033[0;31;40m \nCompleted, saved in {filename}.txt")
