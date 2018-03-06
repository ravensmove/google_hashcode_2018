from point import Point
import utils


class Vehicle(object):
    def __init__(self):
        self.rides = []
        self.ride_distance = 0

    def get_total_rides_length(self):
        curr_point = Point(0, 0)
        total_dist = 0
        for ride in self.rides:
            total_dist += utils.point_dist(curr_point, ride.start_point)
            total_dist += ride.length
            curr_point = ride.end_point
        return total_dist

    def add_ride(self, ride):
        self.rides.append(ride)
        last_pos = self.get_last_position()
        self.ride_distance += utils.point_dist(last_pos, ride.start_point) + ride.length

    def get_last_position(self):
        if len(self.rides) > 0:
            return self.rides[-1].end_point
        else:
            return Point(0, 0)
