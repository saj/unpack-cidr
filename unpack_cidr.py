#!/usr/bin/env python

# pylint: disable=missing-docstring

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import itertools
import sys

import ipaddress
import six
import sortedcontainers

import _about


def network_hosts(net):
    return net.hosts()


def network_addresses(net):
    return itertools.chain([net.network_address],
                           network_hosts(net),
                           [net.broadcast_address])


def get_encoding():
    truths = [
        sys.stdout.encoding, sys.stderr.encoding,
        "ascii", # Guess.
    ]
    return next(t for t in truths if t)


def unicodify(stringish):
    if isinstance(stringish, six.text_type):
        return stringish
    return stringish.decode(get_encoding())


def network(cidr):
    return ipaddress.ip_network(unicodify(cidr))


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        prog=_about.NAME,
        description="Print an ordered list of all IPv4 or IPv6 addresses that "
        "make up one or more IPv4 or IPv6 networks.")
    parser.add_argument(
        "--version", action="version",
        version="%(prog)s {version}".format(version=_about.VERSION))
    parser.add_argument(
        "--usable", action="store_true",
        help="Limit output to usable network addresses.  Exclude network and "
        "broadcast addresses.")
    parser.add_argument(
        "cidrs", metavar="CIDR", nargs="+",
        help="A list of IPv4 or IPv6 networks given in CIDR notation.")
    args = parser.parse_args(argv[1:])

    addr_func = network_addresses
    if args.usable:
        addr_func = network_hosts

    addrs = sortedcontainers.SortedSet()
    for net in [network(c) for c in args.cidrs]:
        for addr in addr_func(net):
            addrs.add(addr)

    for addr in addrs.islice():
        print(addr.compressed)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
