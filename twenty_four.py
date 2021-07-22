from itertools import permutations

TARGET = 24
CALCS = ['+','-','*','/']

def calc(x, y, op):
    if op == 0:
        return x+y
    if op == 1:
        return x-y
    if op == 2: 
        return x*y
    if op == 3:
        if y==0: 
            return None
        else:
            return x/y


def solve(card):
    solution_set = set()
    perms = permutations(card)
    for perm in perms:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    # Method 1
                    x = calc(perm[0], perm[1], i)
                    y = calc(perm[2], perm[3], j)
                    result = calc(x, y, k)
                    if result == TARGET:
                        solution = f'({perm[0]} {CALCS[i]} {perm[1]}) {CALCS[k]} ({perm[2]} {CALCS[j]} {perm[3]}) = {TARGET}'
                        solution_set.add(solution)
                    # Method 2
                    a = calc(perm[0], perm[1], i)
                    b = calc(a, perm[2], j)
                    result = calc(b, perm[3], k)
                    if result == TARGET:
                        solution = f'(({perm[0]} {CALCS[i]} {perm[1]}) {CALCS[j]} {perm[2]}) {CALCS[k]} {perm[3]}) = {TARGET}'
                        solution_set.add(solution)
    solution_count = len(solution_set)
    print(f"There {'is' if solution_count==1 else 'are'} {solution_count} solution{'s' if solution_count!=1 else ''} for {card}.")
    if input("Show solutions (y/n)? ") == "y":
        for solution in solution_set:
            print(solution)

def main():
    while True:
        card_str = input("Enter a card: ")
        if card_str == "":
            break
        card_list = [int(i) for i in card_str.split(",")]
        solve(card_list)


if __name__=="__main__":
    main()
    #solve([1,2,3,4])
    #solve([3,7,8,4])
    #solve([8,3,3,1])