import json
from enum import Enum


class UserType(Enum):
    STANDARD = "standard"
    LOCKED = "locked"
    PROBLEMATIC = "problematic"
    PERFORMANCE = "performance"
    WRONG = "wrong"


class ReaderJSON:
    __file_path__ = 'UI_tests_aut/test/data/login_page_test_data/credentials_data.json'

    @classmethod
    def read_json_file(cls):
        with open('data/file_for_test.json') as f:
            json_file = json.load(f)
        return json_file

    @classmethod
    def select_user_type_node(self, user_type: UserType, data: dict) -> dict:
        if user_type.STANDARD:
            return data['standard']
        elif user_type.LOCKED:
            return data['locked']
        elif user_type.PROBLEMATIC:
            return data['problematic']
        elif user_type.PERFORMANCE:
            return data['performance']
        elif user_type.WRONG:
            return data['wrong']

    @classmethod
    def select_user_credentials(cls, user_type: UserType):
        json_file = cls.read_json_file()
        user_type_node = json_file['credentials']['user_type']

        credentials = cls.select_user_type_node(user_type, user_type_node)
        return credentials
        pass
#     # TODO read json file
#     def read_json_file(self):
#
#     # TODO get_user_credential
#     def get_user_credential(self, user_type):
#
# # TODO
