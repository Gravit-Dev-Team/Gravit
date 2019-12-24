import time

class Log:
    def __init__(self, log=""):
        self.log = log

    def new_log(self, log):
        datetime = time.strftime("[%d/%m/%Y | %H:%M:%S] ", time.localtime(time.time()))
        self.log += "\n"+datetime+log
