import os
import logging
import datetime
import tinytuya
import psutil
import schedule
import time
from dotenv import load_dotenv


def checkStatus():
    print(int(psutil.sensors_battery().percent))

#schedule.every(1).minutes.do(checkStatus)
BATTERY_LOW_THRESHOLD=20
BATTERY_HIGH_THRESHOLD=80
ENABLE_LOGGING=True
logging.basicConfig(filename='auto_laptop_charging_logs.log', filemode='a', format='%(message)s', level=logging.INFO)
schedule.every(5).seconds.do(checkStatus)

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 