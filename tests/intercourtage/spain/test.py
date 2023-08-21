import os

from parsers.generic.tests.helpers import TestCSVFiles

from dispatcher import INTERCOURTAGE_SPAIN


class TestIntercourtageSpainParser(TestCSVFiles):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.parser_key = INTERCOURTAGE_SPAIN

    def test_csv_files(self):
        super().compare_csv_files()
