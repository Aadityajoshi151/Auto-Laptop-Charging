import os
import logging
import datetime
import tinytuya
import psutil
import schedule
import time
from dotenv import load_dotenv

BATTERY_LOW_THRESHOLD=20
BATTERY_HIGH_THRESHOLD=80
ENABLE_LOGGING=True

def checkStatus():
    print(psutil.sensors_battery().percent)

schedule.every(1).minutes.do(checkStatus)

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 