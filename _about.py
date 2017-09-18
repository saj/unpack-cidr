# pylint: disable=missing-docstring

from __future__ import absolute_import


def _derive_version():
    version = "0.dev1"
    try:
        # pylint: disable=wrong-import-position
        import _version
        # pylint: enable=wrong-import-position
    except ImportError:
        pass
    else:
        version = _version.VERSION
    return version


NAME = "unpack-cidr"
VERSION = _derive_version()
DESCRIPTION = ("Decompose IPv4/6 CIDR network notation to discrete IPv4/6 "
               "addresses.")

AUTHOR = "Saj Goonatilleke"
EMAIL = "sg@redu.cx"
