
"""Sprint 2 - User API testing with APIRequestContext.

Fixtures you can use (see conftest.py): api, test_user, auth_headers

Run: pytest tests/api/test_users_api.py -v
"""
import pytest


# ---------------------------------------------------------------- B2.4b errors
@pytest.mark.api
def test_users_register_empty_body_returns_422_with_field_errors(api):
    """Goal: server-side validation.
    Precondition: none.
    Expected: 422 and error lists for 'email' and 'password'."""
    response = api.post("/users/register", data={})
    assert response.status == 422, response.text()
    errors = response.json()
    assert "email" in errors and "password" in errors, errors


# ---------------------------------------------------------------- B2.5a token
@pytest.mark.api
def test_users_me_with_token_returns_own_profile(api, auth_headers, test_user):
    """Goal: bearer token grants access.
    Precondition: user registered by the fixture.
    Expected: 200 and the same email."""
    response = api.get("/users/me", headers=auth_headers)
    assert response.status == 200, response.text()
    assert response.json()["email"] == test_user["email"]
