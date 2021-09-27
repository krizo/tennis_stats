import yaml

from client.helpers import get_root_dir


class Credentials:
    _credentials_file = get_root_dir() + 'secrets.yml'
    _credentials = None

    def __init__(self):
        self._credentials = self._get_credentials()

    def _get_credentials(self) -> dict:
        if self._credentials is None:
            with open(self._credentials_file, 'r') as stream:
                self._credentials = yaml.safe_load(stream)
        return self._credentials

    @property
    def api_token(self) -> str:
        return self._get_credentials().get('api_token')
