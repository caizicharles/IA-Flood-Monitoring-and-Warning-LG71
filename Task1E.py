from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in range(50):
        print(stations[station])


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
