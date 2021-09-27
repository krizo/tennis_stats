from client.api_client import ApiClient


class Competitions(ApiClient):
    _api_client = None
    endpoint = 'competitions'

    @classmethod
    def get_competitions_list(cls, params=None):
        request = cls._get(endpoint='competitions', params=params)
