import unittest

from src.annakeren.ipa.engine.main import Engine

class EngineTest(unittest.TestCase):
    def testStandStamb(self):
        stand = unichr(0x73)+unichr(0x74)+unichr(0x6e)+unichr(0x64)
        stamb = unichr(0x73)+unichr(0x74)+unichr(0x6d)+unichr(0x62)
        actual = Engine.Engine.findMatch(stamb, stand)
        self.assertEqual(4, actual, "msg")
        
    def testNaiceNaish(self):
        naice = unichr(0x6e) + unichr(0x73)
        naish = unichr(0x6e) + unichr(0x0283)
        actual = Engine.Engine.findMatch(naice, naish)
        self.assertEqual(2, actual, "msg")
        
    def testZaeSea(self):
        sea = unichr(0x73)
        zea = unichr(0x7a)
        actual = Engine.Engine.findMatch(zea, sea)
        self.assertEqual(1, actual, "msg")
        
    def testSnegSnowSheleg(self):
        sneg = unichr(0x73) + unichr(0x6e) + unichr(0x67)
        snow = unichr(0x73) + unichr(0x6e)
        sheleg = unichr(0x0283) + unichr(0x6c) + unichr(0x67)
        
        actualSnegSnow = Engine.Engine.findMatch(sneg, snow)
        self.assertEqual(3, actualSnegSnow, "msg")
        
        actualSnowSheleg = Engine.Engine.findMatch(snow, sheleg)
        self.assertEqual(2, actualSnowSheleg, "msg")
        
        actualSnegSheleg = Engine.Engine.findMatch(sneg, sheleg)
        self.assertEqual(3, actualSnegSheleg, "msg")