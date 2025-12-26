#DATE-TIME IN PYTHON

import datetime

current_date = datetime.datetime.today().date()
print("Current date:", current_date)

current_time = datetime.datetime.today().time()
print("Current time:", current_time)

current_datetime = datetime.datetime.today()
print("Current date and time:", current_datetime)

fileName = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
print("Formatted date and time for filename:", fileName)
# print("Current date and time:")
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))