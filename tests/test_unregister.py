def test_unregister_success(client):
    response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }


def test_unregister_returns_404_when_student_not_signed_up(client):
    response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "not_enrolled@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}
