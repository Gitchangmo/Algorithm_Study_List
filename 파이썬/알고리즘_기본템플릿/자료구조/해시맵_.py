
new_dict = {}
print(new_dict)

new_dict["one"] = 1
new_dict["two"] = 2
new_dict["three"] = 3
print(new_dict) # {'one': 1, 'two': 2, 'three': 3}

if "one" in new_dict:
    print(new_dict['one']) # 1

count = new_dict.get("four", 0)
print(count) # 0

new_dict['four'] = 4
count = new_dict.get("four", 0)
print(count) # 4

if "two" in new_dict:
    del new_dict["two"]
    print(new_dict) # {'one': 1, 'three': 3, 'four': 4}

for key, value in new_dict.items():
    print(f"{key} : {value}")
    # one : 1
    # three : 3
    # four : 4