import time
import threading


class SeatbeltSystem:
    def __init__(self):
        self.seatbelt_fastened = False
        self.light_color = "green"  # 'red' for not fastened, 'green' for fastened
        self.sound_alarm = False
        self.blinking = False

    def fasten_seatbelt(self):  #Define the conditions when the seatbelt is fastened
        self.seatbelt_fastened = True
        self.update_alerts()

    def unfasten_seatbelt(self): #Define the conditions when the seatbelt is unfastened
        self.seatbelt_fastened = False
        self.update_alerts()

    def update_alerts(self):  #Define the states of the alerts
        if self.seatbelt_fastened:
            self.light_color = "green"
            self.sound_alarm = False
            self.stop_blinking()
        else:
            self.light_color = "red"
            self.start_blinking()

    def start_blinking(self): #Define the states of the alarm when the seatbelt is unfastened
        self.blinking = True
        threading.Thread(target=self.blink).start()

    def stop_blinking(self): #Define the states of the alarm when the seatbelt is fastened
        self.blinking = False

    def blink(self):
        while self.blinking:
            self.sound_alarm = True
            time.sleep(1)  # simulate the blink interval
            self.sound_alarm = False
            time.sleep(1)

    def is_light_indicator_green(self):
        return self.light_color == "green"

    def is_light_indicator_red(self):
        return self.light_color == "red"

    def is_sound_alarm_on(self):
        return self.sound_alarm


seatbelt_system = SeatbeltSystem()  #Heritage


def fasten_seatbelt():
    seatbelt_system.fasten_seatbelt()


def unfasten_seatbelt():
    seatbelt_system.unfasten_seatbelt()


def is_light_indicator_green():
    return seatbelt_system.is_light_indicator_green()


def is_light_indicator_red():
    return seatbelt_system.is_light_indicator_red()


def is_sound_alarm_on():
    return seatbelt_system.is_sound_alarm_on()
