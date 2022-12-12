import argparse
from datetime import datetime

from parsers.cookie_file_parser import CookieFileParser, ActiveCookieFinder

if __name__ == '__main__':
    # cli parser
    parser = argparse.ArgumentParser(
        prog='CookieFinder',
        usage='Process cookie log file to find the nth most active cookie in a date.',
        description='example: $ python3 -f cookie_log.csv -d 2018-12-09'
    )
    parser.add_argument('-f', '--file',
                        required=True,
                        type=argparse.FileType('r', encoding='UTF-8'),
                        help='Cookie file path')
    parser.add_argument('-d', '--date',
                        required=True,
                        type=str,
                        help='Specify the date (dd-mm-yyyy)')
    parser.add_argument('-n', '--n',
                        type=int,
                        required=False,
                        default=0,
                        help='[optional] The nth most active cookie. default is 0 which means the most active.')

    args = parser.parse_args()
    parsed_date = datetime.fromisoformat(args.d).date()

    # application logic
    Cparser = CookieFileParser(args.f)
    finder = ActiveCookieFinder(cookie_logs=Cparser.parse())
    most_active_logs = finder.get_most_active(date=parsed_date, greater_index=args.n)
    print(*most_active_logs, sep="\n")
