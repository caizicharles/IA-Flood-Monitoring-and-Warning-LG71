from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def execute0():
    
    return

def execute1():

    sorted_keys = sorted(stations_by_river.keys())
    sorted_s_dict = {key:stations_by_river[key] for key in sorted_keys}

    return sorted_s_dict