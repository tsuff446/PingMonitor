import ping3
import time
import datetime

# in seconds how long to monitor network
monitorTime = 60
targetServer = '8.8.8.8'
#delay between pings
delay = 1./60.

numPings = 0
spikeCount = 0
init_time = time.time()
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Starting " + str(monitorTime) + "s Ping Test to " + targetServer + " at " + current_time)
while time.time() - init_time < monitorTime:
    pingTime = ping3.ping(targetServer, unit='ms')
    numPings += 1
    if not pingTime or pingTime > 300:
        spikeCount += 1
        print("Ping Spike at " + time.strftime("%H:%M:%S", time.localtime()))
    time.sleep(delay)
print("RESULTS:")
print(spikeCount, "Ping Spikes in", monitorTime, "seconds")
print("That's (" + str(spikeCount) + "/" + str(numPings) + ")")