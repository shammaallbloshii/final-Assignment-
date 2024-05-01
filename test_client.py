def test_client_initialization():
    client = Client("C001", "Alice Johnson", "789 Client Rd", "555-1234", 50000)
    assert client.clientID == "C001"
    assert client.name == "Alice Johnson"
    assert client.address == "789 Client Rd"
    assert client.contactDetails == "555-1234"
    assert client.budget == 50000
