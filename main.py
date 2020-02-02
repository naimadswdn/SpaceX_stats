from export import export_stats_to_csv, export_stats_per_flight_numbers_to_csv, export_data_to_graph


def main():
    export_stats_per_flight_numbers_to_csv('SpaceX_stats_per_flight_number.csv')
    export_stats_to_csv('SpaceX_stats.csv')
    export_data_to_graph()


if __name__ == "__main__":
    main()
