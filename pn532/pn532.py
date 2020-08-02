#!/usr/bin/env python

import time
from subprocess import call

def main():
    try:
        while True:
            call('nfc-poll')
    except:
        KeyboardInterrupt()

if __name__ == "__main__":
    main()
