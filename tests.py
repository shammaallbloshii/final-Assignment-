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



def test_client_initialization():
    client = Client("C001", "Alice Johnson", "789 Client Rd", "555-1234", 50000)
    assert client.clientID == "C001"
    assert client.name == "Alice Johnson"
    assert client.address == "789 Client Rd"
    assert client.contactDetails == "555-1234"
    assert client.budget == 50000




def test_client_initialization():
    client = Client("C001", "Alice Johnson", "789 Client Rd", "555-1234", 50000)
    assert client.clientID == "C001"
    assert client.name == "Alice Johnson"
    assert client.address == "789 Client Rd"
    assert client.contactDetails == "555-1234"
    assert client.budget == 50000



def test_venue_initialization():
    venue = Venue("V001", "Grand Hall", "500 Venue Way", "555-0001", 100, 500)
    assert venue.venueID == "V001"
    assert venue.name == "Grand Hall"
    assert venue.address == "500 Venue Way"
    assert venue.contact == "555-0001"
    assert venue.minGuests == 100
    assert venue.maxGuests == 500




    def test_supplier_initialization():
        supplier = Supplier("S001", "Supply Co", "404 Supplier St", "555-7890")
        assert supplier.supplierID == "S001"
        assert supplier.name == "Supply Co"
        assert supplier.address == "404 Supplier St"
        assert supplier.contactDetails == "555-7890"





        def test_guest_initialization():
            guest = Guest("G001", "Bob Brown", "101 Guest Ave", "555-5678")
            assert guest.guestID == "G001"
            assert guest.name == "Bob Brown"
            assert guest.address == "101 Guest Ave"
            assert guest.contactDetails == "555-5678"