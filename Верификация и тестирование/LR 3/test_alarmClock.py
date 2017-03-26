from unittest import TestCase
from AlarmClock import *


class TestTime(TestCase):
    def test_set_hour(self):
        time = Time()
        self.assertTrue(time.set_hour(23))

    def test_set_minutes(self):
        time = Time()
        self.assertTrue(time.set_minutes(23))


class TestAlarmClock(TestCase):
    def test_set_alarm(self):
        alarm_clock = AlarmClock()
        self.assertTrue(alarm_clock.set_alarm("melody.mp3", 23, 23))


class TestMelody(TestCase):
    def test_set_melody(self):
        melody = Melody()
        self.assertTrue(melody.set_melody('melody.mp3'))

