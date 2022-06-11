import pytest
from breeze import Config
from breeze import GithubOAuth2 as Github


gh = Github()

if not (Config.GITHUB_CLIENT_ID or Config.GITHUB_CLIENT_SECRET):  # pragma: no cover
    pytest.skip("GithubOAuth2 Configs are not set", allow_module_level=True)


# other method in GithubOAuth2 can't be tested because it's need to Auth user to get token
def test_create_authorization_data():  # pragma: no cover
    assert isinstance(gh.create_authorization_data(), tuple)
    assert len(gh.create_authorization_data()) == 2
