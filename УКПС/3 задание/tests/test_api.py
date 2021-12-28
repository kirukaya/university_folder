import pytest
import requests

# ПАРАМЕТРЫ

# POST PET SIMPLE
post_simple_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "name": "Mikki mouse",
    "animal_type": "mouse",
    "age": '12'
}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"

# API KEY
get_key_headers = {
    "email": "only1exit@gmail.com",
    "password": "razeme123"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"

# PETS LIST
get_headers_my_pets = {
    "auth_key ": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

# NEW PET
post_new_pet_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "name": "Abby",
    "animal_type": "cat",
    "age": '7',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"

# SET PHOTO
post_set_photo_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "pet_id": "cd804c24-3138-4fee-98b9-6dc52697b992"
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "cd804c24-3138-4fee-98b9-6dc52697b992"

# DELETE
delete_pet_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "pet_id": "4a16676c-716d-4d4b-9a19-af3fa1d2cd02"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "4a16676c-716d-4d4b-9a19-af3fa1d2cd02"

# PUT INFO
put_info_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "pet_id": "f158c022-8c2e-49b1-81fc-1840534cd041"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "f158c022-8c2e-49b1-81fc-1840534cd041"


# ФИКСТУРЫ
@pytest.fixture
def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('cat.jpeg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpeg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_pet_info():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


# ТЕСТЫ
@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # post_simple_pet
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),

                             # post_new_pet
                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),

                             # post_set_photo
                             pytest.param(set_photo_POST_link, post_set_photo_params, post_set_photo_headers, True,
                                          marks=pytest.mark.xfail),

                         ]
                         )
def test_post(link, params, header, expected_result):
    response = requests.post(link,
                             params=params,
                             headers=header
                             )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),

                             # get_my_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )
def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_pet_info):
    assert put_pet_info == True
