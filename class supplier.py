class Supplier:
    def __init__(self, supplierID, name, address, contactDetails):
        # Initialize a new instance of Supplier.

        # Assign the supplierID to the supplierID attribute of the instance.
        # supplierID is expected to be a unique identifier for the supplier.
        self.supplierID = supplierID

        # Assign the name to the name attribute of the instance.
        # This is usually the full name of the supplier.
        self.name = name

        # Assign the address to the address attribute of the instance.
        # This should contain the physical address of the supplier.
        self.address = address

        # Assign the contactDetails to the contactDetails attribute of the instance.
        # This should include contact information such as phone number, email, etc.
        self.contactDetails = contactDetails
