from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def time_run():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
scheduler.start()
# 定义BlockingScheduler
#sched = BlockingScheduler()
#sched.add_job(time_run, 'interval', seconds=5)
#sched.start()