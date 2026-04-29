import sys
input = sys.stdin.readline

str = input().strip()
sum = 0
for i in str:
    start = 2
    plus = 0
    w = ord(i)
    if 0 <= w - ord('A') <= 2:
        plus = 1
    elif 3 <= w - ord('A') <= 5:
        plus = 2
    elif 6 <= w - ord('A') <= 8:
        plus = 3
    elif 9 <= w - ord('A') <= 11:
        plus = 4
    elif 12 <= w - ord('A') <= 14:
        plus = 5
    elif 15 <= w - ord('A') <= 18:
        plus = 6
    elif 19 <= w - ord('A') <= 21:
        plus = 7
    elif 22 <= w - ord('A') <= 25:
        plus = 8
    sum += start+plus
print(sum)