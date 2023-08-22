import os
import locale

from helpers import TestCSVFiles


class TestAgimexParser(TestCSVFiles):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.parser_key = "AGIMEX"

    def test_csv_files(self):
        locale.setlocale(locale.LC_TIME, "es_ES.utf8")
        # super().compare_csv_files()
