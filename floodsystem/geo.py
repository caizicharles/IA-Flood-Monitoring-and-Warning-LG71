# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: M IT
"""This module contains a collection of functions related to
geographical data.

"""

"""Task 1B"""

from .utils import sorted_by_key
from haversine import haversine, Unit

def stations_by_distance(stations, p):

    name_n_dis = []
    s_name = []
    s_dis = []

    for location in stations:
        s_name.append(location.name)
        s_dis.append(haversine(location.coord, p))

    for i in range(len((s_name))):
        name_n_dis.append((s_name[i], s_dis[i]))

    return sorted_by_key(name_n_dis, 1)
    

"""------------------------------------------"""

"""Task 1C"""


"""------------------------------------------"""


"""Task 1D"""

def rivers_with_station(stations):

    return


def stations_by_river(stations):
    
    s_name = []
    s_dict = {}
    
    for location in stations:
        s_name.append(location.name)
    
    for items in range(len(s_name)):
        s_dict.update({str(s_name[items]):stations[items]})
        
    return s_dict

"""------------------------------------------"""

"""Task 1E"""


"""------------------------------------------"""