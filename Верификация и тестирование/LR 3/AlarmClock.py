class Time:
    def __init__(self):
        self.hour = 0
        self.minutes = 0

    def set_hour(self, hour):
        if not isinstance(hour, int) or isinstance(hour, bool):
            return False
        elif (hour >= 25) or (hour <= -1):
            return False
        self.hour = 0 if hour == 24 else hour
        return True

    def set_minutes(self, minutes):
        if not isinstance(minutes, int) or isinstance(minutes, bool):
            return False
        elif (minutes >= 61) or (minutes <= -1):
            return False
        self.minutes = 0 if minutes == 60 else minutes
        return True

    def get_time(self):
        return self.hour, self.minutes


class Melody:
    def __init__(self):
        self.melody = ''
        self.default_melody = ''

    def set_melody(self, melody):
        if not isinstance(melody, str):
            return False
        self.melody = melody
        return True


class AlarmClock:
    def __init__(self):
        self.alarms = dict()

    def set_alarm(self, name_melody, hour, minutes):
        time = Time()
        melody = Melody()
        if (time.set_hour(hour) and time.set_minutes(minutes)) and melody.set_melody(name_melody):
            self.alarms[time] = melody
            return True
        return False
