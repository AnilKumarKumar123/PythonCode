import requests
from assertpy.assertpy import assert_that


def test_invalid_credential():
    data = {"username": "", "password": "JobPassword123!@#"}

    response = requests.post("https://qa-practical.qa.swimlane.io/api/user/login",
                             headers={
                                 "Content-Type": "application/x-www-form-urlencoded"
                             }, data=data
                             )
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(401)
    print(response_text)


def test_delete_record():
    response = requests.post("https://qa-practical.qa.swimlane.io/api/app/aaUiorxB5O4lm4Cye/record/aFH1puQ7gYHJJCrCS",
                             headers={
                                 "Content-Type": "application/x-www-form-urlencoded"
                             }
                             )
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(204)
    print(response_text)


def test_valid_credential():
    data = {"username": "anil.kakarla", "password": "JobPassword123!@#"}

    response = requests.post("https://qa-practical.qa.swimlane.io/api/user/login",
                             headers={
                                 "Content-Type": "application/x-www-form-urlencoded"
                             }, data=data
                             )
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)
    print(response_text)


def test_get_record():
    response = requests.post("https://qa-practical.qa.swimlane.io/api/workflow/aaUiorxB5O4lm4Cye",
                             headers={
                                 "Content-Type": "application/x-www-form-urlencoded"
                             }
                             )
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(200)
    print(response_text)


test_invalid_credential()
test_valid_credential()
test_delete_record()
test_get_record()
