def main():
    from sys import stdin, stdout
    for i in range(int(next(stdin))):
        name, start_date, birth_day, num_courses = next(stdin).split()
        if int(start_date[0:4]) >= 2010 or int(birth_day[0:4]) >= 1991:
            stdout.write(f'{name} eligible\n')
        elif int(num_courses) >= 41:
            stdout.write(f'{name} ineligible\n')
        else:
            stdout.write(f'{name} coach petitions\n')

if __name__ == '__main__':
    main()
