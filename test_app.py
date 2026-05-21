from app import app


def test_index_gibt_ok_zurueck():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.get_json()["status"] == "ok"


def test_greet_ohne_namen_gruesst_welt():
    with app.test_client() as client:
        response = client.get("/greet")
        assert response.get_json()["greeting"] == "Hallo, Welt!"


def test_greet_mit_namen_gruesst_diesen():
    with app.test_client() as client:
        response = client.get("/greet?name=Anna")
        assert response.get_json()["greeting"] == "Hallo, Anna!"