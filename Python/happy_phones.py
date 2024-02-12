import sys


def calculate_active_calls_for_each_interval(info):
    for cstart, cend in info['call_times']:
        for interval, (istart, iend) in enumerate(info['interval_times']):
            if cend > istart and cstart < iend:
                info['active_calls'][interval] += 1


def get_test_case_info():
    calls = 0
    intervals = 0
    test_cases = {}
    case_n = 0
    for line in sys.stdin:
        ints = list(map(int, line.split()))
        if calls + intervals == 0:
            calls, intervals = ints
            if calls + intervals == 0:
                break
            case_n += 1
            test_cases[case_n] = {
                'call_times': [],
                'interval_times': [],
                'active_calls': [0]*intervals
                }
        elif calls > 0:
            test_cases[case_n]['call_times'].append((ints[2], ints[2] + ints[3]))
            calls -= 1
        elif intervals > 0:
            test_cases[case_n]['interval_times'].append((ints[0], ints[0] + ints[1]))
            intervals -= 1
    return test_cases


if __name__ == "__main__":
    test_cases = get_test_case_info()
    for info in test_cases.values():
        calculate_active_calls_for_each_interval(info)
        for n_of_calls in info['active_calls']:
            print(n_of_calls)
