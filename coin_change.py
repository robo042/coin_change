#!/usr/bin/env python3


def coin_change(coins, amount):
    ''' This is the worst possible yet still technically valid solution.
        
            O(amount*len(coins)**amount)

        You can do better.  But I don't think you can do worse. This baby isn't
        just bad, it's *comprehensively bad*.  Prove me wrong. '''
    if amount == 0:
        return 0
    p = lambda a, b: [[]] if b == 0 else [[c]+r for c in a for r in p(a, b-1)]
    for length in range(1, amount + 1):
        for combo in p(coins, length):
            if sum(combo) == amount:
                return length
    return -1


if __name__ == '__main__':

    # TIER 1 test cases
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2,3], 0) == 0
    assert coin_change([], 5) == -1
    assert coin_change([], 0) == 0
    assert coin_change([5, 10], 3) == -1
    assert coin_change([3], 9) == 3 
    assert coin_change([2], 8) == 4
    assert coin_change([5], 5) == 1 
    assert coin_change([5, 6, 7], 2) == -1 
    assert coin_change([1, 5, 10], 7) == 3   # 5 + 1 + 1
    assert coin_change([1, 3, 4, 5], 7) == 2 # 3 + 4
    assert coin_change([1, 2, 5], 11) == 3   # 5 + 5 + 1
    assert coin_change([2], 3) == -1

    # TIER 2 test cases
    assert coin_change(
            [1, 2, 5, 10, 20, 50], 99) == 6   # 50 + 20 + 20 + 5 + 2 + 2
    assert coin_change([1, 2, 5], 999) == 201 # 5*199 + 2 + 2
    assert coin_change([1], 10000) == 10000 

    # TIER 3 test cases (good luck)
    assert coin_change([5, 7, 6, 10, 16, 27, 4, 9, 51, 63], 768112) == 12193
    assert coin_change([7, 7, 6, 1, 18, 5, 17, 16, 41, 12], 1448771) == 35337
    assert coin_change([5, 4, 13, 7, 16, 9, 19, 31, 55, 16], 6799049) == 123620
