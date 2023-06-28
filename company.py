## allows you connect to a class from a different file
from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = [] ## for storing the employee objects of the company
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee) ## allows you to add more employees

    def display_employees(self):  ## for formatting employees
        print("List of Current Employees:")
        for i in self.employees:  ##loops over each employee in the list
            print(i.fname, i.lname)
        print("--------------------")

    def pay_employees(self):
        print("Employee Pay: ")
        for i in self.employees:
              print("Biweekly Paycheck for:", i.fname, i.lname)
              print(f"Amount ${i.calculate_paycheck():,.2f}")
              print("--------------------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Alexander", "Lawson", 72384)
    my_company.add_employee(employee1) ## tells it to add the employee
    employee2 = SalaryEmployee("Harrison", "Moenster", 90000)
    my_company.add_employee(employee2) 
    employee3 = SalaryEmployee("Larry", "Frey", 125000)
    my_company.add_employee(employee3)
    employee4 = HourlyEmployee("Jeff", "Harbaugh", 80, 30)
    my_company.add_employee(employee4)
    employee5 = HourlyEmployee("Savannah", "Carpenter", 70, 25)
    my_company.add_employee(employee5)
    employee6 = CommissionEmployee("Home", "Lander", 40000, 15, 200)
    my_company.add_employee(employee6)

    my_company.display_employees() ## calls to show the funciton in the company class that you want to show
    my_company.pay_employees() ## shows pay

main()