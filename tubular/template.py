# -*- coding: utf-8 -*-
#
# © 2015 Ian Eure
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Template rendering"""

import pystache
import pkg_resources

RENDERER = pystache.Renderer(
    file_encoding="utf-8",
    string_encoding="utf-8",
    file_extension="html",
    # missing_tags="strict",
    search_dirs=pkg_resources.resource_filename('tubular', 'data/templates'))
