# -*- coding: utf-8 -*-
#
# © 2014, 2015 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Make monitor data pages."""

import re
import pystache
import argparse
from . loader import load, loadjson
from . monitors import slug, expand
from . template import RENDERER

def get_parser():
    p = argparse.ArgumentParser(description="Make monitor permalink pages")
    p.add_argument('--target', dest='target', default='target/',
                   help='Output directory')
    return p


def main():
    p = get_parser()
    args = p.parse_args()
    monitors = loadjson('monitor_data.json')
    with load('templates/monitor_page.html') as fd:
        template = pystache.parse(unicode(fd.read(), 'utf-8'))

    target = args.target
    if target[-1] != '/':
        target += '/'

    for (manufacturer, monitors) in monitors.iteritems():
        for (model, data) in monitors.iteritems():
            outf = slug(manufacturer, model)
            context = {'monitor': expand(manufacturer, model, data)}

            with open('%s%s.html' % (target, outf), 'w') as fd:
                fd.write(RENDERER.render(template, context).encode('utf-8'))
