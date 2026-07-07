import pytest

from api.auth_client import AuthClient


@pytest.fixture(scope="class", autouse=True)
def clean_test_account(test_user):

    print("===== CLEANUP START =====")

    response = AuthClient.delete_user(
        test_user["email"],
        test_user["password"]
    )

    print("HTTP:", response.status_code)
    print("BODY:", response.text)

    yield