import pickle

class DataHandler:
    def __init__(self):
        self.employees = []
        self.events = []
        self.clients = []
        self.guests = []
        self.suppliers = []
        self.venues = []

    def load_all_data(self):
        self.load_data("employees.pkl", self.employees)
        self.load_data("events.pkl", self.events)
        self.load_data("clients.pkl", self.clients)
        self.load_data("guests.pkl", self.guests)
        self.load_data("suppliers.pkl", self.suppliers)
        self.load_data("venues.pkl", self.venues)

    def save_all_data(self):
        self.save_data("employees.pkl", self.employees)
        self.save_data("events.pkl", self.events)
        self.save_data("clients.pkl", self)
