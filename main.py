from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime

# Set the background color to blue (R, G, B, Alpha)
Window.clearcolor = (0, 0, 1, 1)  # Blue background


class DigitalClock(Label):
    def update_time(self, *args):
        # Get the current time
        self.text = datetime.now().strftime('%H:%M:%S')


class ClockApp(App):
    def build(self):
        # Create a Label widget with white text
        clock_label = DigitalClock()
        clock_label.color = (1, 1, 1, 1)  # Set text color to white
        clock_label.font_size = '72sp'  # Font size for readability

        # Schedule the update_time function to be called every second
        Clock.schedule_interval(clock_label.update_time, 1)

        return clock_label


if __name__ == '__main__':
    ClockApp().run()
