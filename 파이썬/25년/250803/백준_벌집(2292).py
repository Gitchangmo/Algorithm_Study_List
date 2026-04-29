import sys
input = sys.stdin.readline

num = int(input())

count = 1
layer = 1

while num > count:
    count += 6 * layer
    layer += 1

print(layer)