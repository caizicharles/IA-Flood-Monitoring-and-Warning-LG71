from floodsystem.stationdata import build_station_list

print('-----------------------')

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    rivers = set()
    for station in stations:
        rivers.add(station.river)

    river = sorted(rivers)
    return river


print(run())