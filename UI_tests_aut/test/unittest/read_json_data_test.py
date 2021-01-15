import pytest
import json

from UI_tests_aut.main.read_data.json_data.login_page.user_log_in_interface import UserLogInReaderInterface, UserType


@pytest.mark.unittest
class TestJSONReaderInterface:
    __file_path__ = 'C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/UI_tests_aut/test/unittest/data/credentails_backup_data.json'

    def test_read_json_file(self):
        with open(self.__file_path__) as f:
            data = json.load(f)

        assert data is not None

    def test_read_credentials(self):
        data = UserLogInReaderInterface.read_json_file(path=self.__file_path__)
        standard_user = data['credentials']['user_type']['standard']
        credentials = [standard_user['username'], standard_user['password']]
        assert None not in credentials

    def test_select_user_type(self):
        json_file = UserLogInReaderInterface.read_json_file(path=self.__file_path__)
        user_type_node = json_file['credentials']['user_type']

        user_type: dict = UserLogInReaderInterface.select_user_type_node(UserType.LOCKED, user_type_node)
        assert 'locked_out_user' in user_type.values()

    def test_get_username_method(self):
        username_value = UserLogInReaderInterface.get_username(UserType.LOCKED, file_path=self.__file_path__)

        assert username_value == 'locked_out_user'

    def test_get_password_method(self):
        password_value = UserLogInReaderInterface.get_password(UserType.LOCKED, file_path=self.__file_path__)

        assert password_value == 'secret_sauce'

    def test_get_users_able_to_log_in(self):
        users = UserLogInReaderInterface.get_only_proper_users_credentials(file_path=self.__file_path__)

        assert len(users) == 3

    def test_get_user_with_no_access(self):
        users = UserLogInReaderInterface.get_user_with_no_access(file_path=self.__file_path__)

        assert len(users) == 2
