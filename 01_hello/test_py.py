#!/usr/bin/env python3

sl_6 = 3
tp_7 = 5
close_9 = 6

if close_9 > (sl_6 - 2) and close_9 < (sl_6 + 2):
    print('SL')
else:
    print('no SL')

if close_9 > (tp_7 - 2) and close_9 < (tp_7 + 2):
    print('TP')
else:
    print('no TP')

