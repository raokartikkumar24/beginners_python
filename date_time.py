__author__ = 'KRao4'
from datetime import datetime

now = datetime.now()

print(now, now.date(),now.day,now.month,now.year)

print ("%s/%s/%s" %(str(now.month),str(now.day), str(now.year)))

print("%s:%s:%s" %(str(now.minute), str(now.hour), str(now.second)))