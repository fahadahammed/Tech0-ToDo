import os
import json
import sys
import datetime
import time
from ToDo import app


class JsonDatabaseLibrary:
    def __init__(self, json_db_file=None):
        self.protected_path = os.getcwd() + f'/{app.config["PROTECTED_PATH"]}/'
        if json_db_file:
            self.json_db_file = json_db_file
            self.json_db_file_path = self.protected_path + self.json_db_file

    def create_file(self, content):
        try:
            with open(self.json_db_file_path, 'w') as outfile:
                json.dump(content, outfile)
                return True
        except Exception:
            return False

    def list_of_all_files(self):
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.protected_path):
            files.extend(filenames)
            break
        return files

    def read_file(self, filename):
        final_filename = self.protected_path + filename
        try:
            with open(final_filename) as json_file:
                data = json.load(json_file)
            return data
        except Exception:
            return False

    def delete_file(self, filename):
        final_filename = self.protected_path + filename
        try:
            os.unlink(final_filename)
            return True
        except Exception:
            return False