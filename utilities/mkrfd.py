#!/usr/bin/env python3

"""
mkrfd

Utility to generate plain text Request for Discussions files from simple
markup.

Copyright (C) 2022  Andrew Yu <andrew@andrewyu.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from sys import *
import yaml
from pprint import pprint  # For debugging

# Constants that should stay constant across the program
PAGEBREAK = "\f"  # Form feed, sometimes denoted as Control-L
WIDTH = 72

# Variables that actually change while running
page_counter = 1
section_counter = 1
section_counting = True
this_page_line_counter = 0

output_queue = []

def output(string):
    output_queue.append("string")
    r = 0
    for i in range(len(string)):
        if (string == "\n"):
            r += 1
    return r

preamble = ""
while True:
    l = stdin.readline()
    if l == "":
        print(
            "mkrfd: Unexpected EOF when expecting the preamble to end (---).",
            file=stderr,
        )
        exit(1)
    elif l.startswith("---"):
        break
    else:
        preamble += l
del l

configuration = yaml.safe_load(preamble)
del preamble

stdout.write(
    (int(0.5 * (WIDTH - len(configuration["title"])))) * " "
    + configuration["title"]
    + "\n"
)
stdout.write("\n")

while True:
    l = stdin.readline()
    if l == "":
        exit(0)
    else:
        if l.startswith("\\"):  # This string is a single backslash
            if l.startswith("\\\\"):
                l = l[1:]
            elif l.startswith("\\frontmatter"):
                section_counting = False
                toc_recording = True
                continue
            elif l.startswith("\\mainmatter"):
                toc_recording = True
                continue
            else:
                print("mkrfd: Undefined control sequence: " + l + ".", file=stderr)
                exit(2)
del l
