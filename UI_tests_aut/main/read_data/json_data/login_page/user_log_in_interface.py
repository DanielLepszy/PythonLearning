import json
from enum import Enum


class UserType(Enum):
    STANDARD = "standard"
    LOCKED = "locked"
    NONEXISTENT = "nonexistent"
    PROBLEMATIC = "problematic"
    PERFORMANCE = "performance"

    @classmethod
    def users_able_to_log_in(cls):
        users = list(map(lambda c: c.value, cls))
        return users.remove(cls.NONEXISTENT.value)


class UserLogInReaderInterface:
    __file_path__ = 'C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/UI_tests_aut/main/read_data/json_data/login_page/log_in_data.json'

    @classmethod
    def read_json_file(cls, path=__file_path__):
        with open(path) as f:
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
    def get_user_type_node(cls, file_path=__file_path__) -> dict:
        json_file = cls.read_json_file(path=file_path)
        user_type_node = json_file['credentials']['user_type']

        return user_type_node

    @classmethod
    def select_user_credentials(cls, user_type: UserType, file_path=__file_path__):
        json_file = cls.read_json_file(path=file_path)
        user_type_node = json_file['credentials']['user_type']
        credentials_node = cls.select_user_type_node(user_type, user_type_node)

        return credentials_node

    @classmethod
    def get_username(cls, user_type: UserType, file_path=__file_path__) -> str:
        credentials = cls.select_user_credentials(user_type, file_path=file_path)

        return credentials.get('username')

    @classmethod
    def get_password(cls, user_type: UserType, file_path=__file_path__) -> str:
        credentials = cls.select_user_credentials(user_type, file_path=file_path)

        return credentials.get('password')

    @classmethod
    def get_only_proper_users_credentials(cls, file_path=__file_path__):
        """
        Takes credentials of all users which are able to log in to app
        """
        user_type_node: dict = cls.get_user_type_node(file_path=file_path)
        users: list = list(map(lambda c: c.value, UserType))
        users.remove(UserType.NONEXISTENT.value)
        users.remove(UserType.LOCKED.value)

        users_credentials = []
        for user in users:
            user_credential = user_type_node[user]
            username = user_credential.get('username')
            password = user_credential.get('password')
            users_credentials.append((username, password))

        return users_credentials

    @classmethod
    def get_user_with_no_access(cls, file_path=__file_path__):
        """
            Takes users which are not able to log in to app
        """
        user_type_node: dict = cls.get_user_type_node(file_path=file_path)
        users: list = list(map(lambda c: c.value, UserType))
        users.remove(UserType.PERFORMANCE.value)
        users.remove(UserType.STANDARD.value)
        users.remove(UserType.PROBLEMATIC.value)

        users_with_no_access = []
        for user in users:
            users_with_no_access.append(user_type_node[user])

        return users_with_no_access
