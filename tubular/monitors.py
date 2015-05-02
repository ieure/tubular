# -*- coding: utf-8 -*-
#
# © 2015 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Monitor helpers"""

import re
from tubular.tube import Tube

SLUG_CHARS = {'"': " inch"}
SLUG = re.compile(r'[^[a-z0-9-]+')

def slug(manufacturer, model):
    name = ("%s %s" % (manufacturer, model)).lower().strip()
    for (ch, repl) in SLUG_CHARS.iteritems():
        name = name.replace(ch, repl)
    return SLUG.sub('-', name)


def expand(manufacturer, model, data):
    data['type'] = data['type'].title()
    if 'sync' in data:
        data['sync'] = [{'sync': sync} for sync in data['sync']]

    if 'docs' in data:
        new_docs = [{'title': k, 'uri': v}
                    for (k, v) in data['docs'].iteritems()]
        data['docs'] = new_docs

    if 'photos' in data:
        data['photos'] = [{'uri': it} for it in data['photos']]

    data['manufacturer'] = manufacturer
    data['model'] = model
    data['color'] = "Color" if data['color'] else "B&W"
    data['simple_tube'] = Tube.simplify(data['tube'])
    data['class'] = ("%s %s" % (data['color'].replace('&', ''),
                                data['type'])).lower()
    return data
