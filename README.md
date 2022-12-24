## Auto Laptop Charging

A simple script which helps to control [Wipro 10A amert plug](https://www.amazon.in/Wipro-monitoring-appliances-Assistant-DSP1100/dp/B08HNB2FSH/ref=sr_1_6?crid=261O3HO8PB294&keywords=smart%2Bplug&qid=1671857877&sprefix=smart%2Bplug%2Caps%2C269&sr=8-6&th=1) via python.
This script is written to start laptop charging (turn plug on) if battery percent is below certain level and stop charging (turn plug off) once it is above certain percent.
It runs continuously in the background checking the battery percentage every 7 minutes.

## Usage
- Assuming you have a smrt plug compatible with [tinytuya](https://github.com/jasonacox/tinytuya), connect it to your Wifi network to get its IP address. Asiign a static IP address to the plug so that it never changes on your network.

- Follow the [steps](https://github.com/jasonacox/tinytuya#setup-wizard---getting-local-keys) mentioned on tinytuya's page to get the local keys. Upon sucessful completion of steps you would have `device id` and `local key`.

- Once you have the key, clone this repo. You must run the `alc.py` on boot. For that you can take multiple routes

    **On Linux:** [systemd](https://askubuntu.com/questions/919054/how-do-i-run-a-single-command-at-startup-using-systemd)  or [cron](https://phoenixnap.com/kb/crontab-reboot) can be used.

    **On Windows:** [Using the startup directory](https://www.howtogeek.com/208224/how-to-add-a-program-to-startup-in-windows/) or [registry editor](https://www.wintips.org/how-to-run-a-program-at-startup-via-registry/) can be used.

- You can edit `alc.py` file to change minimum and maximum battery thresholds, duration after which script is run and enable/disable logging.

- Create a `credentials.env` file in the in the same place where you have placed `alc.py` file finally.

- Populate the .env file using the format below:
```
DEVICE_ID="<device-id-goes-here>"
DEVICE_IP_ADDRESS="<plug-ip-address-goes-here>"
LOCAL_KEY="<local-key-goes-here>"
```

The script will read these sensitive values from this file.

 - Plug your laptop charger in the plug and restart the system. If everything is done correctly, the script will start on boot and the turning charging on/off will be taken care of by the script itself.

  - If you have logging enabled (enabled by default), a log file will be created in the same location where your `alc.py` file is.