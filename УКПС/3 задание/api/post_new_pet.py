import requests

post_new_pet_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "name": "Abby",
    "animal_type": "cat",
    "age": '7',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('cat.jpeg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))