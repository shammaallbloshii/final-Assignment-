def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, cateringCompany=None,
             cleaningCompany=None, decorationsCompany=None, entertainmentCompany=None, furnitureCompany=None):
    # Initialize a new Event object with the specified attributes.

    # Mandatory event attributes
    self.eventID = eventID  # Unique identifier for the event
    self.type = type  # Type of the event, e.g., wedding, corporate
    self.theme = theme  # Theme of the event, if any
    self.date = date  # Scheduled date of the event
    self.time = time  # Scheduled start time of the event
    self.duration = duration  # Duration of the event in hours or days
    self.venueAddress = venueAddress  # Location where the event will take place
    self.clientID = clientID  # Identifier for the client booking the event

    # Optional event service providers, default to None if not specified
    self.cateringCompany = cateringCompany  # Company handling food services, if applicable
    self.cleaningCompany = cleaningCompany  # Company responsible for post-event cleaning, if applicable
    self.decorationsCompany = decorationsCompany  # Company providing decoration services, if applicable
    self.entertainmentCompany = entertainmentCompany  # Company providing entertainment services, if applicable
    self.furnitureCompany = furnitureCompany  # Company providing furniture and fixtures, if applicable
