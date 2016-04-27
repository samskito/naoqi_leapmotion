# -*- coding: utf-8 -*-
# Import Naoqi - custom path in project property
from naoqi import *

# Import sys - stdin/path
import sys

# Import Leap
sys.path.insert(0, "/home/xxx/KoDiNg/SDK/MyLeapSDK")
import Leap


# Sample listener class
class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print('Connected')

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

    def on_frame(self, controller):
        frame = controller.frame()
        #info = "Frame id: " + str(frame.id) + ", "
        #info += "Gestures: " + str(len(frame.gestures()))

        hand = frame.hands.rightmost

        if hand.is_valid:
            self.nao_features(frame)
        else:
            print("_")

    def nao_features(self, frame):
        tts = ALProxy("ALTextToSpeech", "192.168.0.192", 9559)
        tts.setLanguage("English")
        #tts.say("Nao connected")

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                print(swipe)
                tts.say('swipe')
            elif gesture.type is Leap.Gesture.TYPE_CIRCLE:
                circle = Leap.CircleGesture(gesture)
                print(circle)
                tts.say('circle')


# Main
def main():
    controller = Leap.Controller()
    listener = SampleListener()

    controller.add_listener(listener)

    # End process
    print('Press enter to quit')
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

# Calls main on execution
if __name__ == '__main__':
    main()