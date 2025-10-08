import datetime
yesterday=datetime.date.today()
yesterday=yesterday+datetime.timedelta(days=-1)

today=datetime.date.today()

tomorrow=datetime.date.today()
tomorrow=tomorrow+datetime.timedelta(days=1)
print("Yesterday:",yesterday)
print( "Today:",today)
print("Tomorrow:", tomorrow)