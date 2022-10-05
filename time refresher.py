from datetime import datetime
import time

now = datetime.now()

while True:
    timee = now.time("%H:%M:%S")
    print(timee)
    time.sleep(1)
