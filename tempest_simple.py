#!/usr/bin/env python3
#################################################
#   Title: Simple Tempest Weather Station Logger
# Project: Tempest WX
#################################################
import socket
import json
import datetime
import sys

UDP_IP = "0.0.0.0"
UDP_PORT = 50222

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Listening on UDP port", UDP_PORT)
ts = datetime.datetime.now(datetime.timezone.utc)
ts_str = ts.strftime('%Y%m%d_%H%M%SZ')
fn = "TempestWX_{:s}.log".format(ts_str)
print("Writing to: {:s}".format(fn))

while True:
    data, addr = sock.recvfrom(4096)
    try:
        msg = json.loads(data.decode("utf-8"))
        print(msg)
        with open(fn, 'a') as fh:
            fh.write(json.dumps(msg))
            fh.write('\n')

    except json.JSONDecodeError:
        # Some UDP packets might not be JSON
        pass
