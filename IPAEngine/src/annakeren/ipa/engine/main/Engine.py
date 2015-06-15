'''
Created on 31 May 2015

@author: annakeren
'''
if __name__ == '__main__':
    b={'B':['0x62','0x0253', '0x0299', '0x03B2']}
    c={'C':['0x63','0x0254', '0x0255', '0x00E7']}
    d={'D':['0x64','0x0257', '0x0256', '0x00F0', '0x02A4']}
    f={'F':['0x66','0x025F', '0x0284']}
    g={'G':['0x67','0x0261', '0x0260', '0x0262', '0x029B']}
    h={'H':['0x68','0x0266', '0x0267', '0x0127', '0x0265', '0x029C']}
    j={'J':['0x6a','0x029D', '0x026D', '0x026C', '0x026B', '0x026E']}
    k={'K':['0x6b']}
    l={'L':['0x6c','0x029F']}
    m={'M':['0x6d','0x0271', '0x026F', '0x0270']}
    n={'N':['0x6e','0x014B', '0x0273', '0x0272', '0x0274']}
    r={'R':['0x72','0x0279', '0x027A', '0x027E', '0x0280', '0x0281', '0x027D']}
    p={'P':['0x70']}
    s={'S':['0x73','0x5a','0x0282', '0x0283']}
    t={'T':['0x74','0x0288', '0x02A7']}
    v={'V':['0x76','0x028B', '0x2C71']}

#                     s           t            type of m           d
    stand = unichr(0x73)+unichr(0x74)+unichr(0x0271)+unichr(0x64)
#                     s           t            m            d
    stamb = unichr(0x73)+unichr(0x74)+unichr(0x6d)+unichr(0x62)
    foundCounter = 0
    for c in stamb:
        found = stand.find(c)
        if found > -1:
            foundCounter = foundCounter + 1
        else:
            for sound_group, sounds in m.iteritems():
                for sound in sounds:
                    found = stand.find(unichr(int(sound, 16)))
                    if found > -1:
                        foundCounter = foundCounter + 1
            
    stambLength = len(stamb)
    halfStambLength = stambLength/2
    if foundCounter >=halfStambLength:
        print 'high probability' 
        print foundCounter       
    
    pass