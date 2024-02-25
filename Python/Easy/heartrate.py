def main():
    from sys import stdin, stdout
    for entry in stdin.readlines()[1:]:
        b, p = map(float, entry.split())
        bpm = 60*b/p
        t = 60/p
        a1, a2, a3 = bpm-t, bpm, bpm+t
        stdout.write(f'{a1} {a2} {a3}\n')


if __name__ == '__main__':
    main()
