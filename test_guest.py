def test_guest_initialization():
    guest = Guest("G001", "Bob Brown", "101 Guest Ave", "555-5678")
    assert guest.guestID == "G001"
    assert guest.name == "Bob Brown"
    assert guest.address == "101 Guest Ave"
    assert guest.contactDetails == "555-5678"
