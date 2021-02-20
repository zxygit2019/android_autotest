import os


def new_report(report_path):
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path+"\\"+fn))
    sendfile=os.path.join(report_path,lists[-1])
    print(sendfile)
    return sendfile