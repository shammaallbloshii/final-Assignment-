# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

# Define a class to represent an employee with relevant attributes
class Employee:
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, managerID=None):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.managerID = managerID

# Define a class to represent an event with detailed attributes
class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, cateringCompany=None, cleaningCompany=None, decorationsCompany=None, entertainmentCompany=None, furnitureCompany=None):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.clientID = clientID
        self.cateringCompany = cateringCompany
        self.cleaningCompany = cleaningCompany
        self.decorationsCompany = decorationsCompany
        self.entertainmentCompany = entertainmentCompany
        self.furnitureCompany = furnitureCompany

# Define a class to represent a client
class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

# Define a class to represent a guest
class Guest:
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Define a class to represent a supplier
class Supplier:
    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Define a class to represent a venue
class Venue:
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

# Define the main GUI class for the Event Management System
class EventManagementSystemGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Event Management System")
        self.geometry("600x400")

        self.load_data()

        self.create_menu()
        self.create_buttons()

    # Create the main menu
    def create_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)

    # Create buttons for managing different entities
    def create_buttons(self):
        self.emp_button = tk.Button(self, text="Manage Employees", command=self.manage_employees)
        self.emp_button.pack(pady=10)

        self.event_button = tk.Button(self, text="Manage Events", command=self.manage_events)
        self.event_button.pack(pady=10)

        self.client_button = tk.Button(self, text="Manage Clients", command=self.manage_clients)
        self.client_button.pack(pady=10)

        self.guest_button = tk.Button(self, text="Manage Guests", command=self.manage_guests)
        self.guest_button.pack(pady=10)

        self.supplier_button = tk.Button(self, text="Manage Suppliers", command=self.manage_suppliers)
        self.supplier_button.pack(pady=10)

        self.venue_button = tk.Button(self, text="Manage Venues", command=self.manage_venues)
        self.venue_button.pack(pady=10)

    # Load data from files; handle missing files gracefully
    def load_data(self):
        try:
            with open("employees.pkl", "rb") as f:
                self.employees = pickle.load(f)
        except FileNotFoundError:
            self.employees = []

        try:
            with open("events.pkl", "rb") as f:
                self.events = pickle.load(f)
        except FileNotFoundError:
            self.events = []

        try:
            with open("clients.pkl", "rb") as f:
                self.clients = pickle.load(f)
        except FileNotFoundError:
            self.clients = []

        try:
            with open("guests.pkl", "rb") as f:
                self.guests = pickle.load(f)
        except FileNotFoundError:
            self

