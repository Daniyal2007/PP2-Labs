import datetime

date1 = datetime.datetime(2025, 2, 16, 12, 0, 0)  
date2 = datetime.datetime(2025, 2, 14, 10, 30, 0)  

difference = abs((date1 - date2).total_seconds())

print("Difference in seconds:", difference)
