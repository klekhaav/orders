from .models import *


def get_cubic_weight(length, width, height, weight):
    return length * width * height * weight / 100


def get_cubes(length, width, height):
    return length * width * height / 100


def get_price_per_weight(length, width, height, weight, cubes, carrier, zone_from, zone_t0):
    cl_cubes = get_cubes(length, width, height)
    cw = get_cubic_weight(length, width, height, weight)
    if cubes >= cl_cubes:
        return "Good"

    else:
        return "Sorry you order no Carrier can't trasport so many cubes"
