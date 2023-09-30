from django.urls import reverse


def test_ping(client):
    response = client.get(reverse('ping'))
    assert response.status_code == 200
    data = response.content.decode()
    assert 'students' in data
