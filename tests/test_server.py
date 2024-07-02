# import pytest
# import configparser
# from ..server import Server


# def test_load_config_success(mocker):
#     # Mock configparser.ConfigParser.read to simulate successful config loading
#     mocker.patch.object(configparser.ConfigParser, 'read', return_value=None)
#     server = Server(8080)

#     # Check if the 'Server' section exists
#     assert server.linux_path == '200k.txt'
#     assert server.reread_on_query is True
#     assert server.ssl_enabled is False


# def test_load_config_missing_file(mocker):
#     # Mock configparser.ConfigParser.read to raise an exception
#     mocker.patch.object(configparser.ConfigParser, 'read',
#                         side_effect=configparser.NoSectionError('Server'))
#     with pytest.raises(configparser.NoSectionError):
#         Server(8080)


# def test_load_file_success(tmp_path):
#     # Create a temporary file
#     test_file = tmp_path / 'test.txt'
#     with test_file.open('w') as f:
#         f.write('Line 1\nLine 2')
#     server = Server(8080)
#     server.linux_path = str(test_file)
#     server.load_file()
#     assert server.file_content == 'Line 1\nLine 2'


# def test_load_file_not_found():
#     server = Server(8080)
#     server.linux_path = 'non-existent-file.txt'
#     server.load_file()
#     assert server.file_content == ''


# def test_linear_search_exists():
#     server = Server(8080)
#     server.file_content = 'Line 1\nLine 2'
#     assert server.linear_search('Line 2') is True


# def test_linear_search_not_found():
#     server = Server(8080)
#     server.file_content = 'Line 1\nLine 2'
#     assert server.linear_search('Line 3') is False


# def test_linear_search_empty_file():
#     server = Server(8080)
#     server.file_content = ''
#     assert server.linear_search('Line 1') is False
