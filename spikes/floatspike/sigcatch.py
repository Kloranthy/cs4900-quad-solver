import signal
import sys

def sigint_catch(sig, frame):
    print("\nctr-c detected, exiting")
    sys.exit()
