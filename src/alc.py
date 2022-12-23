import os
import logging
import datetime
import tinytuya
import psutil
import schedule
import time
from dotenv import load_dotenv


def checkStatus():
    print(device_id)
    print(device_ip_address)
    print(local_key)

#schedule.every(1).minutes.do(checkStatus)
BATTERY_LOW_THRESHOLD=20
BATTERY_HIGH_THRESHOLD=80
ENABLE_LOGGING=True

logging.basicConfig(filename='auto_laptop_charging_logs.log', filemode='a', format='%(message)s', level=logging.INFO)

BASEDIR = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(BASEDIR,"credentials.env"))
device_id = os.getenv("DEVICE_ID")
device_ip_address = os.getenv("DEVICE_IP_ADDRESS")
local_key = os.getenv("LOCAL_KEY")

schedule.every(5).seconds.do(checkStatus) ##TODO change seconds to minutes

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 