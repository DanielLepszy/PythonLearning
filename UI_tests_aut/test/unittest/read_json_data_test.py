import pytest
import json

from read_data.json_data.login_page.json_reader import UserCredentialsReaderInterface, UserType


@pytest.mark.unittestJSON
class TestJSONReaderInterface:

    def test_read_json_file(self):
        with open('data/file_for_test.json') as f:
            data = json.load(f)

        assert data is not None

    def test_read_credentials(self):
        with open('data/file_for_test.json') as f:
            data = json.load(f)

        standard_user = data['credentials']['user_type']['standard']
        credentials = [standard_user['username'], standard_user['password']]
        assert None not in credentials

    def test_select_user_type(self):
        json_file = UserCredentialsReaderInterface.read_json_file()
        user_type_node = json_file['credentials']['user_type']

        user_type: dict = UserCredentialsReaderInterface.select_user_type_node(UserType.LOCKED, user_type_node)
        assert 'locked_out_user' in user_type.values()

    def test_get_username_method(self):
        username_value = UserCredentialsReaderInterface.get_username(UserType.LOCKED)

        assert username_value == 'locked_out_user'

    def test_get_password_method(self):
        password_value = UserCredentialsReaderInterface.get_password(UserType.LOCKED)

        assert password_value == 'secret_sauce'

