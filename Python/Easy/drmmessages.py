ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotate(msg_half):
    new_half = ''
    rotate_val = sum([ALPH.index(char) for char in msg_half])
    for char in msg_half:
        int_val = ALPH.index(char)
        for _ in range(rotate_val):
            int_val += 1
            if int_val > 25:
                int_val = 0
        new_half += ALPH[int_val]
    return new_half


def merge(f_half, s_half):
    new_msg = ''
    for i, char in enumerate(s_half):
        s_int_val = ALPH.index(char)
        f_int_val = ALPH.index(f_half[i])
        for i in range(s_int_val):
            f_int_val += 1
            if f_int_val > 25:
                f_int_val = 0
        new_msg += ALPH[f_int_val]
    return new_msg


def main():
    msg = input()
    f_half, s_half = msg[:len(msg)//2], msg[len(msg)//2:]
    f_half = rotate(f_half)
    s_half = rotate(s_half)
    print(merge(f_half, s_half))


if __name__ == '__main__':
    main()
