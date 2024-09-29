"""Final Project.py"""
import tkinter as tk
from tkinter import messagebox

# Main application class
class JavaDLiteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Java D-Lite!")
        
        # Initialize screens
        self.home_screen()

    def home_screen(self):
        # Clear the current frame
        self.clear_frame()

        # Home screen layout
        welcome_label = tk.Label(self.master, text="Welcome to Java D-Lite!", font=("Arial", 24))
        welcome_label.pack(pady=20)

        order_button = tk.Button(self.master, text="Order Coffee", command=self.customization_screen)
        order_button.pack(pady=10)

        past_orders_button = tk.Button(self.master, text="View Past Orders", command=self.view_past_orders)
        past_orders_button.pack(pady=10)

        settings_button = tk.Button(self.master, text="Personal Settings", command=self.settings_screen)
        settings_button.pack(pady=10)

    def customization_screen(self):
        self.clear_frame()

        # Customization screen layout
        tk.Label(self.master, text="Customize Your Coffee Order", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.master, text="Select Coffee Type:").pack()
        self.coffee_type = tk.StringVar()
        tk.OptionMenu(self.master, self.coffee_type, "Espresso", "Latte", "Cappuccino").pack()

        tk.Label(self.master, text="Select Size:").pack()
        self.size = tk.StringVar()
        tk.OptionMenu(self.master, self.size, "Small", "Medium", "Large").pack()

        tk.Label(self.master, text="Add-Ons:").pack()
        self.add_ons = tk.StringVar(value="None")
        tk.Checkbutton(self.master, text="Milk", variable=self.add_ons, onvalue="Milk").pack()
        tk.Checkbutton(self.master, text="Syrup", variable=self.add_ons, onvalue="Syrup").pack()

        confirm_button = tk.Button(self.master, text="Confirm Order", command=self.order_summary)
        confirm_button.pack(pady=20)

        back_button = tk.Button(self.master, text="Back to Home", command=self.home_screen)
        back_button.pack(pady=10)

    def order_summary(self):
        order_details = f"Coffee Type: {self.coffee_type.get()}\nSize: {self.size.get()}\nAdd-Ons: {self.add_ons.get()}"
        messagebox.showinfo("Order Summary", order_details)
        # You could implement additional functionality to save the order here

    def view_past_orders(self):
        self.clear_frame()
        tk.Label(self.master, text="Past Orders (Not Implemented)", font=("Arial", 24)).pack(pady=20)
        back_button = tk.Button(self.master, text="Back to Home", command=self.home_screen)
        back_button.pack(pady=10)

    def settings_screen(self):
        self.clear_frame()
        tk.Label(self.master, text="Personal Settings (Not Implemented)", font=("Arial", 24)).pack(pady=20)
        back_button = tk.Button(self.master, text="Back to Home", command=self.home_screen)
        back_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JavaDLiteApp(root)
    root.mainloop()
