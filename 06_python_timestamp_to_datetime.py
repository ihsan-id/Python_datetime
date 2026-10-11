# Sumber: https://www.programiz.com/python-programming/datetime/timestamp-datetime
from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

now = datetime.now()
ts = datetime.timestamp(now)
print("Timestamp =", ts)
