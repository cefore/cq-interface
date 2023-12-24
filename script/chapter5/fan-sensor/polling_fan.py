#!/usr/bin/env python3

import cefpyco
from time import sleep
from ast import literal_eval
import subprocess

THRESHOLD_TEMPERATURE = 26

with cefpyco.create_handle() as handle:
    fan_is_active = None
    while True:
        handle.send_interest("ccnx:/sensor/getdata/temperature", 0)
        info = handle.receive()
        if info.is_data:
            temp = literal_eval(info.payload_s)
            if temp > THRESHOLD_TEMPERATURE:
                print(f"Temperature: {temp:5.2f} (HOT)")
                if (fan_is_active is None) or (not fan_is_active):
                    print("Turn on fan.")
                    subprocess.run(["sudo", "uhubctl", "-l", "1-1", "-a", "on"])
                    fan_is_active = True
            else:
                print(f"Temperature: {temp:5.2f}")
                if (fan_is_active is None) or fan_is_active:
                    print("Turn off fan.")
                    subprocess.run(["sudo", "uhubctl", "-l", "1-1", "-a", "off"])
                    fan_is_active = False
        else:
            print("Failed to receive data.")
        sleep(1)
