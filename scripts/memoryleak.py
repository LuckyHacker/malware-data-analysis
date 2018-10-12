import psutil
import threading
import time

import __main__


def monitor_memory():
    limit = 90
    while 1:
        percent = psutil.virtual_memory()[2]
        if percent > limit:
            print("Memory usage over {}.".format(limit))
            p = psutil.Process(__main__.os.getpid())
            p.terminate()

        time.sleep(1)


t = threading.Thread(target=monitor_memory)
t.daemon = True
t.start()