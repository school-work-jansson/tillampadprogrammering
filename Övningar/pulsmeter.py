beats = [0]

def on_button_pressed_a():
    for n in beats:
        if n == 0:
            beats.remove(n)
    beats[len(beats)] = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def showBPM():
    bpm = 0
    # Find bpm from the past 10 seconds

    # 
    
    return bpm

def on_forever():
    basic.show_number(showBPM())
    
basic.forever(on_forever)