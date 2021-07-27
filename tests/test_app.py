def test_app_is_created(app):
    """Testa se o app foi criado corretamente"""
    assert app.name == "myapp.app"


def test_config_is_loaded(config):
    """config vem do pytest-flask"""
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    """Se esse teste passar o servidor iniciou legal"""
    assert client.get("/url_que_nao_existe").status_code == 404
