from sys import stdin


def main():
    space_counts = dict()
    total_bytes = 0

    total_files = int(next(stdin))
    for i in range(total_files):
        total_lines = int(next(stdin))
        for j in range(total_lines):
            spaces_on_line = int(next(stdin))
            if spaces_on_line > 0:
                try:
                    space_counts[spaces_on_line] += 1
                except KeyError:
                    space_counts[spaces_on_line] = 1
                total_bytes += spaces_on_line

    max_tab_size = max(space_counts.keys()) if space_counts.keys() else 1
    custom_tab_size = 0
    most_bytes_saved = float('-inf')

    for tab_size in range(1, max_tab_size+1):
        new_total_bytes = 0

        for key, value in space_counts.items():
            total_tabs = key // tab_size
            extra_spaces = key % tab_size
            new_bytes = (total_tabs + extra_spaces) * value
            new_total_bytes += new_bytes

        saved_bytes = total_bytes - new_total_bytes
        if saved_bytes > most_bytes_saved:
            custom_tab_size = tab_size
            most_bytes_saved = saved_bytes

    print(custom_tab_size, most_bytes_saved, sep='\n')


if __name__ == '__main__':
    main()
