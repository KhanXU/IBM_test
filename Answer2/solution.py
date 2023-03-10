#Read data from input file
id, status, error = [], [], []
num = int(input())
for _ in range(num):
    line = input()
    line = line.split()
    id.append(line[0])
    status.append(line[1])
    if line[1] == "true":
        continue
    else:
        error.append(line[2])

#allValid = true
allValid = True

if "false" not in status:
    print("Yes")
    print([])
else:
    print("No")
    msg = " ".join(error)
    print(msg)
