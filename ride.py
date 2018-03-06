from math import fabs
from point import Point


class Ride(object):
    def __init__(self, idx, ride_string):
        self.idx = idx
        split_string = ride_string.split(' ')
        self.start_point = Point(int(split_string[0]), int(split_string[1]))
        self.end_point = Point(int(split_string[2]), int(split_string[3]))
        self.earliest_start = int(split_string[4])
        self.latest_finish = int(split_string[5])
        self.length = fabs(self.start_point.x - self.end_point.x) + fabs(self.start_point.y - self.end_point.y)

    def __str__(self) -> str:
        return str(self.idx) + ' ' + str(self.length)
