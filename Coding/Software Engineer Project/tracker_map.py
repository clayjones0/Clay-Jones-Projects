import tkinter as tk
from tkinter import Label, messagebox, ttk, simpledialog
from tkintermapview import TkinterMapView # type: ignore
from PIL import Image, ImageTk
from pathlib import Path
import math
import smtplib
from email.mime.text import MIMEText

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar

contacts = []

class BoundedMapView(TkinterMapView):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.bind("<Motion>", self.check_bounds)

def refresh_map():
    # Update map data here (e.g., fetch real-time shuttle locations)
    gmap_widget.set_position(36.847896, -76.260920)  # Update center if needed
    gmap_widget.set_zoom(16)

def alert_driver():
    messagebox.showinfo("Alert", "Alerting driver...")

def is_valid_email(email):
    #checks email
    return email.endswith("@gmail.com") or email.endswith("@outlook.com") or email.endswith("@spartans.nsu.edu")

def alert_pickup():
    messagebox.showinfo("Place Pick-Up", "Placing Pick-Up. Press \"OK\" to enter Name and Email")

    def submit():
        name_value = name_entry.get()
        email_value = email_entry.get().lower()  # Ensure email is lowercase for comparison

        if name_value and is_valid_email(email_value):
            contact = {"name": name_value, "email": email_value, "location": selected_time.get()}
            contacts.append(contact)  # Add contact to the list
            

            messagebox.showinfo("Place Pick-Up", f"Thank you, {name_value}! Pick-Up scheduled for {selected_time.get()}. You'll be contacted at {email_value} when ready!")
            

            sender_email = ''
            username = ''
            password = ''

            nsu_email = 'NSU-SHUTTLE-SERVICE@outlook.com'
            #Spoofed full name
            nsu_name = 'NSU Shuttle Services'
            #Victim e-mail address 
            reciever_email = f'{email_value}' 
            # E-mail subject 
            subject= "Your order has been placed\n"
            # E-mail body message
            body = f"Your order has been placed for {selected_time.get()} and you've been added to the pick up list.\n Thank you for using our services!"
            
            header = ('To:' + reciever_email + '\n' +'From: ' + nsu_name + ' <' + nsu_email + '>' + '\n' + 'Subject:' + subject)
            message = (header + '\n\n' + body + '\n\n')
            
            try:
                session = smtplib.SMTP('smtp.gmail.com','587')
                session.starttls()
                session.login(username, password)
                session.sendmail(sender_email, reciever_email, message)
                session.quit()
                print("Email Sent With Success!")
            except smtplib.SMTPException:
                print("Error: Unable To Send The Email!")

        else:
            if not name_value and not email_value:
                messagebox.showwarning("Missing Information", "Name and email are required!")
            else:
                messagebox.showerror("Invalid Email", "Please enter a valid email address ending in @gmail.com, @outlook.com, or @spartans.nsu.edu")

       
        

    root = tk.Tk()
    root.title("Place Pick-Up")

    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    email_label = tk.Label(root, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1, padx=10, pady=5)


    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    root.destroy



                
def print_contacts():
        if contacts:
            output_string = "Pick-Up Waitlist:\n"
            for contact in contacts:
                output_string += f"- {contact['name']} ({contact['email']})\n"
            messagebox.showinfo("Waiting: ", output_string)
        else:
            messagebox.showinfo("Pick_Up Waitlist", "There are no one currently stored.")


def remove_from_waitlist():

    if not contacts:
        messagebox.showinfo("Pick-Up Waitlist", "There are currently no one waiting for pick-up.")
        return

    name = tk.simpledialog.askstring("Remove Contact", "Enter the name of the contact to remove:")
    email = tk.simpledialog.askstring("Remove Contact", "Enter the email of the contact to remove:")

    if not (name and email):
        messagebox.showwarning("Missing Information", "Please enter both name and email.")
        return

    email = email.lower()  # Ensure case-insensitive search

    contact_found = False
    for i, contact in enumerate(contacts):
        if contact["name"] == name and contact["email"] == email:
            contact_found = True
            del contacts[i]  # Remove the contact from the list using index deletion
            break

    if contact_found:
        messagebox.showinfo("Pick-Up Waitlist", f"{name} ({email}) has been removed from the waitlist.")
    else:
        messagebox.showinfo("Pick-Up Waitlist", "Contact not found. Please check the name and email.")

