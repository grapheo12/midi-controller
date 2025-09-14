import mido
from pynput import keyboard

bank = 0

def get_midi_msg(inp):
    global bank
    try:
        inp = int(inp)
        if inp == 0:
            inp = 10
    except Exception as e:
        print("Only numbers 0-9 accepted")
        return None

    pc = bank * 10 + (inp - 1)
    if not (0 <= pc <= 127):
        print("Invalid pc:", pc, " Bank:", bank, " Input:", inp)
        return None
    return mido.Message('program_change', program=pc)



KEY_MAPS = {'j': 1, 'h': -1}

def on_press(key):
    global bank

    cmd = str(key)[1]
    if cmd == 'q':
        return

    if cmd in KEY_MAPS:
        bank += KEY_MAPS[cmd]
        print("Bank:", bank)
        return

    msg = get_midi_msg(cmd)

    if not(msg is None):
        print(msg)
        outport.send(msg)

def on_release(key):
    if str(key) == "'q'":
        # Stop listener
        return False



if __name__ == "__main__":
    outport = mido.open_output()
    print("Midi Output:", outport)
    print("Press q to exit...")
    print("Bank", bank)

    # Collect events until released, suppressing the input
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release,
            suppress=True) as listener:
        listener.join()

    outport.close()

