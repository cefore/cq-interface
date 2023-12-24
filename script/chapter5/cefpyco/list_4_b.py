#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import cefpyco

with cefpyco.create_handle() as handle:
    handle.register("ccnx:/test")
    while True:
        info = handle.receive()
        if info.is_interest and (info.name == "ccnx:/test") and (info.chunk_num == 0):
            print("Send Data.")
            handle.send_data("ccnx:/test", "hello", 0)
            break