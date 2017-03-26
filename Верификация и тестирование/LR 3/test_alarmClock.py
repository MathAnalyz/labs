from unittest import TestCase
from AlarmClock import *


class TestTime(TestCase):
    def test_set_hour(self):
        time = Time()
        self.assertTrue(time.set_hour(0))
        self.assertTrue(time.set_hour(23))
        self.assertFalse(time.set_hour(-1))
        self.assertFalse(time.set_hour(25))
        self.assertFalse(time.set_hour(12.12312))
        self.assertFalse(time.set_hour('q'))
        self.assertFalse(time.set_hour('fsdf'))
        self.assertFalse(time.set_hour(True))
        self.assertFalse(time.set_hour(False))

    def test_set_minutes(self):
        time = Time()
        self.assertTrue(time.set_minutes(0))
        self.assertTrue(time.set_minutes(59))
        self.assertFalse(time.set_minutes(-1))
        self.assertFalse(time.set_minutes(-61))
        self.assertFalse(time.set_minutes(12.12312))
        self.assertFalse(time.set_minutes('q'))
        self.assertFalse(time.set_minutes('fsdf'))
        self.assertFalse(time.set_minutes(True))
        self.assertFalse(time.set_minutes(False))


class TestMelody(TestCase):
    def test_set_melody(self):
        melody = Melody()
        self.assertTrue(melody.set_melody('melody.mp3'))
        self.assertFalse(melody.set_melody(123))
        self.assertFalse(melody.set_melody(3.43))
        self.assertFalse(melody.set_melody(True))
        self.assertFalse(melody.set_melody(False))


class TestAlarmClock(TestCase):
    def test_set_alarm(self):
        alarm_clock = AlarmClock()
        self.assertTrue(alarm_clock.set_alarm('melody.mp3', 23, 23))
        self.assertFalse(alarm_clock.set_alarm(12, 'd', 'dfdsf'))
        self.assertFalse(alarm_clock.set_alarm(True, 123, 23.1))



