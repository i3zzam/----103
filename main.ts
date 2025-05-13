input.onButtonPressed(Button.A, function () {
    basic.showNumber(10)
})
input.onGesture(Gesture.Shake, function () {
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Yes)
})
basic.showIcon(IconNames.Heart)
basic.showLeds(`
    . . . . #
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.showString("Hello!")
for (let index = 0; index < 2; index++) {
    music.play(music.stringPlayable("- - D E F A F C ", 120), music.PlaybackMode.UntilDone)
}
basic.showIcon(IconNames.Happy)
