import datetime

now = datetime.datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print("Original Datetime:", now)
print("Datetime without Microseconds:", now_without_microseconds)
