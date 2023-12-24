#!/usr/bin/env python3

import cefpyco
from sense_hat import SenseHat
from time import sleep

THRESHOLD_TEMPERATURE = 26

with cefpyco.create_handle() as handle:
    sense = SenseHat()
    while True:
        temp = sense.get_temperature()
        if temp > THRESHOLD_TEMPERATURE:
            print(f"Temperature: {temp:5.2f} (HOT)")
            print("Turn on fan.")
            handle.send_interest("ccnx:/fan/on", 0)
            info = handle.receive()
            if (not info.is_data) or info.payload_s == "error":
                print(f"error: {info}")
                continue
        else:
            print(f"Temperature: {temp:5.2f}")
            print("Turn off fan.")
            handle.send_interest("ccnx:/fan/off", 0)
            info = handle.receive()
            if (not info.is_data) or info.payload_s == "error":
                print(f"error: {info}")
                continue
        sleep(1)
