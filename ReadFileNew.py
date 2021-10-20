
print("NEW FILE")
employee_list = open("employelist.txt" , "r" )

#print (employee_list.read())   # To print entire list
#print(employee_list.readline())  # TO print just one line
#print(employee_list.readlines()) # To print entire list in an Array
#print (employee_list.read())

for employee in employee_list:
    print(employee)

employee_list.close()


employee_list_write = open("employelist.txt","a")
employee_list_write.write("7emp7  40000")
employee_list_write.write("\n8emp8  80000")

print("lets see")