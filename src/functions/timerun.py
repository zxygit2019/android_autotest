import time

from self import self


from src.testcase import run_all_case

#run_time = "23:30:00"
run_time = "33:00"

def timerun(self):
    while True:
        #time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
        time_now = time.strftime("%M:%S", time.localtime())  # 刷新
        if time_now == run_time:  # 此处设置每天定时的时间
            print("定时任务开始执行APP自动化测试")
            # 此处3行替换为需要执行的动作
            run_all_case.run_cases()
            subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " APP自动化测试完成"
            print(subject)
            time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次

if __name__ == '__main__':
    timerun(self)