#!/usr/bin/python3
import os
import logging
import tinytuya
import psutil
import schedule
import time
from dotenv import load_dotenv
from datetime import datetime


def toggleStatus(state, logtext, battery_percent):
    ttobj = tinytuya.OutletDevice(device_id, device_ip_address, local_key) #Connect with the smart plug
    ttobj.set_version(3.3)
    if state:
        response = ttobj.turn_on()
    else:
        response = ttobj.turn_off()
    if LOGGING_ENABLED:
        dtobj = datetime.now()
        if "Network Error: Device Unreachable" in response.values():
            logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Smart plug not reachable.")
        else:
            logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Charging {logtext} at {battery_percent}% battery.")

def checkBatteryStatus():
    battery_percentage = int(psutil.sensors_battery().percent) #Get current battery percentage
    plugged_in = psutil.sensors_battery().power_plugged #Get plugged in boolean

    if battery_percentage <= BATTERY_LOW_THRESHOLD and not plugged_in:
        toggleStatus(True, "started", battery_percentage)
    
    if battery_percentage >= BATTERY_HIGH_THRESHOLD and plugged_in:
        toggleStatus(False, "stopped", battery_percentage)

BATTERY_LOW_THRESHOLD=20  #If below this point, laptop will start charging. Change if required.
BATTERY_HIGH_THRESHOLD=80 #If above this point, laptop will stop charging. Change if required.
LOGGING_ENABLED=True #Basic logging option. Disable if not required.
DURATION=7 #After every 7 minutes, the script will check the battery status. Change if required.

if LOGGING_ENABLED:
    logging.basicConfig(filename='auto_laptop_charging_logs.log', filemode='a', format='%(message)s', level=logging.INFO) #Basic logging config

BASEDIR = os.path.abspath(os.path.dirname(__name__)) #Read the info from .env file
load_dotenv(os.path.join(BASEDIR,"credentials.env"))
device_id = os.getenv("DEVICE_ID")
device_ip_address = os.getenv("DEVICE_IP_ADDRESS")
local_key = os.getenv("LOCAL_KEY")

checkBatteryStatus() #Initial call/ 0th call
schedule.every(DURATION).minutes.do(checkBatteryStatus) #Call the checkBatteryStatus function every 7 minutes.

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 