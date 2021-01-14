import pytest
import json

from read_data.json_test_data.login_page_test_data.json_reader import ReaderJSON, UserType


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
        json_file = ReaderJSON.read_json_file()
        user_type_node = json_file['credentials']['user_type']

        user_type: dict = ReaderJSON.select_user_type_node(UserType.STANDARD, user_type_node)
        assert 'standard_user' in user_type.values()

    def test_select_credentials(self):
        # credentials = ReaderJSON.select_user_credentials('standard')
        # print(credentials)
        pass
# with pytest.raises(JSONDecodeError):
# with open('../data/login_page_test_data/credentials_data.json') as f:
# data = json.load(f)
