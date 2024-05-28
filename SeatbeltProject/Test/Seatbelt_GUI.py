import tkinter as tk
from tkinter import messagebox
import Test_seatbelt as seatbelt

class SeatBeltGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Seat Belt System")

        self.status_label = tk.Label(root, text="Light Status: Green")
        self.status_label.pack(pady=10)

        self.fasten_button = tk.Button(root, text="Fasten Seat Belt", command=self.fasten_seatbelt)
        self.fasten_button.pack(pady=5)

        self.unfasten_button = tk.Button(root, text="Unfasten Seat Belt", command=self.unfasten_seatbelt)
        self.unfasten_button.pack(pady=5)

        self.check_status_button = tk.Button(root, text="Check Status", command=self.check_status)
        self.check_status_button.pack(pady=5)

    def fasten_seatbelt(self):
        seatbelt.fasten_seatbelt()
        self.update_status()

    def unfasten_seatbelt(self):
        seatbelt.unfasten_seatbelt()
        self.update_status()

    def check_status(self):
        status_message = (
            f"Seat Belt Fastened: {seatbelt.seatbelt_system.seatbelt_fastened}\n"
            f"Light Status: {seatbelt.seatbelt_system.light_color}\n"
            f"Sound Alarm: {seatbelt.seatbelt_system.sound_alarm}"
        )
        messagebox.showinfo("Seat Belt Status", status_message)

    def update_status(self):
        light_color = "Green" if seatbelt.is_light_indicator_green() else "Red"
        self.status_label.config(text=f"Light Status: {light_color}")
        if seatbelt.is_sound_alarm_on():
            self.root.bell()  # Simulate sound alarm by making a sound

if __name__ == "__main__":
    root = tk.Tk()
    app = SeatBeltGUI(root)
    root.mainloop()
