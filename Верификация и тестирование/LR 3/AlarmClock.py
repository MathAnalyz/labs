class Time:
    def __init__(self):
        self.hour = 0
        self.minutes = 0

    def set_hour(self, hour):
        self.hour = hour
        return True

    def set_minutes(self, minutes):
        self.minutes = minutes
        return True


class Melody:
    def __init__(self):
        self.melody = ""
        self.default_melody = ""

    def set_melody(self, melody):
        self.melody = melody
        return True


class AlarmClock:
    def __init__(self):
        self.alarms = dict()

    def set_alarm(self, melody, hour, minutes):
        time = Time()
        melody = Melody()
        if (time.set_hour(hour)
            and time.set_minutes(minutes)
            and melody.set_melody(melody)):
            self.alarms[time] = melody
            return True
