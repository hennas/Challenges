import sys

n_of_numbers = int(next(sys.stdin).split()[1])
correct_fizzbuzz = list(map(lambda n: 'fizz'*(n%3==0) + 'buzz'*(n%5==0) or str(n), range(1,n_of_numbers+1)))
least_errors = float('inf')
best_candidate = 0
for i, line in enumerate(sys.stdin):
    errors = 0
    for j, num in enumerate(line.strip().split()):
        if num != correct_fizzbuzz[j]:
            errors += 1
    if errors < least_errors:
        best_candidate = i+1
        least_errors = errors

print(best_candidate)
