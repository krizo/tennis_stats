import requests

from client.credentials import Credentials


class ApiClient:
    base_url = "https://api.sportradar.com/tennis"
    access_level = "trial"
    api_version = "v3"
    language_code = 'en'
    _client = None
    _api_key = None

    @classmethod
    def get_api_token(cls):
        if not cls._api_key:
            cls._api_key = Credentials.api_token
        return cls._api_key

    @classmethod
    def _get(cls, endpoint: str, params: dict = None, request_type: str = 'json'):
        base_url = f"{cls.base_url}/{cls.access_level}/{cls.api_version}/{cls.language_code}"
        url = f"{base_url}/{endpoint}.{request_type}/"
        auth = {"api_key": f"{cls.get_api_token()}"}
        params = params or {}
        response = requests.get(url=url, params={**auth, **params})
        assert response.status_code == requests.status_codes.codes.ok, \
            f"Request failed with code. {response.status_code}. Reason: {response.text}"
        return response.content