def shuttle_hours():
    messagebox.showinfo("Shuttle Schedule", "Run Time:\nMonday: 7:30 AM - 8:30 PM \n Tuesday: 7:30 AM - 8:30 PM\n Wednesday: 7:30 AM - 8:30 PM\n Thursday: 7:30 AM - 8:30 PM\n Friday: 7:30 AM - 8:30 PM\n Saturday: 7:30 AM - 7:30 PM\n Sunday: 7:30 AM - 7:30 PM")

lat_list = [36.847223, 36.847334, 36.847031, 36.848985, 36.846705, 36.849086]
long_list = [-76.261923, -76.268818, -76.257554, -76.260881, -76.265315, -76.265608]

lat_list2 = [36.848985, 36.846144, 36.848256, 36.848750, 36.848578, 36.850500 ]
long_list2 = [-76.260881, -76.266804, -76.268875, -76.266182, -76.257254, -76.265315]

def update_marker_coordinates(index):
    if index >= len(lat_list):
        return
    
    # Update the coordinates of the existing marker
    shuttle_marker.set_position(lat_list[index], long_list[index])
    shuttle_marker2.set_position(lat_list2[index], long_list2[index])
    # Schedule next update after 5 seconds
    win.after(15000, update_marker_coordinates, index + 1)



win = tk.Tk()

# Create a frame with dimensions 1100x500 and a light grey border
map_frame = tk.Frame(win, width=1100, height=500, highlightbackground="light grey", highlightthickness=1)
map_frame.pack()

# Create a frame with dimensions 1100x500 and a light grey border
map_frame2 = tk.Frame(win, width=1100, height=200,  highlightbackground="light grey", highlightthickness=1)
map_frame2.pack()

# Create the map widget inside the frame
gmap_widget = TkinterMapView(map_frame, width=1100, height=500)
gmap_widget.pack(fill="both", expand=True)

#map server
gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=16) #lyrs = m for roadmap standard
gmap_widget.set_address("34-38 Presidential Pkwy, Norfolk, VA 23504", expand=True)

#markers

shuttle_stop_marker1 = gmap_widget.set_marker(36.847031, -76.257554, text="PUA 1", marker_color_circle="yellow", marker_color_outside="grey")
shuttle_stop_marker1 = gmap_widget.set_marker(36.848985, -76.260881, text="PUA 2", marker_color_circle="yellow", marker_color_outside="grey")
shuttle_stop_marker1 = gmap_widget.set_marker(36.846705, -76.265315, text="PUA 3", marker_color_circle="yellow", marker_color_outside="grey")
shuttle_stop_marker1 = gmap_widget.set_marker(36.849086, -76.265608, text="PUA 4", marker_color_circle="yellow", marker_color_outside="grey")
shuttle_stop_marker1 = gmap_widget.set_marker(36.848031, -76.258930, text="PUA 5", marker_color_circle="yellow", marker_color_outside="grey")

# Create a marker with the initial coordinates
shuttle_marker = gmap_widget.set_marker(lat_list[0], long_list[0], text="Shuttle 1", marker_color_circle="green", marker_color_outside="green")
shuttle_marker2 = gmap_widget.set_marker(lat_list2[0], long_list2[0], text="Shuttle 2", marker_color_circle="green", marker_color_outside="green")

# Start updating marker coordinates with a delay of 5 seconds between each update
update_marker_coordinates(1)



# Create a Canvas widget within the map_frame to draw the rectangle
canvas = tk.Canvas(map_frame, bg="#D9D9D9", width=1100, height=500, bd=0, highlightthickness=0)
canvas.pack()

#lx,ly,rx,ry
# Draw the time box
canvas.create_rectangle(15, 15,350,185, fill="white", outline="black")
canvas.create_rectangle(75, 25,290,55, fill="white", outline="black")
canvas.create_text(93.0, 28, anchor="nw", text="Schedualing Box", fill="#000000",font=("koho", 24 * -1))
run_time_button = tk.Button(win, text="The Shuttle\n Schedule", font=("koho", 15 * -1),bd=1,  command=shuttle_hours, bg= "gold", highlightthickness=2, highlightcolor="black")
run_time_button.place(x=75, y=590)  # Adjust coordinates as needed

