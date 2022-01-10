#Date Time return values
print "Servers Timezone - This will alter your epoch"
print "============================================="
print system.date.getTimezone()

print ""
print "Ignition Date/Time 'Features'"
print "============================================="
print "Day of Month, starts from 1: " + str(system.date.getDayOfMonth(system.date.now()))
print "Day of Year, starts from 1: " + str(system.date.getDayOfYear(system.date.now()))
print "Day of Week, given sunday = 1: " + str(system.date.getDayOfWeek(system.date.now()))
print "-------------------------------------"
print "Current Month, starts from 0: " + str(system.date.getMonth(system.date.now()))
print "-------------------------------------"
print "Current Year: " + str(system.date.getYear(system.date.now()))

#get current EPOC Time
#useful for historical tracking
print ""
print "Epoch Manipulation"
print "============================================="
print "Epoch Samples - using time library"
import time
millisec = str(time.time() * 1000)
print(millisec)

#with datetime
print ""
print "Epoch Samples - using datetime library"
from datetime import datetime
millisec = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
print(millisec)

print ""
print "Epoch Samples - Epoch to python datetime object"
s = millisec / 1000.0
pythonDT = datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
print pythonDT

print ""
print "Epoch Samples - Epoch to ignition datetime object"
ignDT = system.date.fromMillis(millisec)
print ignDT