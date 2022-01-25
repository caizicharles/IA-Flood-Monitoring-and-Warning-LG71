#geo

import haversine

def stations_by_distance(stations, p):

    s_d = []

    s_d.append(haversine(stations, p))