import sys
dataIn = sys.stdin.readline()

timeData = dataIn.split()
hours = int(timeData[0])
minutes = int(timeData[1])

if minutes >= 45:
    minutes -= 45
else:
    if hours == 0: hours = 24
    hours -= 1
    minutes += 15
    
print('{} {}'.format(hours,minutes))