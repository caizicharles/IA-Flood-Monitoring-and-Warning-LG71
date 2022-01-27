# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):

    name_n_dis = []
    s_name = []
    s_dis = []

    for location in stations:
        if location.name is True:
            s_name.append(location.name)
        
        elif location.coord is True:
            s_dis.append(haversine(location.coord, p))

    for i in s_name, s_dis:
        name_n_dis.append(tuple(s_name[i], s_dis[i]))

    return sorted_by_key(name_n_dis, 1)