num_storages = int(input())
storages = input().split()
num_requests = int(input())
requests = input().split()

storages.sort()
requests.sort()

dic = {"S": 0, "M": 1, "L": 2}


def digitize(arr):
    for i in range(len(arr)):
        if dic.get(arr[i], -1) != -1:
            arr[i] = dic[arr[i]]
        else:
            if arr[i][-1] == "S" and len(arr[i]) > 1:
                benchmark = dic.get("S")
                benchmark = benchmark - (len(arr[i]) - 1)
                arr[i] = benchmark
            elif arr[i][-1] == "L" and len(arr[i]) > 1:
                benchmark = dic.get("L")
                benchmark = benchmark + (len(arr[i]) - 1)
                arr[i] = benchmark
    return arr


new_storages = digitize(storages)
new_requests = digitize(requests)
max_s = max(new_storages)
max_r = max(new_requests)
if max_r > max_s:
    print("No")
else:
    if sum(new_requests) < sum(new_storages):
        print("Yes")
    else:
        print("No")
