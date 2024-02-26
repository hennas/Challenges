def main():
    inp = input()
    is_alive = ':)' in inp
    is_undead = ':(' in inp
    if is_alive and is_undead:
        print('double agent')
    elif is_alive and not is_undead:
        print('alive')
    elif not is_alive and is_undead:
        print('undead')
    else:
        print('machine')


if __name__ == '__main__':
    main()
