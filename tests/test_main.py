from http import HTTPStatus

from fastapi.testclient import TestClient

from todolist.main import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange(organizacao)
    response = client.get('/')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo'}
