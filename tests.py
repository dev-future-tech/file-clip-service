import unittest
from file_service import saveFiles, FileMetaSchema, FileCollSchema

class TestSaveFiles(unittest.TestCase):
    def test_saveFiles(self):
        
        files = '{ "files": [{ "name" : "file_1.txt", "content": "This is the body"}]}'

        schema = FileCollSchema()
        data = schema.loads(files)

        results = saveFiles(data)

        self.assertEqual(len(results.files), 1, "Unexpected result")
        self.assertEqual(results.files[0].file_name, "file_1.txt", "Unexepected filename")

if __name__ == '__main__':
    unittest.main()
