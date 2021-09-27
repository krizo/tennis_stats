from client.competition import Competitions


def test_competitions_list():
    assert Competitions.get_competitions_list() is not None
