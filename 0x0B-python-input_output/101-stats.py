#!/usr/bin/python3
"""
101-stats.py
"""

import sys

# Dictionary storing status code counts
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:

        parts = line.split()

        if len(parts) >= 2:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            total_file_size += int(file_size)

            line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))
