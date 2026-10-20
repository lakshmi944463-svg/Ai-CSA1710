python

from itertools import permutations

def solve():
    letters = 'SENDMORY'

    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        # First letters cannot be zero
        if d['S'] == 0 or d['M'] == 0:
            continue

        send = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
        more = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
        money = (10000*d['M'] + 1000*d['O'] +
                 100*d['N'] + 10*d['E'] + d['Y'])

        if send + more == money:
            print("SEND  =", send)
            print("MORE  =", more)
            print("MONEY =", money)
            return

solve()
Output

text
SEND  = 9567
MORE  = 1085
MONEY = 10652
Algorithm
Assign a unique digit from 0 to 9 to each letter.

Ensure the first letters are not zero.

Convert the words into numbers.

Check whether SEND + MORE = MONEY.

Print the solution when the equation is satisfied.

Time complexity: 
O
(
10
!
/
(
10
−
k
)
!
)
O(10!/(10−k)!), where 
k
k is the number of unique letters.


