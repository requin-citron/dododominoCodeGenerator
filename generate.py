#!/usr/bin/env python3

import random
import time
import os

print("[+]Generate Code")
time.sleep(random.randint(0,5))
for _ in range(random.randint(100,150)):
    print("[+] Found:","".join(str(random.randint(0,9)) for _ in range(5)))
    time.sleep(random.randint(0,10)/10)

try:
    open(os.path.expanduser('~')+"/.klemou","w").write("aHR0cHM6Ly90ZW5vci5jb20vdmlldy9tYXR0ZG9nLWRvZy1ub3NlLWJpZy1ub3NlLWdpZi0yNDI3NDM4NQ==")
except Exception as e:
    print(";(")
print("hacked by klemou")