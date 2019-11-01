num_students = input("how many students are there")
num_sweets = input("how many sweets are there")
strudets_sweets = num_sweets//num_students
left = num_sweets % num_students
print("the students get", strudets_sweets, "each")
print("there are", left, "left")