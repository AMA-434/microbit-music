length = 0
hertz = 0

def on_forever():
    global length, hertz
    soundExpression.giggle.play()
    length = 64
    music.play_tone(hertz, length)
    hertz += 3
basic.forever(on_forever)
