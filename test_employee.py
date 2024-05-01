def test_employee_initialization():
    emp = Employee("John Doe", 123, "Engineering", "Developer", 70000, managerID=456)
    assert emp.name == "John Doe"
    assert emp.employeeID == 123
    assert emp.department == "Engineering"
    assert emp.jobTitle == "Developer"
    assert emp.basicSalary == 70000
    assert emp.managerID == 456

def test_employee_without_manager():
    emp = Employee("Jane Smith", 124, "Marketing", "Manager", 85000)
    assert emp.name == "Jane Smith"
    assert emp.employeeID == 124
    assert emp.managerID is None
