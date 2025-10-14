import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = (V-B-1) // (A-B) + 1 # 꼭대기 도착하기 직전 마지막 이동거리 / 꼭대기 도착전 매일 이동거리 에 마지막 이동거리 +1을 해주면 됨

print(day)