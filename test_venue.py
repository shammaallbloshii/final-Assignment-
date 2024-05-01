def test_venue_initialization():
    venue = Venue("V001", "Grand Hall", "500 Venue Way", "555-0001", 100, 500)
    assert venue.venueID == "V001"
    assert venue.name == "Grand Hall"
    assert venue.address == "500 Venue Way"
    assert venue.contact == "555-0001"
    assert venue.minGuests == 100
    assert venue.maxGuests == 500
