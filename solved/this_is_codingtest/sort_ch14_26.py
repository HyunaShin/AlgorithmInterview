from itertools import combinations, permutations

def main(shuffle_idx):
    global min_compare
    if shuffle_idx >= len(shuffled_cases):
        return min_compare

    shuffle = shuffled_cases[shuffle_idx]
    for i in range(n-1):
        shuffle[i], shuffle[i+1] = [shuffle[i] + shuffle[i+1]]*2
    min_compare = min(min_compare ,sum(shuffle[:-1]))
    shuffle_idx +=1
    return  main(shuffle_idx)

if __name__ == "__main__":
    n = int(input())
    deck = []
    min_compare = 2100000001
    for _ in range(n):
        deck.append(int(input()))

    shuffled_cases = [list(x) for x in permutations(deck, n)]
    ret = main(0)
    print(ret)


