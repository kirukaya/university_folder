import requests

put_info_headers = {
    "auth_key": "a3236e05d5f93d97616559ea446e7960bff6a24596c2a42d2b692bc1",
    "pet_id": "f158c022-8c2e-49b1-81fc-1840534cd041"
}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "f158c022-8c2e-49b1-81fc-1840534cd041"


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))