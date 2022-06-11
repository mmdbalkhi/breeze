from typing import Tuple

from authlib.integrations.requests_client import OAuth2Session
from breeze.config import Config


class GithubOAuth2:
    """OAuth2 class"""

    def __init__(self):
        self.github = OAuth2Session(
            Config.GITHUB_CLIENT_ID,
            Config.GITHUB_CLIENT_SECRET,
            scope=Config.GITHUB_SCOOP,
        )
        self.authorization_endpoint = "https://github.com/login/oauth/authorize"
        self.token_endpoint = "https://github.com/login/oauth/access_token"

    def create_authorization_data(self) -> Tuple[str, str]:
        """Create authorization datas
        :return: `Tuple[str, str]`: uri, state
        """
        return self.github.create_authorization_url(self.authorization_endpoint)

    def fetch_token(self, authorization_response: str) -> dict:
        """Fetch token

        :param code: `str`: code
        :return: `dict`: token
        """
        return self.github.fetch_token(
            self.token_endpoint, authorization_response=authorization_response
        )

    def get_user_info(self, token: dict) -> dict:
        """Get user info

        :param token: `dict`: token
        :return: `dict`: user info
        """
        client = OAuth2Session(
            Config.GITHUB_CLIENT_ID, Config.GITHUB_CLIENT_SECRET, token=token
        )
        return client.get("https://api.github.com/user").json()

    def get_user_by_code(self, code: str) -> dict:
        """Get user by code

        :param code: `str`: code
        :return: `dict`: user info
        """
        token = self.fetch_token(code)
        return self.get_user_info(token)
