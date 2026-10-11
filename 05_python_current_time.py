# Sumber: https://www.programiz.com/python-programming/datetime/current-time
from datetime import datetime
import time

now = datetime.now()
current_time = now.time()
print("Current time (datetime):", current_time)
print("Hour  :", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

t = time.localtime()
print("Current time (time)   :", time.strftime("%H:%M:%S", t))
