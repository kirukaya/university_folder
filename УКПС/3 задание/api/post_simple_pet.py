import requests

post_simple_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "name": "Jessica",
    "animal_type": "dog",
    "age": '2'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))
