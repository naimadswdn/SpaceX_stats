from api import get_launches_json
from datetime import datetime


def get_launches(**query):
    """
    Function is returning SpaceX data based on queries (dict). It allow to filter full set of returned data,
    to get only the one user is interested in.
    :param query: Dictionary with definition of queries, allowed by SpaceX API. Full list of strings:
    https://docs.spacexdata.com/?version=latest#5fc4c846-c373-43df-a10a-e9faf80a8b0a
    :return: List of data, filtered by queries.
    """
    return get_launches_json(query)


def get_list_of_years():
    """
    Function responsible for returning a list of years (int) since 2006 till now.
    :return: List of years - years are integers.
    """
    year_list = range(2006, int(datetime.today().year))  # first launches started at 2006
    return year_list


def split_launches(data):
    """
    Function is splitting input data (list) based on launch_success querystring from SpaceX API.
    :param data: Input data returned from SpaceX API (list).
    :return: Dictionary with two keys: success and failure. Each key contain flight_numbers of launches, according to
    launch_success flag.
    """
    success = []
    failure = []
    for launch_details in data:
        if launch_details['launch_success'] is True:
            success.append(launch_details['flight_number'])
        else:
            failure.append(launch_details['flight_number'])

    return {'success': success, 'failure': failure}


def launches_per_year():
    """
    Function is dividing split_launches output data based on launch year.
    :return: List with two dictionaries: one with successful launches and second one with failed ones.
    Launch years are represented as keys. Values are lists of flight numbers.
    """
    success_in_year = {}
    failure_in_year = {}

    for year in get_list_of_years():
        raw_data = get_launches(launch_year=year)
        result = split_launches(raw_data)
        success_in_year[year] = result['success']
        failure_in_year[year] = result['failure']

    return success_in_year, failure_in_year


def get_count_per_year():
    """
    Function is preparing an overview of success/failed launches for all years since 2006.
    Overview in this case, is a sum of success/failed launches per yer.
    :return: List with two dictionaries: one with count of successful launches and second one with count of failed ones.
    """
    success_in_year, failure_in_year = launches_per_year()
    success_count_per_year = {}
    failure_count_per_year = {}

    for year, flights in success_in_year.items():
        success_count_per_year[year] = len(flights)

    for year, flights in failure_in_year.items():
        failure_count_per_year[year] = len(flights)

    return success_count_per_year, failure_count_per_year
