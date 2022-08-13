#!/usr/bin/python3
import math

class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
    
    def __add__(self, other_time):
        minute_temp = 0
        hour_temp = 0
        new_second = self.seconds + other_time.seconds
        if new_second > 59:
            minute_temp = new_second / 60
            new_second = math.fmod(new_second, 60)

        new_minute = self.minutes + other_time.minutes + minute_temp
        if new_minute > 59:
            hour_temp = new_minute / 60
            new_minute = math.fmod(new_minute, 60)

        new_hour = self.hours + other_time.hours + hour_temp
        new_hour = math.fmod(new_hour, 24)

        new_time = Time(new_hour, new_minute, new_second)
        return(new_time)

def main():
    time1 = Time(2, 34, 11)
    print(time1 + Time(24, 26, 50))

main() 
