# import time

# start = time.time()
# # --- 측정할 코드 블록 ---
# for i in range(10000):
#     for j in range(10000):
#         pass
# end = time.time()   

# print("실행 시간:", end - start, "초")



# 더 정밀
import time

start = time.perf_counter()
# --- 측정할 코드 블록 ---
for i in range(100000000):
    pass
end = time.perf_counter()

print("실행 시간:", end - start, "초")
