# unpack-cidr

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
[![CircleCI](https://circleci.com/gh/saj/unpack-cidr.svg?style=svg&circle-token=045c569dbd0749d500cb521cbc09e16475ab80e9)](https://circleci.com/gh/saj/unpack-cidr)

Decompose IPv4/6 CIDR network notation to discrete IPv4/6 addresses.

```
% unpack-cidr 10.0.0.16/30 192.168.10.97/29
10.0.0.16
10.0.0.17
10.0.0.18
10.0.0.19
192.168.10.96
192.168.10.97
192.168.10.98
192.168.10.99
192.168.10.100
192.168.10.101
192.168.10.102
192.168.10.103
```
