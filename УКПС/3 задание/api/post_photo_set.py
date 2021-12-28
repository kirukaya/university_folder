import requests

post_set_photo_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "pet_id": "4a16676c-716d-4d4b-9a19-af3fa1d2cd02"
}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "4a16676c-716d-4d4b-9a19-af3fa1d2cd02"


def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpeg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))