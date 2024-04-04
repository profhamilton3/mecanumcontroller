def on_received_number(receivedNumber):
    joystickbit.Vibration_Motor(100)
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def my_function():
    radio.send_number(7)
    basic.show_arrow(ArrowNames.SOUTH_WEST)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def on_button_pressed_a():
    radio.send_number(12)
    basic.show_string("&")
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    radio.send_number(8)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def on_button_pressed_ab():
    radio.send_number(0)
    basic.show_string("P")
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(13)
    basic.show_string("@")
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function3():
    radio.send_number(6)
    basic.show_arrow(ArrowNames.NORTH_EAST)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    radio.send_number(5)
    basic.show_arrow(ArrowNames.NORTH_WEST)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

def on_logo_pressed():
    radio.send_number(9)
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

joystickbit.init_joystick_bit()
radio.set_group(5)
radio.set_frequency_band(33)
radio.set_transmit_power(7)
joystickbit.Vibration_Motor(500)
pY0 = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
pX0 = joystickbit.get_rocker_value(joystickbit.rockerType.X)
pX = pX0
pY = pY0
basic.show_icon(IconNames.HOUSE)

def on_forever():
    global pX, pY
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.X) - pX0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.X) < 500:
            radio.send_number(3)
            basic.show_arrow(ArrowNames.EAST)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.X) >= 500:
            radio.send_number(2)
            basic.show_arrow(ArrowNames.WEST)
        else:
            basic.show_icon(IconNames.NO)
        pX = joystickbit.get_rocker_value(joystickbit.rockerType.X)
    if abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY) > 50 and abs(joystickbit.get_rocker_value(joystickbit.rockerType.Y) - pY0) > 50:
        if joystickbit.get_rocker_value(joystickbit.rockerType.Y) < 500:
            radio.send_number(4)
            basic.show_arrow(ArrowNames.SOUTH)
        elif joystickbit.get_rocker_value(joystickbit.rockerType.Y) >= 500:
            radio.send_number(1)
            basic.show_arrow(ArrowNames.NORTH)
            music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
                music.PlaybackMode.IN_BACKGROUND)
        else:
            basic.show_icon(IconNames.NO)
        pY = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
basic.forever(on_forever)
