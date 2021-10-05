import threading
import alarmbot

class AsyncTask:
    def __init__(self):
        self.Alarmbot = alarmbot.Alarmbot()
        pass

    def TaskA(self):
        self.Alarmbot.trace_ksd_premium()
        threading.Timer(5,self.TaskA).start()

if __name__ == "__main__":
    at = AsyncTask()
    at.TaskA()

