def on_button_pressed_a():
    basic.show_number(10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
basic.show_leds("""
    . . . . #
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    """)
basic.show_string("Hello!")
for index in range(2):
    music.play(music.string_playable("- - D E F A F C ", 120),
        music.PlaybackMode.UNTIL_DONE)
basic.show_icon(IconNames.HAPPY)