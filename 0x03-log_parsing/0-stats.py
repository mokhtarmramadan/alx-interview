#!/usr/bin/python3
''' log parsing '''
import re
import sys
from typing import Dict

# Initialize the status code dictionary and total file size
status_code_dict: Dict[str, int] = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_file_size: int = 0


def line_parser(line: str) -> None:
    ''' parses a line using regex '''
    global total_file_size
    global status_code_dict

    log_pattern = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
        r'"GET /projects/\d+ HTTP/1\.1" (\d{3}) (\d+)$'
    )
    match_line = log_pattern.match(line)
    if match_line:
        status_code = match_line.group(1)
        response_size = int(match_line.group(2))
        total_file_size += response_size

        if status_code in status_code_dict:
            status_code_dict[status_code] += 1


def print_statistics() -> None:
    ''' After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning '''
    global total_file_size
    global status_code_dict
    print("File size: {}".format(total_file_size))
    for k, v in sorted(status_code_dict.items()):
        if v > 0:
            print("{}: {}".format(k, v))


def main():
    ''' Entry point '''
    counter: int = 0
    try:
        for line in sys.stdin:
            counter += 1
            line_parser(line)
            if counter == 10:
                print_statistics()
                counter = 0
    except KeyboardInterrupt:
        pass
    finally:
        print_statistics()


if __name__ == "__main__":
    main()
