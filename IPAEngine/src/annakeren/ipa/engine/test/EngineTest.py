import unittest

from src.annakeren.ipa.engine.main import Engine

class EngineTest(unittest.TestCase):
    def testStandStamb(self):
        print 'English consonant shift in connected speech:'
        stand = unichr(0x73)+unichr(0x74)+unichr(0x6e)+unichr(0x64)
        stamb = unichr(0x73)+unichr(0x74)+unichr(0x6d)+unichr(0x62)
        print '(stand)' + stand + ' vs ' + stamb + '(like in stand back)'
        actual = Engine.Engine.findMatch(stamb, stand)
        self.assertEqual(4, actual, "msg")
        
    def testNaiceNaish(self):
        print "English consonant shift in connected speech:"
        naice = unichr(0x6e) + unichr(0x73)
        naish = unichr(0x6e) + unichr(0x0283)
        print '(nice)' +naice + ' vs ' + naish + '(like in nice shoes)'
        actual = Engine.Engine.findMatch(naice, naish)
        self.assertEqual(2, actual, "msg")
        
    def testZaeSea(self):
        print 'English consonant shift in connected speech:'
        sea = unichr(0x73)
        zea = unichr(0x7a)
        print '(sea)' + sea + ' vs ' + zea + '(like in swansea)'
        actual = Engine.Engine.findMatch(zea, sea)
        self.assertEqual(1, actual, "msg")
        
    def testSnegSnowSheleg(self):
        print 'Russian and English'
        sneg = unichr(0x73) + unichr(0x6e) + unichr(0x67)
        snow = unichr(0x73) + unichr(0x6e)
        sheleg = unichr(0x0283) + unichr(0x6c) + unichr(0x67)
        print '(sneg)' + sneg + ' vs ' + snow + '(snow)'

        actualSnegSnow = Engine.Engine.findMatch(sneg, snow)
        self.assertEqual(3, actualSnegSnow, "msg")
        
        print 'English and Hebrew'
        print '(snow)' + snow + ' vs ' + sheleg + '(sheleg)'
        actualSnowSheleg = Engine.Engine.findMatch(snow, sheleg)
        self.assertEqual(2, actualSnowSheleg, "msg")
        
        print 'Russian and Hebrew'
        print '(sheleg)' + sheleg + ' vs ' + sneg + '(sneg)'
        actualSnegSheleg = Engine.Engine.findMatch(sneg, sheleg)
        self.assertEqual(3, actualSnegSheleg, "msg")
        
    def testStarZvezda(self):  
        
        print 'English and Russian'
        
        star = unichr(0x73) + unichr(0x74)
        zvezda = unichr(0x7a) + unichr(0x76) + unichr(0x7a) + unichr(0x64)
        print '(star)' + star + ' vs ' + zvezda + '(zvezda)'
        actualStarZvezda = Engine.Engine.findMatch(star, zvezda)
        self.assertEqual(2, actualStarZvezda, "msg")
        