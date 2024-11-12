import unittest
from file_service import saveFiles, FileCollSchema, connectDB
from unittest.mock import MagicMock, Mock
from unittest.mock import patch

class TestSaveFiles(unittest.TestCase):

    @patch('psycopg.connect')
    def test_database_connection(self, mock_connect):

        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value.fetch_one.return_value = ['1']
        mock_cursor.__exit__ = MagicMock()

        mock_connect.return_value.cursor.return_value = mock_cursor

        files = '{ "files": [{ "name" : "file_1.txt", "content": "This is the body"}]}'

        schema = FileCollSchema()
        data = schema.loads(files)

        results = saveFiles(data)
        print(results)
        print(results.files[0].file_id)
        self.assertEqual(results.files[0].file_id, 1, "Identifier doesn't match")

    @patch('psycopg.connect')
    def test_saveFiles(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value.fetch_one.return_value = {
            "file_id": 1,
            "file_name" : "file1.txt",
            "content" : "content of file 1"
        }

        mock_cursor.__exit__ = MagicMock()

        mock_connect.return_value.cursor.return_value = mock_cursor

        files = '{ "files": [{ "name" : "file_1.txt", "content": "This is the body"}]}'

        schema = FileCollSchema()
        data = schema.loads(files)

        results = saveFiles(data)

        self.assertEqual(len(results.files), 1, "Unexpected result")
        self.assertEqual(results.files[0].file_name, "file_1.txt", "Unexepected filename")

if __name__ == '__main__':
    unittest.main()
