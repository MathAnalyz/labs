import os
import datetime
import time


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

    def get_name_melody(self):
        return self._path_to_melody


class AlarmClock:
    def __init__(self):
        self.alarms = dict()

    def set_alarm(self, name_melody, hour, minutes, reset=False):
        time_c = Time()
        melody = Melody()
        result = time_c.set_hour(hour) \
                 and time_c.set_minutes(minutes) \
                 and melody.set_melody(name_melody)
        if self.is_exist(time_c):
            print('На данное время уже установлен будильник.')
            if not reset:
                print('Он не был переустановлен.')
                return False
        if result:
            self.alarms[time_c.get_time()] = melody
            if reset:
                print('Он был переустановлен.')
        return result

    def is_exist(self, time):
        if self.alarms.get(time.get_time()) is None:
            return False
        return True

    def play_melody(self, time):
        melody = self.alarms.get(time.get_time())
        print('Звучит аудиозапись - ' + melody.get_name_melody() +
              '. Время - ' + str(time.get_time()[0]) + ':' + str(time.get_time()[1]) + '.')

    def run_alarm(self):
        time_now = datetime.datetime.now()
        shift = 60 - time_now.second
        time.sleep(shift - 1)
        while True:
            time_now = datetime.datetime.now()
            time_c = Time()
            time_c.set_hour(time_now.hour)
            time_c.set_minutes(time_now.minute)
            if self.is_exist(time_c):
                self.play_melody(time_c)
                break
            shift = 60 - time_now.second
            time.sleep(shift - 1)
