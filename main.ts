radio.onReceivedNumber(function (receivedNumber) {
    joystickbit.Vibration_Motor(100)
    basic.showNumber(receivedNumber)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    radio.sendNumber(4)
    basic.showArrow(ArrowNames.South)
    basic.pause(200)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showString("A")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    radio.sendNumber(11)
    basic.showArrow(ArrowNames.East)
    basic.pause(200)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(0)
    basic.showString("B")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    radio.sendNumber(1)
    basic.showArrow(ArrowNames.North)
    basic.pause(200)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    radio.sendNumber(10)
    basic.showArrow(ArrowNames.West)
    basic.pause(200)
})
joystickbit.initJoystickBit()
radio.setGroup(1)
radio.setFrequencyBand(16)
radio.setTransmitPower(7)
joystickbit.Vibration_Motor(500)
let pY0 = joystickbit.getRockerValue(joystickbit.rockerType.Y)
let pX0 = joystickbit.getRockerValue(joystickbit.rockerType.X)
let pX = pX0
let pY = pY0
basic.showIcon(IconNames.Meh)
basic.forever(function () {
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.X) < 500) {
            radio.sendNumber(3)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.X) >= 500) {
            radio.sendNumber(2)
        } else {
            basic.showIcon(IconNames.No)
        }
        pX = joystickbit.getRockerValue(joystickbit.rockerType.X)
    }
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.Y) < 500) {
            radio.sendNumber(4)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.Y) >= 500) {
            radio.sendNumber(1)
        } else {
            basic.showIcon(IconNames.No)
        }
        pY = joystickbit.getRockerValue(joystickbit.rockerType.Y)
    }
    basic.pause(200)
})
