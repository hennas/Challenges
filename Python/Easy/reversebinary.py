def main():
   print(int(bin(int(input())).replace('0b', '')[::-1], 2))


if __name__ == '__main__':
    main()
