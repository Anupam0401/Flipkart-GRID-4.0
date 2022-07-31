import time
import tweets as tw 
from datetime import datetime, timedelta
# run script every 10 minutes past 5 hours 

while 1:
    tw.top_trends()
    dt = datetime.now() + timedelta(hours=2)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)