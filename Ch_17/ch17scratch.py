import datetime
import time

halloween2016 = datetime.datetime(2016, 10, 31)
print(halloween2016)

dtnow = datetime.datetime.now()
print(dtnow)

# Convert from epoch
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

# time delta
delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)

print(delta.days,delta.seconds,delta.microseconds)
print(delta.total_seconds())
print(str(delta))

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
thousandFromToday = dt - thousandDays
print(dt)
print(thousandFromToday)

# Sleep until a day/time
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
print('Happy Halloween.')

# Time as strings
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# Strings as time
print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))

today = '8/13/2020'
print(datetime.datetime.strptime(today, '%m/%d/%Y'))