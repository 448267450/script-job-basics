import schedule
import time as tm 
from datetime import time, timedelta, datetime


def job():
    print("Subscribe to RyanRen")
    
    
# schedule.every(5).seconds.do(job)
schedule.every().second.do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)

