#!/usr/bin/env python

# pylint: disable=missing-docstring

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        description="Print an ordered list of all IPv4 or IPv6 addresses that "
        "make up one or more IPv4 or IPv6 networks.")
    parser.add_argument(
        "networks", metavar="CIDR", nargs="+",
        help="A list of IPv4 or IPv6 networks given in CIDR notation.")
    args = parser.parse_args(argv[1:])

    # TODO(saj)
    print(args.networks)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
