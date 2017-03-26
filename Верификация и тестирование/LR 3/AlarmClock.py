import os


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
        self._path_to_melody = ''
        self.__default_path_to_melody = 'melody.txt'

    def set_melody(self, path):
        if not isinstance(path, str):
            return False
        self._path_to_melody = path
        if self.is_exist():
            return True
        else:
            self._path_to_melody = ''
        return False

    def is_exist(self, default=False):
        if not default:
            return os.path.isfile(self._path_to_melody)
        return os.path.isfile(self.__default_path_to_melody)


class AlarmClock:
    def __init__(self):
        self.alarms = dict()

    def set_alarm(self, name_melody, hour, minutes):
        time = Time()
        melody = Melody()
        result = time.set_hour(hour) \
                 and time.set_minutes(minutes) \
                 and melody.set_melody(name_melody)
        if result:
            self.alarms[time] = melody
        return result
