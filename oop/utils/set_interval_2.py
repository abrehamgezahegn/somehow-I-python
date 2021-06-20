import time, threading

StartTime = time.time()


def action(some, things):
    print("in action", some, things)
    print("action ! -> time : {:.1f}s".format(time.time() - StartTime))


class Set_Interval:
    def __init__(self, interval, action, args):
        self.interval = interval
        self.action = action
        self.args = args
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime - time.time()):
            nextTime += self.interval
            self.action(*self.args)

    def cancel(self):
        self.stopEvent.set()


# # start action every 0.6s
# inter = Set_Interval(0.6, action, ["hommie", "hold your head"])
# print("just after setInterval -> time : {:.1f}s".format(time.time() - StartTime))

# # will stop interval in 5s
# t = threading.Timer(5, inter.cancel)
# t.start()
