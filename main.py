import ping3
import time

# in seconds how long to monitor network
monitorTime = 60
targetServer = '8.8.8.8'
#how high ping has to spike to count as a spike
spikeThreshold = 300
#delay between pings (s)
delay = 1.

numPings = 0
spikeCount = 0
init_time = time.time()
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Starting " + str(monitorTime) + "s Ping Test to " + targetServer + " at " + current_time)
while time.time() - init_time < monitorTime:
    pingTime = ping3.ping(targetServer, unit='ms')
    numPings += 1
    if not pingTime:
        spikeCount += 1
        print("Request Timed out at " + time.strftime("%H:%M:%S", time.localtime()))
    elif pingTime > spikeThreshold:
        spikeCount += 1
        print("Ping Spike of", pingTime, "at " + time.strftime("%H:%M:%S", time.localtime()))
    time.sleep(delay)
print("RESULTS:")
print(spikeCount, "Ping Spikes in", monitorTime, "seconds")
