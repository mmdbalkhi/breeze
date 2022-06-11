import unittest

import pytest
from breeze import Config
from breeze import GithubOAuth2 as Github

if not (Config.GITHUB_CLIENT_ID or Config.GITHUB_CLIENT_SECRET):  # pragma: no cover
    pytest.skip("GithubOAuth2 Configs are not set", allow_module_level=True)


class GithubOAuth2Test(unittest.TestCase):
    gh = Github()

    def test_create_authorization_data(self):
        assert isinstance(self.gh.create_authorization_data(), tuple)
        assert len(self.gh.create_authorization_data()) == 2

    # other method in GithubOAuth2 can't be tested because it's need to Auth user to get token
