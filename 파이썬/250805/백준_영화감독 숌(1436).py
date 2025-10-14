import time
N = int(input())
start = time.perf_counter()
num = 666
count = 1
repeat_count = 0
while True:
    if '666' in str(num):
        if count == N:
            print(num)
            break
        count += 1
    num += 1
    repeat_count += 1

end = time.perf_counter()

print("실행 시간:", end - start, "초")
print("실행 횟수:", repeat_count)