# test_hello_add.py
from app import app
from flask import json


def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_new_course():
    response = app.test_client().post(
        "/api/v1.0/courses/",
        data=json.dumps(
            {
                "name": "test name",
                "dbegin": "01.01.2021",
                "dend": "01.06.2021",
                "cntlections": 29,
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] == 1
    assert data["data"]["data"] == "ok"


def test_upd_course():
    response = app.test_client().put(
        "/api/v1.0/courses/3",
        data=json.dumps(
            {
                "name": "test name 2",
                "dbegin": "01.02.2021",
                "dend": "01.07.2021",
                "cntlections": 33,
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] == 1
    assert data["data"]["data"] == "ok"


def test_del_course():
    response = app.test_client().delete(
        "/api/v1.0/courses/2",
        data=json.dumps({}),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] == 1
    assert data["data"]["data"] == "ok"


def test_ret_courses():
    response = app.test_client().get(
        "/api/v1.0/courses/",
        data=json.dumps({}),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] > 1
    assert len(data["data"]["data"]) > 1


def test_ret_course():
    response = app.test_client().get(
        "/api/v1.0/courses/3",
        data=json.dumps({}),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] == 1
    assert len(data["data"]["data"][0]) == 5


def test_search_course():
    response = app.test_client().get(
        "/api/v1.0/courses/q",
        data=json.dumps({"q": "01.02.2021"}),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["data"]["rowcount"] >= 1
    assert len(data["data"]["data"]) >= 1
