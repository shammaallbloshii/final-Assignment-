def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
    # Initialize a new instance of a class that represents a venue.
    # This constructor sets up the essential properties that each venue should have.

    self.venueID = venueID  # Assign the venueID parameter to the venueID attribute of the instance.
    # This is typically a unique identifier for the venue.

    self.name = name  # Assign the name parameter to the name attribute of the instance.
    # This is the name of the venue.

    self.address = address  # Assign the address parameter to the address attribute of the instance.
    # This holds the physical address of the venue.

    self.contact = contact  # Assign the contact parameter to the contact attribute of the instance.
    # This is used for storing contact information, possibly a phone number or email.

    self.minGuests = minGuests  # Assign the minGuests parameter to the minGuests attribute of the instance.
    # This represents the minimum number of guests that the venue can accommodate.

    self.maxGuests = maxGuests  # Assign the maxGuests parameter to the maxGuests attribute of the instance.
    # This represents the maximum number of guests the venue can accommodate.
