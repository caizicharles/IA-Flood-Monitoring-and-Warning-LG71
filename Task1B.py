from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def show():

    show_list0 = []
    show_list = []
    show_list0.append(stations_by_distance(build_station_list(), (1, 2)))

    for j in range(0, 10):
        show_list.append(show_list0[j])

    return show_list

print(show())
