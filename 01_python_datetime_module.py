# Sumber: https://www.programiz.com/python-programming/datetime
import datetime

now = datetime.datetime.now()
print(now)

current_date = datetime.date.today()
print(current_date)

print(dir(datetime))

d = datetime.date(2022, 12, 25)
print(d)

from datetime import date
d = date(2022, 12, 25)
print(d)

todays_date = date.today()
print("Today's date =", todays_date)

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import time
a = time()
print("a =", a)
b = time(11, 34, 56)
print("b =", b)
c = time(hour=11, minute=34, second=56)
print("c =", c)
d = time(11, 34, 56, 234566)
print("d =", d)

a = time(11, 34, 56)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

from datetime import datetime
a = datetime(2022, 12, 28)
print(a)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

a = datetime(2022, 12, 28, 23, 55, 59, 342380)
print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())

from datetime import datetime, date
t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)
print("Type of t3 =", type(t3))
print("Type of t6 =", type(t6))

from datetime import timedelta
t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2
print("t3 =", t3)

t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("Total seconds =", t.total_seconds())

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)

date_string = "25 December, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

try:
    import pytz
    local = datetime.now()
    print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
except ImportError:
    print("[SKIP] Modul pytz belum terinstall. Jalankan: pip install pytz")
