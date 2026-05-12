import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0

for i in range(N):
    find_num = nums[i]
    start_idx = 0
    end_idx = N - 1

    while start_idx < end_idx:
        if nums[start_idx] + nums[end_idx] == find_num:
            if i != start_idx and i != end_idx:
                count += 1
                break
            elif i == start_idx:
                start_idx += 1
            elif i == end_idx:
                end_idx -= 1
        elif nums[start_idx] + nums[end_idx] > find_num:
            end_idx -= 1
            continue
        else:
            start_idx += 1
            continue

print(count)