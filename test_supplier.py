def test_supplier_initialization():
    supplier = Supplier("S001", "Supply Co", "404 Supplier St", "555-7890")
    assert supplier.supplierID == "S001"
    assert supplier.name == "Supply Co"
    assert supplier.address == "404 Supplier St"
    assert supplier.contactDetails == "555-7890"
