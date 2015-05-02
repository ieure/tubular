# -*- coding: utf-8 -*-
#
# © 2015 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Data loader"""

import json
import pkg_resources

def load(file_):
    fname = pkg_resources.resource_filename('tubular', 'data/' + file_)
    return open(fname, 'r')


def loadjson(file_):
    with load(file_) as fd:
        return json.load(fd)
