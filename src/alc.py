import os
import logging
import tinytuya
import psutil
import schedule
import time
from dotenv import load_dotenv
from datetime import datetime


def checkBatteryStatus():
    battery_percentage = int(psutil.sensors_battery().percent)
    plugged_in = psutil.sensors_battery().power_plugged

    if battery_percentage <= BATTERY_LOW_THRESHOLD and not plugged_in:
        ttobj = tinytuya.OutletDevice(device_id, device_ip_address, local_key)
        ttobj.set_version(3.3)
        response = ttobj.turn_on()
        if ENABLE_LOGGING:
            if "Network Error: Device Unreachable" in response.values():
                dtobj = datetime.now()             
                logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Smart plug not reachable.")
            else:
                logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Charging started at {battery_percentage}% battery.")
    
    if battery_percentage >= BATTERY_HIGH_THRESHOLD and plugged_in:
        ttobj = tinytuya.OutletDevice(device_id, device_ip_address, local_key)
        ttobj.set_version(3.3)
        response = ttobj.turn_off()
        if ENABLE_LOGGING:
            if "Network Error: Device Unreachable" in response.values():
                dtobj = datetime.now()             
                logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Smart plug not reachable.")
            else:
                logging.info(f"[{dtobj.strftime('%d %b %Y - %I:%M:%S %p')}] Charging stopped at {battery_percentage}% battery.")

BATTERY_LOW_THRESHOLD=20
BATTERY_HIGH_THRESHOLD=80
ENABLE_LOGGING=True

logging.basicConfig(filename='auto_laptop_charging_logs.log', filemode='a', format='%(message)s', level=logging.INFO)

BASEDIR = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(BASEDIR,"credentials.env"))
device_id = os.getenv("DEVICE_ID")
device_ip_address = os.getenv("DEVICE_IP_ADDRESS")
local_key = os.getenv("LOCAL_KEY")

schedule.every(7).minutes.do(checkBatteryStatus)

def main():   
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
 