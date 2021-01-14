import json
from enum import Enum

class UserType(Enum):
    STANDARD = "standard"
    LOCKED = "locked"
    PROBLEMATIC = "problematic"
    PERFORMANCE = "performance"
    WRONG = "wrong"


class UserCredentialsReaderInterface:
    __file_path__ = 'UI_tests_aut/test/data/login_page/credentials_data.json'

    @classmethod
    def read_json_file(cls):
        with open('data/file_for_test.json') as f:
            json_file = json.load(f)
        return json_file

    @classmethod
    def select_user_type_node(self, user_type: UserType, data: dict) -> dict:
        if user_type == user_type.STANDARD:
            return data['standard']
        elif user_type == user_type.LOCKED:
            return data['locked']
        elif user_type == user_type.PROBLEMATIC:
            return data['problematic']
        elif user_type == user_type.PERFORMANCE:
            return data['performance']
        elif user_type == user_type.WRONG:
            return data['wrong']

    @classmethod
    def select_user_credentials(cls, user_type: UserType):
        json_file = cls.read_json_file()
        user_type_node = json_file['credentials']['user_type']
        credentials_node = cls.select_user_type_node(user_type, user_type_node)

        return credentials_node

    @classmethod
    def get_username(cls, user_type: UserType) -> str:
        credentials = cls.select_user_credentials(user_type)

        return credentials.get('username')

    @classmethod
    def get_password(cls, user_type: UserType) -> str:
        credentials = cls.select_user_credentials(user_type)

        return credentials.get('password')
