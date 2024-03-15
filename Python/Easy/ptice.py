def main():
    seq_a = 'ABC'
    seq_b = 'BABC'
    seq_g = 'CCAABB'
    correct = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}
    input()
    s = input()
    for i, c in enumerate(s):
        if c == seq_a[i%3]:
            correct['Adrian'] += 1
        if c == seq_b[i%4]:
            correct['Bruno'] += 1
        if c == seq_g[i%6]:
            correct['Goran'] += 1
    m = max(correct.values())
    print(m)
    for k,v in correct.items():
        if v == m:
            print(k)


if __name__ == '__main__':
    main()
