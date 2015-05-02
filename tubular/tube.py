# -*- coding: utf-8 -*-
#
# © 2014, 2015 Ian Eure
# Author: Ian Eure <ian.eure@gmail.com>
#
"""Tube parsing

   See http://wiki.arcadeotaku.com/w/CRT_designation_systems"""

import re

SIMPLIFY_RE = re.compile(r'(X)[0-9]+$')

class Helpers():

    parse_regex = None
    match_regex = None

    @classmethod
    def centisToInches(cls, centimeters):
        return round(int(centimeters) / 2.54);

    @classmethod
    def inchesToCentis(cls, inches):
        return round(int(inches) * 2.54);

    @classmethod
    def faceToViewable(cls, inches):
        m = {15: 13,
             20: 19}
        return m[inches]

    @classmethod
    def test(cls, tube):
        return bool(cls._test(tube))

    @classmethod
    def _test(cls, tube):
        if tube:
            return cls.parse_regex.match(tube)

    @classmethod
    def _groups(cls, tube):
        m = cls._test(tube)
        if not m:
            raise TypeError("`%s' is not a %s" % (tube, cls))
        return m.groups()

    @classmethod
    def find(cls, tube):
        m = cls.parse_regex.search(tube)
        if m:
            return m.group(0)

    @classmethod
    def simplify(cls, tube):
        return SIMPLIFY_RE.sub('\\1', tube)


class WorldTube(Helpers):
    parse_regex = re.compile(r'^([ABMW])([0-9]{2})([A-Z]{3})([0-9A-Z]+)', re.I)
    name = "WTDS (World)"
    applications = {"A": "Direct view TV",
                    "B": "Direct view TV, remanufactured / B quality",
                    "M": "Direct view monitor",
                    "W": "Widescreen direct view TV"}

    @classmethod
    def parse(cls, tube):
        m = cls._groups(tube)
        return [
            [m[0], cls.applications[m[0]]],
            [m[1], '%dcm / %d" diagonal viewable size' % (
                int(m[1]), cls.centisToInches(m[1]))],
            [m[2], "Family"],
            [m[3], "Phosphor type"]]


class EiaTube(Helpers):
    parse_regex = re.compile(r'^([0-9]{2}V?)([A-Z]{2,3})([0-9]+)([A-Z])?$', re.I)
    name = "EIA (USA)"

    @classmethod
    def parse(cls, tube):
        m = cls._groups(tube)
        out = []
        size = m[0];

        if size[-1] == "V":
            desc = "diagonal viewable size";
            size = size[:-1]
        else:
            desc = "diagonal face size";

        out.append([m[0], '%dcm / %s" %s' % (int(cls.inchesToCentis(size)), size, desc)])

        out.append([m[1], "Family"])
        out.append([m[2], "Phosphor"])
        if m[3]:
            out.append([m[3], "Revision " + m[3]]);

        return out


class EiajTube(Helpers):
    parse_regex = re.compile(r'^([0-9]{3})([0-9A-Z]{1,2})(B[0-9]+)(-[A-Z0-9]+)?', re.I)
    name = "EIAJ (Japan)"

    @classmethod
    def parse(cls, tube):
        m = cls._groups(tube)
        out = []

        size = int(int(m[0]) / 10)
        out.append([m[0],
                    '%dcm / %d" diagonal face size' % (
                        size, cls.centisToInches(size))])
        out.append([m[1], "Family"])
        out.append([m[2], "Phosphor"])
        if m[3]:
            out.append([m[3], "Yoke"])

        return out

class EuroTube(Helpers):
    parse_regex = re.compile(r'^([ADEFLMPQ])([0-9]{2})(-[0-9]+)([A-Z])', re.I)
    name = "Pro Electron (Europe)"
    applications = {
        "A": "Direct view TV tube",
        "D": "Single trace oscilloscope tube",
        "E": "Multiple trace oscilloscope tube",
        "F": "Direct view radar tube",
        "L": "Display storage tube",
        "M": "Direct view tube for professional TV / monitor",
        "P": "Projection tube",
        "Q": "Flying spot scanner"}
    phosphorTypes = {
        "A": "reddish purple, purple, blueish purple",
        "B": "purplish blue, blue, greenish blue",
        "D": "blue-green",
        "G": "blueish green, green, yellowish green",
        "K": "yellow-green",
        "L": "orange, orange-pink",
        "R": "reddish orange, red, pink, purplish pink, purplish red, red-purple",
        "W": "standard white (black and white tubes)",
        "X": "red, green, blue (color picture tubes)",
        "Y": "greenish yellow, yellow, yellowish orange"}

    @classmethod
    def parse(cls, tube):
        m = cls._groups(tube);
        out = []
        out.append([m[0], cls.applications[m[0]]])
        size = int(m[1])
        out.append([m[1], '%dcm / %d" diagonal face size' % (
            size, cls.centisToInches(size))])
        out.append([m[2], "Family"])
        out.append([m[3], "Phosphor: " + EuroTube.phosphorTypes[m[3]]])

        return out


class Tube(Helpers):

    systems = [WorldTube, EiaTube, EiajTube, EuroTube]

    @classmethod
    def parse(cls, tube):
        for system in cls.systems:
            if system.test(tube):
                return system.parse(tube)

    @classmethod
    def find(cls, tube):
        for system in cls.systems:
            f = system.find(tube)
            if f:
                return f

        # print "WARN: Can't parse tube `%s'" % tube
