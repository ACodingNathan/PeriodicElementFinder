import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import requests
from io import StringIO


# Function to search for an element in the CSV file
def search_element():
    # Ask the user to input an element using a dialog box
    element = simpledialog.askstring("Element Search", "Enter an element of the periodic table:")

    # Download the CSV file from the URL
    url = 'https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv'
    response = requests.get(url)
    data = response.content.decode('utf-8')

    # Open the CSV file for reading using StringIO
    csv_reader = csv.reader(StringIO(data))
    found = False

    # Search for the element in the CSV file and store all rows for table display
    table_data = []
    header_row = next(csv_reader)  # Get the header row (row 0)

    for row in csv_reader:
        if element.lower() == row[1].lower():  # Assuming the element symbol is in the third column (index 2)
            found = True
            table_data.append(header_row)  # Add header row to table data
            table_data.append(row)

    if found:
        # Create a new Tkinter window to display the table
        table_window = tk.Tk()
        table_window.title("Element Information Table")

        # Create a table format using labels for each row in the data
        for i, row_data in enumerate(table_data):
            for j, value in enumerate(row_data):
                label = tk.Label(table_window, text=value, borderwidth=1, relief="solid")
                label.grid(row=i, column=j)

        # Start the main loop of Tkinter for the table window
        table_window.mainloop()
    else:
        messagebox.showinfo("Element Information", f"{element} not found in the periodic table.")


# Create the main Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Call the function to search for an element in the CSV file
search_element()