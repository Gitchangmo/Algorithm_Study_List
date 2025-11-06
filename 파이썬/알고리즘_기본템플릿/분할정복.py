''' 분할 정복 알고리즘은 큰 문제를 가장 작은 단위로 나누어서 각자 해결한 뒤에 답을 합치는 방식 '''
''' 1. 문제가 재귀적으로 동일한 구조로 더 작은 문제로 나눌 수 있을때 '''
''' 2. N의 크기가 클 때 O(logN)의 시간으로 효율적으로 알고리즘 설계 가능 '''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1

    merged.extend(left[l_idx:])
    merged.extend(right[r_idx:])

    return merged


my_list = [5, 2, 3, 7, 5, 1]

sorted_list = merge_sort(my_list)
print(sorted_list)