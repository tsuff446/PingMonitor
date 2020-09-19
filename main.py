import time
import cmd_ping
# in seconds how long to monitor network
monitorTime = 360
targetServer = '172.217.4.46'
#how long a connection has to wait before timeout (s)
timeout = 10
#how high ping has to spike to count as a spike
spikeThreshold = 300
#delay between pings (s)
delay = .2

logStream = open('logs.txt', 'w')
numPings = 0
spikeCount = 0
init_time = time.time()
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Starting " + str(monitorTime) + "s Ping Test to " + targetServer + " at " + current_time)
while time.time() - init_time < monitorTime:
    start = time.time()
    result = cmd_ping.ping(targetServer, logStream)
    pingTime = time.time() - start
    numPings += 1
    if not result:
        spikeCount += 1
        print("Request Timed out (>" + str(timeout) + "s)" + " at " + time.strftime("%H:%M:%S", time.localtime()))
    elif pingTime > spikeThreshold:
        spikeCount += 1
        print("Ping Spike of", pingTime, "at " + time.strftime("%H:%M:%S", time.localtime()))
    time.sleep(delay)
print("RESULTS:")
print(spikeCount, "Ping Spikes in", monitorTime, "seconds")
