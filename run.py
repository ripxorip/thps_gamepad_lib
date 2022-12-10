import evdev
from evdev import InputDevice, categorize, ecodes

import keyboard

import time

# Find the Gamepad
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if 'Nintendo Switch Pro Controller' == device.name:
        input_dev = device.path


pos_thresh = 20000
neg_thresh = -pos_thresh

macro_delay_s = 0.0
macro_delay_press_len = 0.05

last = {
    "ABS_Y": 0,
    "ABS_X": 0
}

dev = InputDevice(input_dev)
dev.grab()
for event in dev.read_loop():
    ev = categorize(event)
    if ecodes.bytype[ev.event.type][ev.event.code] == 'ABS_Y':
        val = ev.event.value

        if val > pos_thresh and last['ABS_Y'] < pos_thresh:
            keyboard.press('down')
        elif val < pos_thresh and last['ABS_Y'] > pos_thresh:
            keyboard.release('down')

        elif val < neg_thresh and last['ABS_Y'] > neg_thresh:
            keyboard.press('up')
        elif val > neg_thresh and last['ABS_Y'] < neg_thresh:
            keyboard.release('up')

        last['ABS_Y'] = val

    if ecodes.bytype[ev.event.type][ev.event.code] == 'ABS_X':
        val = ev.event.value

        if val > pos_thresh and last['ABS_X'] < pos_thresh:
            keyboard.press('right')
        elif val < pos_thresh and last['ABS_X'] > pos_thresh:
            keyboard.release('right')

        elif val < neg_thresh and last['ABS_X'] > neg_thresh:
            keyboard.press('left')
        elif val > neg_thresh and last['ABS_X'] < neg_thresh:
            keyboard.release('left')

        last['ABS_X'] = val

    if ecodes.bytype[ev.event.type][ev.event.code] == 'BTN_START':
        if ev.event.value:
            keyboard.press('esc')
        else:
            keyboard.release('esc')

    if ecodes.bytype[ev.event.type][ev.event.code] == 'BTN_SELECT':
        if ev.event.value:
            keyboard.press('enter')
        else:
            keyboard.release('enter')

    if 'BTN_EAST' in ecodes.bytype[ev.event.type][ev.event.code]:
        if ev.event.value:
            keyboard.press('6')
        else:
            keyboard.release('6')

    if 'BTN_WEST' in ecodes.bytype[ev.event.type][ev.event.code]:
        if ev.event.value:
            keyboard.press('4')
        else:
            keyboard.release('4')

    if 'BTN_NORTH' in ecodes.bytype[ev.event.type][ev.event.code]:
        if ev.event.value:
            keyboard.press('8')
        else:
            keyboard.release('8')

    if 'BTN_SOUTH' in ecodes.bytype[ev.event.type][ev.event.code]:
        if ev.event.value:
            keyboard.press('2')
        else:
            keyboard.release('2')

    if 'BTN_TR' in ecodes.bytype[ev.event.type][ev.event.code]:
        if ev.event.value:
            keyboard.press('7')
        else:
            keyboard.release('7')

    # Manual macros to save my poor thumbs..
    if 'BTN_TL' in ecodes.bytype[ev.event.type][ev.event.code]:
        keyboard.press('up')
        time.sleep(macro_delay_press_len)
        keyboard.release('up')
        time.sleep(macro_delay_s)
        keyboard.press('down')
        time.sleep(macro_delay_press_len)
        keyboard.release('down')

    if 'BTN_TL2' in ecodes.bytype[ev.event.type][ev.event.code]:
        keyboard.press('down')
        time.sleep(macro_delay_press_len)
        keyboard.release('down')
        time.sleep(macro_delay_s)
        keyboard.press('up')
        time.sleep(macro_delay_press_len)
        keyboard.release('up')
