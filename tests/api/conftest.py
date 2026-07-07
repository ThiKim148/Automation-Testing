import pytest

from api.auth_client import AuthClient


@pytest.fixture(scope="class", autouse=True)
def clean_test_account(test_user):

    response = AuthClient.delete_user(
        test_user["email"],
        test_user["password"]
    )

    print("Cleanup:", response.text)

    yield