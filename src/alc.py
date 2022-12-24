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
    ttobj = tinytuya.OutletDevice(device_id, device_ip_address, local_key)
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
    battery_percentage = int(psutil.sensors_battery().percent)
    plugged_in = psutil.sensors_battery().power_plugged

    if battery_percentage <= BATTERY_LOW_THRESHOLD and not plugged_in:
        toggleStatus(True, "started", battery_percentage)
    
    if battery_percentage >= BATTERY_HIGH_THRESHOLD and plugged_in:
        toggleStatus(False, "stopped", battery_percentage)

BATTERY_LOW_THRESHOLD=20
BATTERY_HIGH_THRESHOLD=80
LOGGING_ENABLED=True
DURATION=7

logging.basicConfig(filename='auto_laptop_charging_logs.log', filemode='a', format='%(message)s', level=logging.INFO)

BASEDIR = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(BASEDIR,"credentials.env"))
device_id = os.getenv("DEVICE_ID")
device_ip_address = os.getenv("DEVICE_IP_ADDRESS")
local_key = os.getenv("LOCAL_KEY")

checkBatteryStatus()
schedule.every(DURATION).minutes.do(checkBatteryStatus)

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 