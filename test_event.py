def test_event_initialization():
    event = Event("E01", "Wedding", "Traditional", "2024-06-15", "14:00", 6, "123 Venue St.", "C001", cateringCompany="Delicious Inc.")
    assert event.eventID == "E01"
    assert event.type == "Wedding"
    assert event.theme == "Traditional"
    assert event.date == "2024-06-15"
    assert event.time == "14:00"
    assert event.duration == 6
    assert event.venueAddress == "123 Venue St."
    assert event.clientID == "C001"
    assert event.cateringCompany == "Delicious Inc."
    assert event.cleaningCompany is None

def test_event_with_all_services():
    event = Event("E02", "Conference", "Tech", "2024-07-20", "09:00", 8, "456 Conference Blvd.", "C002", "Foodies", "CleanIt", "DecorExperts", "FunTimes", "FurniturePlus")
    assert event.decorationsCompany == "DecorExperts"
    assert event.entertainmentCompany == "FunTimes"
    assert event.furnitureCompany == "FurniturePlus"
