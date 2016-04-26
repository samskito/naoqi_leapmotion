# -*- coding: utf-8 -*-
# Import Naoqi - custom path in project property
from naoqi import *

# Import sys - stdin
import sys

# Import Leap
sys.path.insert(0, "/home/readi/KoDiNg/SDK/MyLeapSDK")
import Leap


# Sample listener class
class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print('Connected')

    def on_frame(self, controller):
        print('Frame available')


# Main
def main():
    controller = Leap.Controller()
    listener = SampleListener()

    controller.add_listener(listener)

    print('Press enter to quit')
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == '__main__':
    main()