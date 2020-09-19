import ping3
import matplotlib.animation as animation
import time
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation


ticks_on_screen = 100
x_data, y_data = [], []

figure = pyplot.figure()
line, = pyplot.plot(x_data, y_data, '-')

tick = 0
spikes = 0
def update(frame):
    currPing = ping3.ping('8.8.8.8', unit='ms')
    if not currPing:
        print('Timed out')
        currPing = 1000
    elif currPing > 1000:
        print('Ping Spike')
    y_data.append(currPing)
    if len(y_data) > ticks_on_screen:
        y_data.pop(0)
    line.set_data([i for i in range(len(y_data))], y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=200)

pyplot.title("Live Ping")
pyplot.ylabel("Ping (ms)")
pyplot.xticks([])
pyplot.show()

