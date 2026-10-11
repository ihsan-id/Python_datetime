# Sumber: https://www.programiz.com/python-programming/time
import time

seconds = time.time()
print("Seconds since epoch =", seconds)

seconds = 1672215379.5045543
local_time = time.ctime(seconds)
print("Local time:", local_time)

result = time.localtime(1672214933)
print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.gmtime(1672214933)
print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
seconds = time.mktime(time_tuple)
print(seconds)

t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
result = time.asctime(t)
print("Result:", result)

named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)

time_string = "14 July, 2023"
result = time.strptime(time_string, "%d %B, %Y")
print(result)
