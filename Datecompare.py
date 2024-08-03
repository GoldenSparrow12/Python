from datetime import datetime
import time

# tim = int(input("Enter The time"))
if datetime(datetime.now().year,datetime.now().month,datetime.now().day,10)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,16):
    print("Working Hours")
else:
    print("Free Time")

ti = time.asctime(time.localtime(time.time()))
print(ti)