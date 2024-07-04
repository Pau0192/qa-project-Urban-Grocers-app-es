import configuration
import data
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


print(data.user_body)
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)


response = post_new_client_kit(data.kit_body, data.headers)
print(data.kit_body)
print(response.status_code)

def get_kit_model_table():
    return requests.get(configuration.URL_SERVICE + configuration.KIT_MODEL_TABLE_PATH)

response = get_kit_model_table()
print(response.status_code)
