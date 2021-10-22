class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print ("Total number of employee till now " + str(Employee.count))

    def displayEmployee(self):
        print("Name = "+self.name+" salary = "+str(self.salary))


emp1 = Employee("1David", 2000)
emp2 = Employee("2David", 12000)
emp3 = Employee("3David", 22000)

print(Employee.count)
emp1.displayEmployee()

emp1.displayCount()

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)



