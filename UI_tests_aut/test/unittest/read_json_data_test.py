import pytest
import json

from read_data.json_data.login_page.json_reader import UserCredentialsReaderInterface, UserType


@pytest.mark.unittestJSON
class TestJSONReaderInterface:
    __file_path__ = 'data/credentails_backup_data.json'

    def test_read_json_file(self):
        with open(self.__file_path__) as f:
            data = json.load(f)

        assert data is not None

    def test_read_credentials(self):
        data = UserCredentialsReaderInterface.read_json_file(path=self.__file_path__)
        standard_user = data['credentials']['user_type']['standard']
        credentials = [standard_user['username'], standard_user['password']]
        assert None not in credentials

    def test_select_user_type(self):
        json_file = UserCredentialsReaderInterface.read_json_file(path=self.__file_path__)
        user_type_node = json_file['credentials']['user_type']

        user_type: dict = UserCredentialsReaderInterface.select_user_type_node(UserType.LOCKED, user_type_node)
        assert 'locked_out_user' in user_type.values()

    def test_get_username_method(self):
        username_value = UserCredentialsReaderInterface.get_username(UserType.LOCKED, file_path=self.__file_path__)

        assert username_value == 'locked_out_user'

    def test_get_password_method(self):
        password_value = UserCredentialsReaderInterface.get_password(UserType.LOCKED, file_path=self.__file_path__)

        assert password_value == 'secret_sauce'

    def test_get_users_able_to_log_in(self):
        users = UserCredentialsReaderInterface.get_only_proper_users_credentials(file_path=self.__file_path__)

        assert len(users) == 4

    def test_get_user_with_no_access(self):
        users = UserCredentialsReaderInterface.get_user_with_no_access(file_path=self.__file_path__)

        assert len(users) == 3
