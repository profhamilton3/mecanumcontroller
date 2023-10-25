radio.onReceivedNumber(function (receivedNumber) {
    joystickbit.Vibration_Motor(100)
    basic.showNumber(receivedNumber)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    radio.sendNumber(7)
    basic.showArrow(ArrowNames.SouthWest)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(12)
    basic.showString("&")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    radio.sendNumber(8)
    basic.showArrow(ArrowNames.SouthEast)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(0)
    basic.showString("P")
    music.stopMelody(MelodyStopOptions.All)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(13)
    basic.showString("@")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    radio.sendNumber(6)
    basic.showArrow(ArrowNames.NorthEast)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    radio.sendNumber(5)
    basic.showArrow(ArrowNames.NorthWest)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendNumber(9)
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
})
joystickbit.initJoystickBit()
radio.setGroup(3)
radio.setFrequencyBand(33)
radio.setTransmitPower(7)
joystickbit.Vibration_Motor(500)
let pY0 = joystickbit.getRockerValue(joystickbit.rockerType.Y)
let pX0 = joystickbit.getRockerValue(joystickbit.rockerType.X)
let pX = pX0
let pY = pY0
basic.showIcon(IconNames.House)
basic.forever(function () {
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.X) - pX0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.X) < 500) {
            radio.sendNumber(3)
            basic.showArrow(ArrowNames.East)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.X) >= 500) {
            radio.sendNumber(2)
            basic.showArrow(ArrowNames.West)
        } else {
            basic.showIcon(IconNames.No)
        }
        pX = joystickbit.getRockerValue(joystickbit.rockerType.X)
    }
    if (Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY) > 50 && Math.abs(joystickbit.getRockerValue(joystickbit.rockerType.Y) - pY0) > 50) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.Y) < 500) {
            radio.sendNumber(4)
            basic.showArrow(ArrowNames.South)
        } else if (joystickbit.getRockerValue(joystickbit.rockerType.Y) >= 500) {
            radio.sendNumber(1)
            basic.showArrow(ArrowNames.North)
        } else {
            basic.showIcon(IconNames.No)
        }
        pY = joystickbit.getRockerValue(joystickbit.rockerType.Y)
    }
})
