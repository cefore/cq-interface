#!/usr/bin/env python3

import cefpyco
from sense_hat import SenseHat

with cefpyco.create_handle() as handle:
    sense = SenseHat()
    print(f"temp:{sense.get_temperature()}")
    handle.register("ccnx:/sensor")
    while True:
        temp = sense.get_temperature()
        print(f"temp:{temp}")
        info = handle.receive()
        exp_name = "ccnx:/sensor/getdata/temperature"
        if info.is_interest and (info.name == exp_name) and (info.chunk_num == 0):
            print(f"Send data")
            handle.send_data(exp_name, f"{temp}", 0)
