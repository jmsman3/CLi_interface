import os   # os--> lightweight database for easy access for command line application

class Employee:
    def __init__(self,emp_id, name , designation ,salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = float(salary)
    
    def __str__(self):
        return f"id:{self.emp_id} , Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"
    
class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        self.employees = []
        self.load_employees()
    
    def load_employees(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME ,'r') as file:
                for line in file:
                    emp_id, name ,designation,salary = line.strip().split(",")
                    self.employees.append(Employee(emp_id , name ,designation , salary))
    
    def save_employees(self):
        with open(self.FILE_NAME,'w') as file:
            for emp in self.employees:
                file.write(f"{emp.emp_id},{emp.name},{emp.designation},{emp.salary}\n")
    
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee name: ")
        designation = input("Enter Employee designation: ")
        salary = input("Enter Salary: ")
        self.employees.append(Employee(emp_id, name,designation, salary))
        self.save_employees()
        print("\nEmployee added Successfully..!\n")
    
    def update_employee(self):
        emp_id = input("Enter Employee id for Update: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = input("Enter Update Name: ") or emp.name
                emp.designation = input("Enter Update Designation: ") or emp.designation
                salary_input = input("Enter Update salary: ") or  emp.salary 
                if salary_input:
                    emp.salary = float(salary_input)
                self.save_employees()
                print("Employe Data Updated Successfully:\n")
                return 
        print("Sorry , Employee not found\n")
    
    def delete_employee(self):
        emp_id = input("Enter Employee ID: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                self.save_employees()
                print("Employee Deleted Suyccessfully..!\n")
                return
        print("OPPS,Sorry , Employee ID not Found...!\n")
    
    def view_employees(self):
        if not self.employees:
            print("\nSorry , No Employees to Display here...\n")
            return
        else:
            print() #Blank Line Print To Look better 
            for emp in self.employees:
                print(emp)
        print()  
    
    def search_employees(self):
        search_item = input("Enter name Or Designation Or Employee_ID to Search: ").lower() #lower mane all soto haat er letter for remove capital /small letter conflict
        results = []

        for emp in self.employees:
            emp_name_lower_Convert = emp.name.lower()  #lower kore nelam
            emp_designation_Lower_convert = emp.designation.lower()  #lower kore nelam
            Use_emp_id = emp.emp_id
            

            if search_item in emp_name_lower_Convert  or search_item in emp_designation_Lower_convert or search_item in Use_emp_id:
                results.append(emp)       #result er vitor search item ta append kore delam
            
        if results:
            for emp in results:
                print(emp)
        else:
            print("\nSorry, We Did Not Found any Search Result...please input the correct value")

    
#---------------------------Manager Admin pannel--------------------------------


    def Manager_Panel_Run_Kori(self):
        while(True):
            print("\n.............|| Welcome To Employee Management System ||.............")
            print("1. Add Employee: ")
            print("2. Update Employee: ")
            print("3: Delete Employee: ")
            print("4. View All Employees: ")
            print("5. Search Employee: ")
            print("6. Exit: ")
            
            choice = input("Eneter Your Choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.update_employee()
            elif choice == "3":
                self.delete_employee()
            elif choice == "4":
                self.view_employees()
            elif choice == "5":
                self.search_employees()
            elif choice == "6":
                print("\nExiting Admin Dasboard, Bye Bye...!")
            else:
                print("\nInvalid Choice. Please Try Again....!")
            
        
if __name__ ==  "__main__":

    manager = EmployeeManager()
    manager.Manager_Panel_Run_Kori()


        
            

        








        