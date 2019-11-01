num_students=int(input("how many students are there "))
num_sweets=int(input("how many sweets are there "))
SS = num_sweets//num_students
TS = num_sweets%num_students
print("the students get "+str(SS)+" and there are "+str(TS)+ " left")