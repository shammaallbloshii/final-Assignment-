class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        # Initialize the Client object with the given parameters.

        # Assigns a unique identifier for the client.
        self.clientID = clientID

        # Sets the name of the client.
        self.name = name

        # Records the physical address of the client.
        self.address = address

        # Stores contact information (e.g., phone, email) of the client.
        self.contactDetails = contactDetails

        # Sets the budget limit specified by the client.
        self.budget = budget

