import datetime
d1=datetime.datetime(2025,9,12,13,40,50)
print(d1)
d2=datetime.datetime(2025,9,12,13,40,30)
print(d2)
dif=(d1-d2 )
sec=dif.total_seconds()
print("difference in seconds equal to",sec)
#abs(d1-d2) без минус