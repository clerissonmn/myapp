def test_index(client):
    assert client.get("/").status_code == 200


def test_about(client):
    assert client.get("/about").status_code == 200


def test_work(client):
    assert client.get("/work").status_code == 200


def test_work_single(client):
    assert client.get("/work-single").status_code == 200


def test_pricing(client):
    assert client.get("/pricing").status_code == 200


def test_contact(client):
    assert client.get("/contact").status_code == 200
