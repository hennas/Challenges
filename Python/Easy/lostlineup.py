def main():
    _ = input()
    print(' '.join([str(entry[0]) for entry in sorted([(1,0)] + [(i+2, people_in_front) for i, people_in_front in enumerate(map(int, input().split()))], key=lambda x:x[1])]))


if __name__ == '__main__':
    main()
