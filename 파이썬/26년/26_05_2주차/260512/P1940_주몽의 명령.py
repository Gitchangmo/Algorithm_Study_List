import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

count = 0

nums.sort()

start_index = 0
end_index = N-1

while start_index < end_index:
    if nums[start_index] + nums[end_index] == M:
        count += 1
        start_index += 1
        end_index -= 1
    elif nums[start_index] + nums[end_index] > M:
        end_index -= 1
    else:
        start_index += 1

print(count)