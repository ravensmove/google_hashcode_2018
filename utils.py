from math import fabs


def point_dist(point_a, point_b):
    return fabs(point_a.x - point_b.x) + fabs(point_a.y - point_b.y)
