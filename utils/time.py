# Time class to track time for package deliveries
class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    # O(1)
    # Method returns time as string for package delivery
    def get_time(self):
        hour = self.hour
        minute = self.minute

        if minute <= 9:
            minute = str(minute).zfill(2)

        return str(hour) + ":" + str(minute)

    # O(1)
    # Methods updates time for trucks during delivery
    def update_time(self, minute_time):
        self.minute += minute_time

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.hour > 12:
            self.hour = 1

        return self.hour, self.minute
