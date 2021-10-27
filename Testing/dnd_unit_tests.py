import dnd_app
import pytest

CLASS_API = "https://www.dnd5eapi.co/api/classes/"


@pytest.fixture()
def test_generate_response_failure():
    return dnd_app.generate_response("Wizard")


def test_get_status_code_failure(test_generate_response_failure):
    assert dnd_app.get_status_code(test_generate_response_failure) != 200


@pytest.fixture()
def test_generate_response_success():
    return dnd_app.generate_response("wizard")


def test_get_status_code_success(test_generate_response_success):
    assert dnd_app.get_status_code(test_generate_response_success) == 200


def test_get_hit_die(test_generate_response_success):
    assert dnd_app.get_hit_die(test_generate_response_success) == 6


def test_get_saving_throw(test_generate_response_success):
    assert dnd_app.get_saving_throw(test_generate_response_success) is not None
    firstThrow = test_generate_response_success.json()["saving_throws"][0]["index"]
    secondThrow = test_generate_response_success.json()["saving_throws"][1]["index"]
    assert firstThrow + ", " + secondThrow == "int, wis"


def test_dnd_api_call():
    expected = "API call made to: " + CLASS_API + "wizard\nResponse for api call was: 200\nHit die is: 6\nSaving " \
                                                  "throws are: int, wis"
    actual = dnd_app.dnd_api_call("wizard")
    assert expected == actual