books_button = tk.Button(win, text="The Booking\n Schedule", font=("koho", 15 * -1),bd=1,  command=print_contacts, bg= "gold", highlightthickness=2, highlightcolor="black")
books_button.place(x=197, y=567)  # Adjust coordinates as needed

remove_button = tk.Button(win, text="Remove Booking", command=remove_from_waitlist, bg= "gold", highlightthickness=2, highlightcolor="black")
remove_button.place(x=194, y=627)



#The pick up box
canvas.create_rectangle(370, 15,790,185, fill="white", outline="black")
canvas.create_rectangle(430, 25,730,55, fill="white", outline="black")
canvas.create_text(470.0, 28, anchor="nw", text="SHUTTLE BOOKING", fill="#000000",font=("koho", 24 * -1))
canvas.create_text(390.0, 75, anchor="nw", text="Destination:", fill="#000000",font=("koho", 21 * -1))
canvas.create_text(390.0, 125, anchor="nw", text="Location:", fill="#000000",font=("koho", 21 * -1))

#time drop down /do time range
times = ["Pick up Area 1", "Pick up Area 2", "Pick up Area 3", "Pick up Area 4", "Pick up Area 5", "Request to Driver"]
selected_time = StringVar()
time_dropdown = ttk.Combobox(canvas, textvariable=selected_time, values=times, height= 10, width=20, state="readonly")
time_dropdown.place(x=506, y=77)  # Adjust coordinates as needed
time_dropdown.set("Pick up Area 1")  # Set initial text
time = time_dropdown.set("Pick up Area 1")  # Set initial text

#location dropdown
locations = ["Pick up Area 1", "Pick up Area 2", "Pick up Area 3", "Pick up Area 4", "Pick up Area 5"]
selected_location = StringVar()
location_dropdown = ttk.Combobox(canvas, textvariable=selected_location, values=locations, height= 10, width=20, state="readonly")
location_dropdown.place(x=485, y=128)  # Adjust coordinates as needed
location_dropdown.set("Pick up Area 1")  # Set initial text

#place order button
place_button = tk.Button(win, text="Schedule", font=("koho", 15 * -1),bd=1,  command=alert_pickup)
place_button.place(x=670, y=627)  # Adjust coordinates as needed




#Emergency Box
canvas.create_rectangle(810, 15, 1085,185, fill="white", outline="black")
image2 = Image.open("C:/Users/c2m3j/OneDrive/Documents/Shuttle_App/The_map/stop_button.png")
width, height = 125, 125  # Adjust width and height as needed
image = image2.resize((width, height), Image.BICUBIC)
stop_img = ImageTk.PhotoImage(image)
stop_button = tk.Button(win, image=stop_img,bd=0,  command=alert_driver)
stop_button.image = stop_img  # Keep a reference to avoid garbage collection
stop_button.place(x=883, y=536)  # Adjust coordinates as needed




# Create a button for refresh
image = Image.open("C:/Users/c2m3j/OneDrive/Documents/Shuttle_App/The_map/refresh_button.png")
width, height = 50, 50  # Adjust width and height as needed
image = image.resize((width, height), Image.BICUBIC)
refresh_img = ImageTk.PhotoImage(image)
refresh_button = tk.Button(win, image=refresh_img, command=refresh_map)
refresh_button.image = refresh_img  # Keep a reference to avoid garbage collection
refresh_button.place(x=1040, y=10)  # Adjust coordinates as needed


"""
functioning requirements, 
interactive map that highlights the nsu campus, the area around the campus to explore, shows the location of the shuttle(simulates movement), 
the location of pick-up spots and refreshes so the user can focus the map on the nsu area

A pick up schueling feature that allows the user to pick from marker points, sends an email for confirmation, give space to input name and email
and adds it to a list of people to pick up for the driver (put in left side along with shuttle scheduel)

a log in feature that only allows nsu emails using database
"""

#sizing and window name
win.geometry("1100x700")
win.title("Shuttle Tracker")
win.resizable(False, False)
win.mainloop()