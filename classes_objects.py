class Employee:
    empCount = 0

    def __init__(self, first, last, pay): # Constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.empCount = Employee.empCount + 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.first,  "- Salary:", self.pay)
emp1 = Employee("Chris", "Moreano", 20000)

emp1.displayEmployee()

loopControl = True
employeeList = []
while( loopControl == True):


    tempfirst = input("Enter Name")
    templast = input("Enter Last Name")
    tempay = input("Enter Current Pay")
    tempemail = input("Enter email")

    submitControl = input("Would you like to submit? y/n ")

    if(submitControl == 'y'):
        employeeList.append(Employee(tempfirst,templast,tempay))

    elif (submitControl == 'n'):



