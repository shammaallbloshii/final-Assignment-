import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

class Employee:
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, managerID=None):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.managerID = managerID

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

class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

class Guest:
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

class Supplier:
    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

class Venue:
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

class EventManagementSystemGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Event Management System")
        self.geometry("600x400")

        self.load_data()

        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)

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
            self.guests = []

        try:
            with open("suppliers.pkl", "rb") as f:
                self.suppliers = pickle.load(f)
        except FileNotFoundError:
            self.suppliers = []

        try:
            with open("venues.pkl", "rb") as f:
                self.venues = pickle.load(f)
        except FileNotFoundError:
            self.venues = []

    def save_data(self):
        with open("employees.pkl", "wb") as f:
            pickle.dump(self.employees, f)

        with open("events.pkl", "wb") as f:
            pickle.dump(self.events, f)

        with open("clients.pkl", "wb") as f:
            pickle.dump(self.clients, f)

        with open("guests.pkl", "wb") as f:
            pickle.dump(self.guests, f)

        with open("suppliers.pkl", "wb") as f:
            pickle.dump(self.suppliers, f)

        with open("venues.pkl", "wb") as f:
            pickle.dump(self.venues, f)

    def manage_employees(self):
        emp_window = tk.Toplevel(self)
        emp_window.title("Manage Employees")

        tk.Label(emp_window, text="Employee Name:").grid(row=0, column=0)
        name_entry = tk.Entry(emp_window)
        name_entry.grid(row=0, column=1)

        tk.Label(emp_window, text="Employee ID:").grid(row=1, column=0)
        emp_id_entry = tk.Entry(emp_window)
        emp_id_entry.grid(row=1, column=1)

        tk.Label(emp_window, text="Department:").grid(row=2, column=0)
        department_entry = tk.Entry(emp_window)
        department_entry.grid(row=2, column=1)

        tk.Label(emp_window, text="Job Title:").grid(row=3, column=0)
        job_title_entry = tk.Entry(emp_window)
        job_title_entry.grid(row=3, column=1)

        tk.Label(emp_window, text="Basic Salary:").grid(row=4, column=0)
        salary_entry = tk.Entry(emp_window)
        salary_entry.grid(row=4, column=1)

        tk.Label(emp_window, text="Manager ID:").grid(row=5, column=0)
        manager_id_entry = tk.Entry(emp_window)
        manager_id_entry.grid(row=5, column=1)

        def add_employee():
            name = name_entry.get()
            emp_id = emp_id_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            salary = salary_entry.get()
            manager_id = manager_id_entry.get()

            if not name or not emp_id or not department or not job_title or not salary:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                salary = float(salary)
            except ValueError:
                messagebox.showerror("Error", "Invalid salary format.")
                return

            employee = Employee(name, emp_id, department, job_title, salary, manager_id)
            self.employees.append(employee)
            self.save_data()
            messagebox.showinfo("Success", "Employee added successfully.")
            emp_window.destroy()

        tk.Button(emp_window, text="Add Employee", command=add_employee).grid(row=6, columnspan=2)

    def manage_events(self):
        event_window = tk.Toplevel(self)
        event_window.title("Manage Events")

        tk.Label(event_window, text="Event ID:").grid(row=0, column=0)
        event_id_entry = tk.Entry(event_window)
        event_id_entry.grid(row=0, column=1)

        tk.Label(event_window, text="Type:").grid(row=1, column=0)
        type_entry = tk.Entry(event_window)
        type_entry.grid(row=1, column=1)

        tk.Label(event_window, text="Theme:").grid(row=2, column=0)
        theme_entry = tk.Entry(event_window)
        theme_entry.grid(row=2, column=1)

        tk.Label(event_window, text="Date (YYYY-MM-DD):").grid(row=3, column=0)
        date_entry = tk.Entry(event_window)
        date_entry.grid(row=3, column=1)

        tk.Label(event_window, text="Time (HH:MM):").grid(row=4, column=0)
        time_entry = tk.Entry(event_window)
        time_entry.grid(row=4, column=1)

        tk.Label(event_window, text="Duration (hrs):").grid(row=5, column=0)
        duration_entry = tk.Entry(event_window)
        duration_entry.grid(row=5, column=1)

        tk.Label(event_window, text="Venue Address:").grid(row=6, column=0)
        venue_entry = tk.Entry(event_window)
        venue_entry.grid(row=6, column=1)

        tk.Label(event_window, text="Client ID:").grid(row=7, column=0)
        client_id_entry = tk.Entry(event_window)
        client_id_entry.grid(row=7, column=1)

        def add_event():
            event_id = event_id_entry.get()
            type = type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_entry.get()
            client_id = client_id_entry.get()

            if not event_id or not type or not theme or not date or not time or not duration or not venue_address or not client_id:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                date = datetime.strptime(date, "%Y-%m-%d").date()
                time = datetime.strptime(time, "%H:%M").time()
                duration = float(duration)
            except ValueError:
                messagebox.showerror("Error", "Invalid date, time, or duration format.")
                return

            event = Event(event_id, type, theme, date, time, duration, venue_address, client_id)
            self.events.append(event)
            self.save_data()
            messagebox.showinfo("Success", "Event added successfully.")
            event_window.destroy()

        tk.Button(event_window, text="Add Event", command=add_event).grid(row=8, columnspan=2)


    def manage_clients(self):
        client_window = tk.Toplevel(self)
        client_window.title("Manage Clients")

        tk.Label(client_window, text="Client ID:").grid(row=0, column=0)
        client_id_entry = tk.Entry(client_window)
        client_id_entry.grid(row=0, column=1)

        tk.Label(client_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(client_window)
        name_entry.grid(row=1, column=1)

        tk.Label(client_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(client_window)
        address_entry.grid(row=2, column=1)

        tk.Label(client_window, text="Contact Details:").grid(row=3, column=0)
        contact_entry = tk.Entry(client_window)
        contact_entry.grid(row=3, column=1)

        tk.Label(client_window, text="Budget:").grid(row=4, column=0)
        budget_entry = tk.Entry(client_window)
        budget_entry.grid(row=4, column=1)

        def add_client():
            client_id = client_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_entry.get()
            budget = budget_entry.get()

            if not client_id or not name or not address or not contact_details or not budget:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                budget = float(budget)
            except ValueError:
                messagebox.showerror("Error", "Invalid budget format.")
                return

            client = Client(client_id, name, address, contact_details, budget)
            self.clients.append(client)
            self.save_data()
            messagebox.showinfo("Success", "Client added successfully.")
            client_window.destroy()

        tk.Button(client_window, text="Add Client", command=add_client).grid(row=5, columnspan=2)

    def manage_guests(self):
        guest_window = tk.Toplevel(self)
        guest_window.title("Manage Guests")

        tk.Label(guest_window, text="Guest ID:").grid(row=0, column=0)
        guest_id_entry = tk.Entry(guest_window)
        guest_id_entry.grid(row=0, column=1)

        tk.Label(guest_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(guest_window)
        name_entry.grid(row=1, column=1)

        tk.Label(guest_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(guest_window)
        address_entry.grid(row=2, column=1)

        tk.Label(guest_window, text="Contact Details:").grid(row=3, column=0)
        contact_entry = tk.Entry(guest_window)
        contact_entry.grid(row=3, column=1)

        def add_guest():
            guest_id = guest_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_entry.get()

            if not guest_id or not name or not address or not contact_details:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            guest = Guest(guest_id, name, address, contact_details)
            self.guests.append(guest)
            self.save_data()
            messagebox.showinfo("Success", "Guest added successfully.")
            guest_window.destroy()

        tk.Button(guest_window, text="Add Guest", command=add_guest).grid(row=4, columnspan=2)

    def manage_suppliers(self):
        supplier_window = tk.Toplevel(self)
        supplier_window.title("Manage Suppliers")

        tk.Label(supplier_window, text="Supplier ID:").grid(row=0, column=0)
        supplier_id_entry = tk.Entry(supplier_window)
        supplier_id_entry.grid(row=0, column=1)

        tk.Label(supplier_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(supplier_window)
        name_entry.grid(row=1, column=1)

        tk.Label(supplier_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(supplier_window)
        address_entry.grid(row=2, column=1)

        tk.Label(supplier_window, text="Contact Details:").grid(row=3, column=0)
        contact_entry = tk.Entry(supplier_window)
        contact_entry.grid(row=3, column=1)

        def add_supplier():
            supplier_id = supplier_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_entry.get()

            if not supplier_id or not name or not address or not contact_details:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            supplier = Supplier(supplier_id, name, address, contact_details)
            self.suppliers.append(supplier)
            self.save_data()
            messagebox.showinfo("Success", "Supplier added successfully.")
            supplier_window.destroy()

        tk.Button(supplier_window, text="Add Supplier", command=add_supplier).grid(row=4, columnspan=2)

    def manage_venues(self):
        venue_window = tk.Toplevel(self)
        venue_window.title("Manage Venues")

        tk.Label(venue_window, text="Venue ID:").grid(row=0, column=0)
        venue_id_entry = tk.Entry(venue_window)
        venue_id_entry.grid(row=0, column=1)

        tk.Label(venue_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(venue_window)
        name_entry.grid(row=1, column=1)

        tk.Label(venue_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(venue_window)
        address_entry.grid(row=2, column=1)

        tk.Label(venue_window, text="Contact:").grid(row=3, column=0)
        contact_entry = tk.Entry(venue_window)
        contact_entry.grid(row=3, column=1)

        tk.Label(venue_window, text="Minimum Guests:").grid(row=4, column=0)
        min_guests_entry = tk.Entry(venue_window)
        min_guests_entry.grid(row=4, column=1)

        tk.Label(venue_window, text="Maximum Guests:").grid(row=5, column=0)
        max_guests_entry = tk.Entry(venue_window)
        max_guests_entry.grid(row=5, column=1)

        def add_venue():
            venue_id = venue_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            if not venue_id or not name or not address or not contact or not min_guests or not max_guests:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                min_guests = int(min_guests)
                max_guests = int(max_guests)
            except ValueError:
                messagebox.showerror("Error", "Invalid minimum or maximum guests format.")
                return

            venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
            self.venues.append(venue)
            self.save_data()
            messagebox.showinfo("Success", "Venue added successfully.")
            venue_window.destroy()

        tk.Button(venue_window, text="Add Venue", command=add_venue).grid(row=6, columnspan=2)

if __name__ == "__main__":
    app = EventManagementSystemGUI()
    app.mainloop()
