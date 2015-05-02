# -*- coding: utf-8 -*-
#
# © 2014 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#

import unittest
from tubular.make_tubes import expand_sencore

class TestExpendSencore(unittest.TestCase):

    def test_expand(self):
        data = ["19VLUP22", 22, "V", 6.3, "D"]
        self.assertEqual({'model': 22,
                          'heater': 6.3,
                          'bias': "V",
                          'socket': "D"}, expand_sencore(data[1:]))


if __name__ == '__main__':
    unittest.main()
