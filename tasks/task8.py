from datetime import datetime
import re

fileName = r"D:\temp\service.txt"
runningSvcs = r"D:\temp\service_running.txt"
stoppedSvcs = r"D:\temp\service_stopped.txt"
errorLog = r"D:\temp\ErrorLog.txt"

try:
    #fileName = input("Please enter full path to service.txt:\n")
    r = open(runningSvcs, 'w')
    s = open(stoppedSvcs, 'w')
    
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub("\s\s+" , " ", line)
            svc = line.split()[1]
            if("Running" in line):
                r.write(svc + "\n")
            elif("Stopped" in line):
                s.write(svc + "\n")
            else:
                print("Service neither Running or Stopped: " + line)
    r.close()
    s.close()
except FileNotFoundError:
    with open(errorLog, 'a') as eLog:
        eLog.write("{} - File not found: {}\n".format(str(datetime.now().strftime("%d-%m-%y %H:%M:%S")), fileName))
