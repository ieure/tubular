# -*- coding: utf-8 -*-
#
# © 2014, 2015 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Make monitor ID page."""

import pystache
import argparse
from tubular.tube import Tube
from . loader import load, loadjson
from . monitors import slug, expand
from . template import RENDERER

def get_parser():
    p = argparse.ArgumentParser(description="Make monitor ID page")
    p.add_argument('--target', dest='target', default='target/',
                   help='Output directory')
    return p


def main():
    p = get_parser()
    args = p.parse_args()
    monitors = loadjson('monitor_data.json')
    with load('templates/monitor_id_page.html') as fd:
        template = pystache.parse(unicode(fd.read(), 'utf-8'))

    target = args.target
    if target[-1] != '/':
        target += '/'

    monitor_list = []
    for (manufacturer, monitors) in monitors.iteritems():
        for (model, data) in monitors.iteritems():
            if 'photos' not in data or not data['photos']:
                # Entries with no photos aren't helpful.
                pass
            else:
                monitor_list.append(
                    {'monitor': expand(manufacturer, model, data)})

    context = {'monitors': monitor_list}
    with open('%smonitor/identify.html' % target, 'w') as fd:
        fd.write(RENDERER.render(template, context).encode('utf-8'))
