ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotate(msg_half):
    rotate_val = sum([ALPH.index(char) for char in msg_half])
    return ''.join([ALPH[(ALPH.index(char) + rotate_val)%26] for char in msg_half])


def merge(f_half, s_half):
    new_msg = ''
    for i, char in enumerate(s_half):
        s_int_val = ALPH.index(char)
        f_int_val = ALPH.index(f_half[i])
        new_msg += ALPH[(f_int_val + s_int_val)%26]
    return new_msg


def main():
    msg = input()
    f_half, s_half = msg[:len(msg)//2], msg[len(msg)//2:]
    f_half = rotate(f_half)
    s_half = rotate(s_half)
    print(merge(f_half, s_half))


if __name__ == '__main__':
    main()
