from launches import get_count_per_year, launches_per_year
import collections
import matplotlib.pyplot as plt


def export_stats_to_csv(csv_file):
    """
    Function responsible for export years stats of SpaceX success/failure launches. Data is saved in CSV file.
    :param csv_file: Name of CSV file. Extension (.csv) need to be included as well.
    By default saved in current project folder; can be created anywhere if absolute path provided.
    :return: CSV file with data.
    """
    csv_columns = ['Year', 'Count of successes', 'Count of failures']
    success_count_per_year, failure_count_per_year = get_count_per_year()

    with open(csv_file, 'w') as file:
        file.write('{},{},{}\n'.format(csv_columns[0], csv_columns[1], csv_columns[2]))  # write headers
        for key in success_count_per_year.keys():
            file.write('{},{},{}\n'.format(key, success_count_per_year[key], failure_count_per_year[key]))


def export_data_to_graph():
    """
    Function responsible for creating a bar chart with stats of SpaceX success/failure launches.
    :return: Matplot figure.
    """
    success_count_per_year, failure_count_per_year = get_count_per_year()
    x1, y1 = zip(*[(key, value) for (key, value) in success_count_per_year.items()])
    x2, y2 = zip(*[(key, value) for (key, value) in failure_count_per_year.items()])

    plt.bar(x1, y1, color='green', label='Success')
    plt.bar(x1, y2, color='red', label='Failure')
    plt.grid(color='black', linestyle='--', linewidth=1, axis='y')
    plt.title('Successful and failed SpaceX launches per years')
    plt.xlabel('Years')
    plt.ylabel('Counts')
    plt.legend(loc='upper left')
    plt.show()


def reorganize_flights(input_dict, output_dict, value):
    """
    Function used to reogranize output from launches_per_year function. Empty lists are omitted.
    Function is assigning given value (status - Success or Failure) to a flight number, base of input data.
    :param input_dict: Input data - it is result for launches_per_year function from launches.py file.
    Example: ({2006: [], 2007: [], 2008: [4], 2009: [5], 2010: [6, 7])
    :param output_dict: Name of output dictionary. Example of format:
    {4: 'Success', 5: 'Success', 6: 'Success', 7: 'Success'}
    :param value: Name of value (status) assigned to a flight number.
    :return: Dictionary defined under input_dict is populated with reorganized data.
    """
    for flight_number in input_dict.values():
        if len(flight_number) is False:
            pass
        else:
            for i in flight_number:
                output_dict[i] = value


def export_stats_per_flight_numbers_to_csv(csv_file):
    """
    Function is exporting stats per flight number to CSV file. Each flight number got it own status: Success or Failure.
    :param csv_file: Name of CSV file. Extension (.csv) need to be included as well.
    :return: CSV file with data.
    """
    csv_headers = ['Flight number', 'Status']
    success, failures = launches_per_year()

    flights = {}

    reorganize_flights(success, flights, 'Success')
    reorganize_flights(failures, flights, 'Failure')

    ordered_flights = collections.OrderedDict(sorted(flights.items()))

    with open(csv_file, 'w') as file:
        file.write('{},{}\n'.format(
            csv_headers[0],
            csv_headers[1]))

        for key, value in ordered_flights.items():
            file.write('{},{}\n'.format(
                key,
                value
            ))
