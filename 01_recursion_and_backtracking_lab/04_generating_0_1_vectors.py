import itertools

n = int(input())

combinations = list(itertools.product([0, 1], repeat=n))

counter = 0
for combo in combinations:
    counter += 1
    print(f"#Combination: {counter} -> {''.join(map(str, combo))}")
