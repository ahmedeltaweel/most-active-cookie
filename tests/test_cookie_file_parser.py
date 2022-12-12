import io
import unittest
from datetime import datetime
from typing import Dict, List

from parsers.cookie_file_parser import CookieFileParser
from parsers.models import CookieLog


class TestCookieFileParser(unittest.TestCase):

    def test_parse_csv_file_coorectly(self) -> None:
        testcases: List[Dict[str, List[CookieLog]]] = [{
            "cookie,timestamp\nAtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\nAtY0laUfhglK3lC8,2018-12-09T14:18:00+00:00":
            [CookieLog(
                cookie="AtY0laUfhglK3lC7", timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")),
             CookieLog(
                cookie="AtY0laUfhglK3lC8", timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00"))]},
            {"": []},
            {"cookietimestampAtY0laUfhglK3lC7": []}]

        for testcase in testcases:
            for input, output in testcase.items():
                fh_bytes = io.BytesIO(str.encode(input))
                fh = io.TextIOWrapper(fh_bytes, encoding='utf-8', newline='\n')
                finder = CookieFileParser(fh)
                result = finder.parse()

                self.assertCountEqual(result, output)
