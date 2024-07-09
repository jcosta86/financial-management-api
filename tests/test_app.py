from http import HTTPStatus


def test_health_check_should_return_ok_and_hello_world(client):
    response = client.get('/health-check')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'hendrix',
            'email': 'hendrix@example.com',
            'password': 'string',
            'name': 'string',
            'last_name': 'string',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'hendrix',
        'email': 'hendrix@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'hendrix',
                'email': 'hendrix@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'buba_gump',
            'email': 'buba_gump@example.com',
            'password': 'mynewpassword',
            'name': 'buba',
            'last_name': 'gump',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'buba_gump',
        'email': 'buba_gump@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
