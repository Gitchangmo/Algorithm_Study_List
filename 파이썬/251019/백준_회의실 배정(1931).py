import sys
input = sys.stdin.readline

N = int(input())

meeting = []
end_time = 0
count = 0

for i in range(N):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))

for start, end in meeting:
    if end_time <= start:
        count += 1
        end_time = end

print(count)

