import unittest
from typing import Dict, List, Tuple

from datetime import datetime
from parsers.models import CookieLog

from parsers.active_cookie_finder import ActiveCookieFinder


class TestActiveCookieFinder(unittest.TestCase):

    def test_calculate_most_active_cookie(self) -> None:
        testcases: List[Dict[List[CookieLog], Tuple[str]]] = [
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00")
                    )
                ): [
                    "AtY0laUfhglK3lC7"
                ]
            },
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-09T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-09T14:18:00+00:00"))
                ): [
                    "AtY0laUfhglK3lC7",
                    "AtY0laUfhglK3lC8"
                ]
            },
            {
                (
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-11T14:19:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC7",
                        timestamp=datetime.fromisoformat("2018-12-12T14:17:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-03T14:18:00+00:00")
                    ),
                    CookieLog(
                        cookie="AtY0laUfhglK3lC8",
                        timestamp=datetime.fromisoformat("2018-12-05T14:18:00+00:00"))
                ): [
                    "No logs found"
                ]
            },
            {
                (): ["No logs found"]
            }
        ]

        for testcase in testcases:
            for input, output in testcase.items():
                finder = ActiveCookieFinder(input)
                result = finder.get_most_active(datetime.fromisoformat("2018-12-09T14:19:00+00:00").date())
                self.assertCountEqual(result, output)
