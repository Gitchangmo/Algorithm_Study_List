X = int(input())

# 누적합 정방향
# layer = 1
# sum = 1
# while X > sum:
#     layer += 1
#     sum += layer

# sum -= layer

# if layer % 2 == 0:
#     top = X - sum
#     bottom = layer - (X - sum) + 1
# else:
#     top = layer - (X - sum) + 1
#     bottom = X - sum

# print(f"{top}/{bottom}")


# 누적합 역방향
layer = 1
while X > layer:
    X -= layer
    layer += 1

if layer % 2 == 0:
    top = X
    bottom = layer - X + 1
else:
    top = layer - X + 1
    bottom = X

print(f"{top}/{bottom}")
