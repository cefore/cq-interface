#!/usr/bin/env python3

import cefpyco
import subprocess


with cefpyco.create_handle() as handle:
    fan_is_active = None
    handle.register("ccnx:/fan")
    name_on = "ccnx:/fan/on"
    name_off = "ccnx:/fan/off"
    while True:
        info = handle.receive()
        if not info.is_interest or (info.chunk_num != 0):
            print(f"Pass ({info})")
            continue
        if info.name == name_on:
            if (fan_is_active is None) or (not fan_is_active):
                print("Turn on fan.")
                subprocess.run(["sudo", "uhubctl", "-l", "1-1", "-a", "on"])
                handle.send_data(name_on, f"ok", 0)
                fan_is_active = True
            else:
                print("Already active.")
                handle.send_data(name_on, f"ng", 0)
        elif info.name == name_off:
            if (fan_is_active is None) or fan_is_active:
                print("Turn off fan.")
                subprocess.run(["sudo", "uhubctl", "-l", "1-1", "-a", "off"])
                handle.send_data(name_off, f"ok", 0)
                fan_is_active = False
            else:
                print("Already inactive.")
                handle.send_data(name_off, f"ng", 0)
        else:
            print(f"Invalid name: {info.name}")
            handle.send_data(info.name, f"error", 0)
