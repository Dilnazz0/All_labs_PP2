import datetime 
currentdate=datetime.datetime.today()
print(currentdate)
currentdate=currentdate+datetime.timedelta(days=-5)
print(currentdate)