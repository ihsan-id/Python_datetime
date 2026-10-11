# Sumber: https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("ISO format     :", now.isoformat())
print("Readable       :", now.strftime("%A, %d %B %Y, %H:%M:%S"))
