import schedule
from schedule import every, repeat
import time as tm 
from datetime import time, timedelta, datetime


# Repeat every 5 seconds
@repeat(every(5).seconds, message="Subscribe")
def job(message):
    print("Hello the message is:", message)
    
    
schedule.every().second.do(job, message="HELLO")
# def job():
#     print("Subscribe to RyanRen")
    
    
    
# schedule.every(5).seconds.do(job)
# schedule.every().second.do(job)
# schedule.every(7).minutes.do(job)

# schdule the job every day at 15:43
# schedule.every().day.at("15:43").do(job)

# schedule every 40 second of the minute to execute the job
# schedule.every().minute.at(":40").do(job)

# j = schedule.every(1).to(5).seconds.do(job)

# count = 0

while True:
    schedule.run_pending()
    tm.sleep(1)
    # count += 1
    # if count == 10:
    #     schedule.cancel_job(j)

