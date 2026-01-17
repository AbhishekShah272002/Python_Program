#To get current DATE AND TIME
from datetime import datetime, timedelta
today = datetime.now()

print('Today: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday ' + str(yesterday))