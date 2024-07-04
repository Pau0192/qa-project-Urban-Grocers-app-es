
import data
import sender_stand_request
import pytest


def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(data.headers,data.kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == data.kit_body["name"]

    kit_model_table_response = sender_stand_request.get_kit_model_table()
    str_kit = data.kit_body["name"] + ",,," + sender_stand_request.get_user_body["auth_token"]
    assert kit_model_table_response.text.count(str_kit) == 1

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos" \
                                         "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
#Prueba 1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")

#Prueba 2
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3
def test_create_kit_smallest_parameter_name_get_error_response():
    negative_assert_code_400('A')

def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

def test_create_kt_has_number_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_empty_name_get_error_response():
    kit_body = data.kit_body('')
    negative_assert_code_400(kit_body)

def test_create_kit_different_parameter_in_name_get_error_response():
    negative_assert_code_400(123)


