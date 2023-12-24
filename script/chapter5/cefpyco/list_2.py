#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cefpyco

with cefpyco.create_handle() as handle:
    # ccnx:/testというコンテンツの0番目のチャンクを
    # 要求するInterestパケットを送信
    handle.send_interest("ccnx:/test", 0)
    # ccnx:/testというコンテンツ名・チャンク番号0で
    # helloというテキストコンテンツをDataパケットとして送信
    handle.send_data("ccnx:/test", "hello", 0)
