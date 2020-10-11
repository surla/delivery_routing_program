class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def get_time(self):
        hour = self.hour
        minute = self.minute

        if minute <= 9:
            minute = str(minute).zfill(2)

        return str(hour) + ":" + str(minute)

    def update_time(self, minute_time):
        self.minute += minute_time

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.hour > 12:
            self.hour = 1

        return self.hour, self.minute
