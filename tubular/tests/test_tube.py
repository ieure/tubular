# -*- coding: utf-8 -*-
#
# © 2014, 2015 Ian Eure
# Author: Ian Eure <ian.eure@gmail.com>
#

import unittest
from pprint import pprint
from tubular.tube import WorldTube, EiaTube, EiajTube, EuroTube, Tube, Helpers

class TestWorldTube(unittest.TestCase):

    def test_test(self):
        self.assertTrue(WorldTube.test('A48AAB00X'))
        self.assertTrue(WorldTube.test('a48aab00x'))
        self.assertFalse(WorldTube.test('19VLUP22'))
        self.assertFalse(WorldTube.test('19vlup22'))

    def test_parse(self):
        self.assertEqual([['A', 'Direct view TV'],
                          ['48', '48cm / 19" diagonal viewable size'],
                          ['AAB', 'Family'],
                          ['00X', 'Phosphor type']], WorldTube.parse('A48AAB00X'))


class TestEiaTube(unittest.TestCase):

    def test_test(self):
        self.assertFalse(EiaTube.test('A48AAB00X'))
        self.assertFalse(EiaTube.test('a48aab00x'))
        self.assertTrue(EiaTube.test('19VLUP22'))
        self.assertTrue(EiaTube.test('19vlup22'))

    def test_parse(self):
        self.assertEqual([['19V', '48cm / 19" diagonal viewable size'],
                          ['LUP', 'Family'],
                          ['22', 'Phosphor']],
                         EiaTube.parse('19VLUP22'))


class TestEiajTube(unittest.TestCase):

    def test_test(self):
        self.assertFalse(EiajTube.test('A48AAB00X'))
        self.assertFalse(EiajTube.test('a48aab00x'))
        self.assertFalse(EiajTube.test('19VLUP22'))
        self.assertFalse(EiajTube.test('19vlup22'))
        self.assertTrue(EiajTube.test('3708B22'))
        self.assertTrue(EiajTube.test('3708b22'))
        self.assertTrue(EiajTube.test('370ESB22'))

    def test_parse(self):
        self.assertEqual([['370', '37cm / 15" diagonal face size'],
                          ['8', 'Family'],
                          ['B22', 'Phosphor']],
                         EiajTube.parse('3708B22'))
        print EiajTube.parse('470MSB22')


class TestEuroTube(unittest.TestCase):

    def test_test(self):
        self.assertFalse(EuroTube.test('A48AAB00X'))
        self.assertFalse(EuroTube.test('a48aab00x'))
        self.assertFalse(EuroTube.test('19VLUP22'))
        self.assertFalse(EuroTube.test('19vlup22'))
        self.assertFalse(EuroTube.test('3708B22'))
        self.assertFalse(EuroTube.test('3708b22'))
        self.assertFalse(EuroTube.test('370ESB22'))
        self.assertTrue(EuroTube.test('A37-554X'))
        self.assertTrue(EuroTube.test('a37-554x'))

    def test_parse(self):
        self.assertEqual([['A', 'Direct view TV tube'],
                          ['37', '37cm / 15" diagonal face size'],
                          ['-554', 'Family'],
                          ['X', 'Phosphor: red, green, blue (color picture tubes)']],
                         EuroTube.parse('A37-554X'))


class TestTube(unittest.TestCase):

    def test_parse(self):
        self.assertEqual([['A', 'Direct view TV'],
                          ['48', '48cm / 19" diagonal viewable size'],
                          ['AAB', 'Family'],
                          ['00X', 'Phosphor type']], Tube.parse('A48AAB00X'))

    def test_find(self):
        self.assertEqual("180DRB22", Tube.find("180DRB22 (R)"))
        self.assertEqual("M17-12", Tube.find("M17-12"))

    def test_system(self):
        self.assertEqual('WTDS (World)', Tube.system('A48AAB00X'))
        self.assertEqual('EIAJ (Japan)', Tube.system('3708B22'))



class TestHelpers(unittest.TestCase):
    def test_centisToInches(self):
        self.assertEqual(15, Helpers.centisToInches(37))
        self.assertEqual(18, Helpers.centisToInches(47))
        self.assertEqual(19, Helpers.centisToInches(48))
        self.assertEqual(20, Helpers.centisToInches(51))
        self.assertEqual(25, Helpers.centisToInches(63))

    def test_inchesToCentis(self):
        self.assertEqual(37, Helpers.inchesToCentis(15))
        self.assertEqual(47, Helpers.inchesToCentis(18))
        self.assertEqual(48, Helpers.inchesToCentis(19))
        self.assertEqual(51, Helpers.inchesToCentis(20))
        self.assertEqual(63, Helpers.inchesToCentis(25))

    def test_faceToViewable(self):
        self.assertEqual(13, Helpers.faceToViewable(15))
        self.assertEqual(19, Helpers.faceToViewable(20))


if __name__ == '__main__':
    unittest.main()
