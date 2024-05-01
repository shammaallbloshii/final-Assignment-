class Employee:
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, managerID=None):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.managerID = managerID
