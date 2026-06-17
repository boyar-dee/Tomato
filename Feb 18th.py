#a = input('Enter your name:')
#b = input('Enter your birth year:')
#print('Hello',a, 'your birth year is',b)

#a = input('Enter a string:')
#print(a.count("is"))

import sys
sys.stdin = open('Lettuce.txt', 'r')
sys.stdout = open('potato.txt', 'w')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b < c < d:
    print("Fish Rising")
elif a > b > c > d:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")

