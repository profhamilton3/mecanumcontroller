def on_received_number(receivedNumber):
    joystickbit.Vibration_Motor(100)
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def my_function():
    radio.send_number(4)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.pause(200)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def on_button_pressed_a():
    radio.send_number(1)
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    radio.send_number(11)
    basic.show_arrow(ArrowNames.EAST)
    basic.pause(200)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def on_button_pressed_b():
    radio.send_number(0)
    basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function3():
    radio.send_number(1)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(200)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    radio.send_number(10)
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(200)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

joystickbit.init_joystick_bit()
radio.set_group(1)
radio.set_frequency_band(16)
radio.set_transmit_power(7)
joystickbit.Vibration_Motor(500)
pY0 = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
pX0 = joystickbit.get_rocker_value(joystickbit.rockerType.X)
pX = pX0
pY = pY0
basic.show_icon(IconNames.MEH)

def on_forever():
    global pX, pY
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.X) < 500:
            radio.send_number(3)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.X) >= 500:
            radio.send_number(2)
        else:
            basic.show_icon(IconNames.NO)
        pX = joystickbit.get_rocker_value(joystickbit.rockerType.X)
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.Y) < 500:
            radio.send_number(4)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.Y) >= 500:
            radio.send_number(1)
        else:
            basic.show_icon(IconNames.NO)
        pY = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
    basic.pause(200)
basic.forever(on_forever)
