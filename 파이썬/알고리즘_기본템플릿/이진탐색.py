
def binary_search(nums, target):
    global count
    
    start = 0
    end = len(nums)
    while start <= end:
        count += 1
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 

count = 0 

nums = [6, 2, 4 ,1 ,8, 24, 31, 35, 77, 24, 75, 82, 13, 90, 55]
nums.sort()
print(nums)

target = 31
index = binary_search(nums, target)
print(f"{nums[index]}은 {index}번째에~ ")
print(f"{len(nums)}길이 배열에서 반복수 : {count}")