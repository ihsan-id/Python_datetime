# Sumber: https://www.programiz.com/python-programming/datetime/strptime
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)
print("type of date_string =", type(date_string))
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))

dt_string = "12/11/2018 09:15:32"
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

try:
    date_string = "12/11/2018"
    date_object = datetime.strptime(date_string, "%d %m %Y")
    print("date_object =", date_object)
except ValueError as e:
    print("ValueError:", e)
