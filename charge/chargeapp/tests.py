import unittest
import json
from django.core.files import File
from .models import Upload


class TestHelper(unittest.TestCase):

    def simulate_upload(self, file):
        try:
            newdoc = Upload(docfile=file)
            newdoc.full_clean()
            newdoc.save()
            newdoc.parse()
            newdoc.delete()
        except Exception as e:
            print(e)

    def try_upload_bad_file(self, file):
        with self.assertRaises(Exception):
            TestHelper.simulate_upload(file)

    def try_upload_good_file(self, file):
        upload = Upload(docfile=file)
        upload.save()
        parsed_data = upload.parse()
        upload.delete()
        for row in json.loads(parsed_data):
            assert row["LATITUDE"]
            assert row["LONGITUDE"]
            assert row["LOT_OPERATOR"]
            assert row["ADDRESS"]

class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        ROOT = "media/tests/"
        self.kml_file = File(open(ROOT+"kml_file.kml"))
        self.kmz_file = File(open(ROOT+"kmz_file.kmz"))
        self.xls_file = File(open(ROOT+"xls_file.xls"))
        self.ods_file = File(open(ROOT+"ods_file.ods"))
        self.good_csv_file = File(open(ROOT+"good.csv"))
        self.excess_column_csv_file = File(open(ROOT+"excess.csv"))
        self.missing_header_csv_file = File(open(ROOT+"missing_header.csv"))
        self.missing_column_csv_file = File(open(ROOT+"missing_column.csv"))
        self.missing_data_csv_file = File(open(ROOT+"missing_data.csv"))
        self.bad_data_file = File(open(ROOT+"bad.csv"))
        self.empty_file = File(open(ROOT+"empty.csv"))

    def tearDown(self):
        self.kml_file.close()
        self.kmz_file.close()
        self.xls_file.close()
        self.ods_file.close()
        self.good_csv_file.close()
        self.excess_column_csv_file.close()
        self.missing_header_csv_file.close()
        self.missing_column_csv_file.close()
        self.missing_data_csv_file.close()
        self.bad_data_file.close()
        self.empty_file.close()

    # tests if exceptions are thrown when we try to create the wrong file format
    def test_reject_non_csv_files(self):
        TestHelper.try_upload_bad_file(self, self.kml_file)
        TestHelper.try_upload_bad_file(self, self.kmz_file)
        TestHelper.try_upload_bad_file(self, self.xls_file)
        TestHelper.try_upload_bad_file(self, self.ods_file)

    # tests if a well formed csv file is parsed
    def test_well_formed_csv_parse_to_json_success(self):
        TestHelper.try_upload_good_file(self, self.good_csv_file)

    # tests if parser parses csv files with incorrect, excess, or no data
    # it does - the job of the parser is just to parse
    def test_excess_column_csv_parse_to_json_exception(self):
        TestHelper.try_upload_good_file(self, self.excess_column_csv_file)

    def test_bad_data_csv_parse_to_json_exception(self):
        TestHelper.try_upload_good_file(self, self.bad_data_file)

    def test_empty_csv_exception(self):
        TestHelper.try_upload_good_file(self, self.empty_file)

    # tests if parser parses csv files that are missing headings/columns/data
    # it does not as the json key values do not exist
    def test_missing_header_csv_parse_to_json_exception(self):
        TestHelper.try_upload_bad_file(self, self.missing_header_csv_file)

    def test_missing_column_csv_parse_to_json_exception(self):
        TestHelper.try_upload_bad_file(self, self.missing_column_csv_file)

    def test_missing_data_csv_parse_to_json_exception(self):
        TestHelper.try_upload_bad_file(self, self.missing_data_csv_file)
