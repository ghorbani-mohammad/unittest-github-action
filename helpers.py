import os
import unittest


class TestCSVFiles(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_dir = None
        self.parser_key = None

    def compare_csv_files(self):
        test_files = [
            f
            for f in os.listdir(self.test_dir)
            if f.endswith(".csv") or f.endswith(".json")
        ]
        print(f"test files: {test_files}")
        print()

        if len(test_files) % 2 != 0:
            raise ValueError("Number of test files must be even")

        for i in range(0, len(test_files), 2):
            input_path = test_files[i+1] if "expected" in test_files[i] else test_files[i]
            input_path = os.path.join(self.test_dir, input_path)
            expected_path = test_files[i+1] if "expected" in test_files[i+1] else test_files[i]
            expected_path = os.path.join(self.test_dir, expected_path)
            print()
            print(f"input-path: {input_path}")
            print(f"expected-path: {expected_path}")

            with open(input_path, "r", encoding="utf-8", errors="ignore") as input_file:
                input_data = input_file.read()

            with open(expected_path, "r", encoding="utf-8") as expected_file:
                expected_content = [line.strip() for line in expected_file.readlines()]

            print(f"length of input: {len(input_data)}")
            print(f"length of expected: {len(expected_content)}")
            print()
            return
            # for index, item in enumerate(expected_content):
            #     print()
            #     print(index)
            #     print(item)

            print()
            parsed_content = []
            expected_content = expected_content[1:]

            error_result = []

            for i in range(max(len(parsed_content), len(expected_content))):
                parsed_line = parsed_content[i]
                expected_line = expected_content[i]
                try:
                    self.assertEqual(parsed_line, expected_line)
                except AssertionError as error:
                    self.print_error(
                        error, input_path, i + 2, parsed_line, expected_line
                    )
                    error_result.append(f"parsed,{parsed_line}")
                    error_result.append(f"expected,{expected_line}")