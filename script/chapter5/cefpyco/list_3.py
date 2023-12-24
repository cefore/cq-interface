#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cefpyco

with cefpyco.create_handle() as handle:
    handle.send_interest("ccnx:/test", 0)  # Dataパケットを受信したい場合
    # handle.register("ccnx:/test") # Interestパケットを受信したい場合
    info = handle.receive()
    print(info)
