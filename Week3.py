print("Hello")
list = []
for amount in range(6):
    temp = float(input("pleas enter temperature " + str(amount + 1)))
    temp_cleaned = int(temp[:-1])
    if temp[-1].lower() in ("c", "f"):
        if temp[-1] == "f":
            temp_cleaned = (temp_cleaned - 32) / 1.8
        list.append(temp_cleaned)
    else:
        print("please ensure inputs have c or f")
max = max(list)
print("the hottest temperature is ", max, (max * 32) * 1.8)
print("the coolist temperature is ", min(list))
ave = round(sum(list)/len(list), 2)
print("the averige temperature is ", str(ave))