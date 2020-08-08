from django.urls import reverse
import pytest

@pytest.fixture
def response(client):
    return client.get(reverse('account:login'))

def test_login_status_code(response):
    assert response.status_code == 200
