def test_get_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in body
    assert isinstance(body[expected_activity]["participants"], list)


def test_signup_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body["message"] == f"Signed up {email} for {activity_name}"
    assert email in client.get("/activities").json()[activity_name]["participants"]


def test_signup_duplicate(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert body["detail"] == "Student already signed up for this activity"


def test_unregister_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    email = "nobody@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    body = response.json()

    # Assert
    assert response.status_code == 404
    assert body["detail"] == "Student not signed up for this activity"
