import os
croot = os.getcwd()
print(croot)
ftime = 0
fpath = ""
for files in os.listdir(croot):
    if(".apk" in files):
        path = os.path.join(croot, files)
        time = os.path.getmtime(path)
        if(ftime < time):
            ftime = time
            fpath = path
cmdstr = "adb install -r " + fpath
os.system(cmdstr)