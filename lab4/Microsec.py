import datetime
today=datetime.datetime.today()
print("Today:",today)
microsecno=today.replace(microsecond=0)
print("No microsecond:",microsecno)