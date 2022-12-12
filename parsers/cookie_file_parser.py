import csv
from datetime import date, datetime
from typing import List, Dict
from io import TextIOWrapper

from .models import CookieLog


class CookieFileParser:
    """
    A class to represent a single cookielog.
    CookieFileParser: is used to parse the cookies log file and map the data into interal list of CookieLog type.
    ...

    Attributes
    ----------
    file : TextIOWrapper
        csv text data read from the cli file arg.

    Methods
    -------
    parse(self) -> List[CookieLog]:
        Parse the csv data and return a list of system know CookieLog objest.
    """

    def __init__(self, file: TextIOWrapper) -> None:
        self.file = file

    def parse(self) -> List[CookieLog]:
        data = self.file.read()
        csvdata = csv.reader(data.split("\n"))
        next(csvdata)  # skip the titles row

        cookie_logs = [
            CookieLog(
                cookie=row[0],
                timestamp=datetime.fromisoformat(row[1])
            ) for row in csvdata
        ]
        self.file.close()
        return cookie_logs


class ActiveCookieFinder:
    """
    A class to represent a cookies activies in certain date.
    ActiveCookieFinder: uses the pased data from CookieFileParser to caluclate the most active cookies per certain date.
    ...

    Attributes
    ----------
    cookie_logs : List[CookieLog]
        List CookieLog objects.

    Methods
    -------
    __parse_logs(self):
        Parse the list of CookieLog object to calculate the activiers per day in form of
        Dict[date, Dict[CookieLog, int]] objects.

    __calculate_cookie_activites_per_day(self):
        Calclate the number activies for certain date in a reverse form of Dict[date, Dict[int, List[CookieLog]]]
        to ease the calculation.

    get_most_active(self, date: date, greater_index: int = 0) -> List[str]:
        return the nth most active cookie per day. greater_index is used to reflect n.
        ie:
            if the most active cookie is needed, then greater_index should be = 0.
            if the 2nd most active cookie is needed, then greater_index should be = 1. and so on.
    """

    def __init__(self, cookie_logs: List[CookieLog]) -> None:
        self.cookie_logs = cookie_logs
        self.cookies_activities_per_day: Dict[date, Dict[CookieLog, int]] = {}
        self.most_active_cookies_per_day: Dict[date, Dict[int, List[CookieLog]]] = {}

        self.__parse_logs()
        self.__calculate_cookie_activites_per_day()

    def __parse_logs(self):
        for i in self.cookie_logs:
            date = i.timestamp.date()
            if date not in self.cookies_activities_per_day.keys():
                self.cookies_activities_per_day[date] = {i.cookie: 1}
                continue
            self.cookies_activities_per_day[date][
                i.cookie] = self.cookies_activities_per_day[date].setdefault(
                i.cookie, 0) + 1

    def __calculate_cookie_activites_per_day(self):
        for date, cookielogs in self.cookies_activities_per_day.items():
            activity: Dict[int, List[CookieLog]] = {}
            for cookielog, number_of_oocerience in cookielogs.items():
                if number_of_oocerience in activity:
                    activity[number_of_oocerience].append(cookielog)
                    continue
                activity[number_of_oocerience] = [cookielog]
            self.most_active_cookies_per_day[date] = activity

    def get_most_active(self, date: date, greater_index: int = 0) -> List[str]:
        most_active = self.most_active_cookies_per_day.get(date)
        if not most_active:
            return ["No logs found"]
        keys = sorted(most_active.keys(), reverse=True)
        if len(keys) <= greater_index:
            return ["No logs found"]
        return most_active[keys[greater_index]]
