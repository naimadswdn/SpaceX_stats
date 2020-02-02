import requests


def get_launches_json(query=None):
    """
    Function is sending HTTP request to SpaceX API with parameters (queries).
    Function should be used only by method launches.get_launches().
    :param query: Set of parameters, needed to filter data returned from SpaceX API.
    :return: List of data, already deserialized from JSON.
    """
    if query is None:
        query = {}
    url = 'https://api.spacexdata.com/v3/launches'
    res = requests.get(url, params=query)

    if not res.ok:
        res.raise_for_status()

    return res.json()


