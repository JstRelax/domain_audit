# Impacket - Collection of Python classes for working with network protocols.
#
# SECUREAUTH LABS. Copyright (C) 2019 SecureAuth Corporation. All rights reserved.
#
# This software is provided under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# Description:
#   This logger is intended to be used by impacket instead
#   of printing directly. This will allow other libraries to use their
#   custom logging implementation.
#

import logging as _logging
import sys

# This module can be used by scripts using the Impacket library
# in order to configure the root logger to output events
# generated by the library with a predefined format

# If the scripts want to generate log entries, they can write
# directly to the root logger (logging.info, debug, etc).


class ImpacketFormatter(_logging.Formatter):
    """
    Prefixing logged messages through the custom attribute 'bullet'.
    """

    def __init__(self):
        _logging.Formatter.__init__(self, "%(bullet)s %(message)s", None)

    def format(self, record):
        if record.levelno == _logging.INFO:
            record.bullet = "[*]"
        elif record.levelno == _logging.DEBUG:
            record.bullet = "[+]"
        elif record.levelno == _logging.WARNING:
            record.bullet = "[!]"
        else:
            record.bullet = "[-]"

        return _logging.Formatter.format(self, record)


class ImpacketFormatterTimeStamp(ImpacketFormatter):
    """
    Prefixing logged messages through the custom attribute 'bullet'.
    """

    def __init__(self):
        _logging.Formatter.__init__(
            self, "[%(asctime)-15s] %(bullet)s %(message)s", None
        )

    def formatTime(self, record, datefmt=None):
        return ImpacketFormatter.formatTime(self, record, datefmt="%Y-%m-%d %H:%M:%S")


def init(ts=False):
    # We add a StreamHandler and formatter to the root logger
    handler = _logging.StreamHandler(sys.stdout)
    if not ts:
        handler.setFormatter(ImpacketFormatter())
    else:
        handler.setFormatter(ImpacketFormatterTimeStamp())
    _logging.getLogger("certipy").addHandler(handler)
    _logging.getLogger("certipy").setLevel(_logging.INFO)
    _logging.getLogger("certipy").propagate = False


logging = _logging.getLogger("certipy")
