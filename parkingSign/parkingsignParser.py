# Generated from parkingsign.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,85,8,1,1,2,3,2,88,8,2,1,2,1,2,1,2,1,2,1,3,3,3,95,
        8,3,1,3,1,3,3,3,99,8,3,1,3,3,3,102,8,3,1,3,3,3,105,8,3,1,4,3,4,108,
        8,4,1,4,1,4,3,4,112,8,4,1,4,4,4,115,8,4,11,4,12,4,116,1,4,3,4,120,
        8,4,1,4,3,4,123,8,4,1,5,3,5,126,8,5,1,5,1,5,4,5,130,8,5,11,5,12,
        5,131,1,5,3,5,135,8,5,1,5,3,5,138,8,5,1,6,1,6,1,6,1,6,1,6,3,6,145,
        8,6,1,6,3,6,148,8,6,1,6,3,6,151,8,6,1,7,1,7,1,7,1,7,3,7,157,8,7,
        1,7,1,7,1,7,3,7,162,8,7,1,7,3,7,165,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,180,8,8,1,9,1,9,3,9,184,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,3,16,220,8,16,1,17,1,17,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,241,8,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,
        3,24,251,8,24,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,3,27,
        262,8,27,1,28,1,28,1,29,1,29,1,29,3,29,269,8,29,1,29,1,29,3,29,273,
        8,29,1,29,1,29,3,29,277,8,29,1,30,1,30,1,30,3,30,282,8,30,1,31,1,
        31,1,31,3,31,287,8,31,1,32,1,32,3,32,291,8,32,1,33,1,33,3,33,295,
        8,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,7,1,0,48,49,1,
        0,16,17,1,0,9,11,1,0,21,22,1,0,35,36,1,0,32,33,1,0,40,46,310,0,71,
        1,0,0,0,2,84,1,0,0,0,4,87,1,0,0,0,6,94,1,0,0,0,8,107,1,0,0,0,10,
        125,1,0,0,0,12,139,1,0,0,0,14,156,1,0,0,0,16,166,1,0,0,0,18,183,
        1,0,0,0,20,191,1,0,0,0,22,194,1,0,0,0,24,197,1,0,0,0,26,200,1,0,
        0,0,28,204,1,0,0,0,30,208,1,0,0,0,32,219,1,0,0,0,34,221,1,0,0,0,
        36,223,1,0,0,0,38,227,1,0,0,0,40,240,1,0,0,0,42,242,1,0,0,0,44,244,
        1,0,0,0,46,246,1,0,0,0,48,248,1,0,0,0,50,254,1,0,0,0,52,256,1,0,
        0,0,54,261,1,0,0,0,56,263,1,0,0,0,58,276,1,0,0,0,60,281,1,0,0,0,
        62,286,1,0,0,0,64,290,1,0,0,0,66,294,1,0,0,0,68,70,3,2,1,0,69,68,
        1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,
        73,71,1,0,0,0,74,75,5,0,0,1,75,1,1,0,0,0,76,85,3,4,2,0,77,85,3,6,
        3,0,78,85,3,8,4,0,79,85,3,10,5,0,80,85,3,14,7,0,81,85,3,16,8,0,82,
        85,3,12,6,0,83,85,3,18,9,0,84,76,1,0,0,0,84,77,1,0,0,0,84,78,1,0,
        0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,
        1,0,0,0,85,3,1,0,0,0,86,88,3,22,11,0,87,86,1,0,0,0,87,88,1,0,0,0,
        88,89,1,0,0,0,89,90,3,32,16,0,90,91,3,56,28,0,91,92,3,20,10,0,92,
        5,1,0,0,0,93,95,3,22,11,0,94,93,1,0,0,0,94,95,1,0,0,0,95,98,1,0,
        0,0,96,99,3,54,27,0,97,99,3,32,16,0,98,96,1,0,0,0,98,97,1,0,0,0,
        99,101,1,0,0,0,100,102,5,15,0,0,101,100,1,0,0,0,101,102,1,0,0,0,
        102,104,1,0,0,0,103,105,3,40,20,0,104,103,1,0,0,0,104,105,1,0,0,
        0,105,7,1,0,0,0,106,108,3,48,24,0,107,106,1,0,0,0,107,108,1,0,0,
        0,108,111,1,0,0,0,109,112,3,24,12,0,110,112,3,26,13,0,111,109,1,
        0,0,0,111,110,1,0,0,0,112,114,1,0,0,0,113,115,3,32,16,0,114,113,
        1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,
        1,0,0,0,118,120,5,15,0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,122,
        1,0,0,0,121,123,3,40,20,0,122,121,1,0,0,0,122,123,1,0,0,0,123,9,
        1,0,0,0,124,126,3,48,24,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,
        1,0,0,0,127,129,3,28,14,0,128,130,3,32,16,0,129,128,1,0,0,0,130,
        131,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,
        135,5,15,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,
        138,3,40,20,0,137,136,1,0,0,0,137,138,1,0,0,0,138,11,1,0,0,0,139,
        140,3,48,24,0,140,141,5,37,0,0,141,144,3,22,11,0,142,145,3,54,27,
        0,143,145,3,32,16,0,144,142,1,0,0,0,144,143,1,0,0,0,145,147,1,0,
        0,0,146,148,5,15,0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,150,1,0,
        0,0,149,151,3,40,20,0,150,149,1,0,0,0,150,151,1,0,0,0,151,13,1,0,
        0,0,152,153,5,52,0,0,153,157,5,34,0,0,154,155,5,52,0,0,155,157,3,
        50,25,0,156,152,1,0,0,0,156,154,1,0,0,0,157,158,1,0,0,0,158,159,
        5,8,0,0,159,161,3,32,16,0,160,162,5,15,0,0,161,160,1,0,0,0,161,162,
        1,0,0,0,162,164,1,0,0,0,163,165,3,40,20,0,164,163,1,0,0,0,164,165,
        1,0,0,0,165,15,1,0,0,0,166,167,5,52,0,0,167,168,5,34,0,0,168,169,
        5,8,0,0,169,170,3,40,20,0,170,171,3,40,20,0,171,172,3,58,29,0,172,
        173,3,58,29,0,173,174,5,9,0,0,174,175,5,9,0,0,175,176,3,58,29,0,
        176,179,3,58,29,0,177,178,5,15,0,0,178,180,5,20,0,0,179,177,1,0,
        0,0,179,180,1,0,0,0,180,17,1,0,0,0,181,182,5,28,0,0,182,184,5,29,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,186,5,30,
        0,0,186,187,5,7,0,0,187,188,5,52,0,0,188,189,5,31,0,0,189,190,3,
        52,26,0,190,19,1,0,0,0,191,192,5,47,0,0,192,193,7,0,0,0,193,21,1,
        0,0,0,194,195,5,7,0,0,195,196,5,8,0,0,196,23,1,0,0,0,197,198,5,7,
        0,0,198,199,5,25,0,0,199,25,1,0,0,0,200,201,5,26,0,0,201,202,5,8,
        0,0,202,203,5,27,0,0,203,27,1,0,0,0,204,205,5,38,0,0,205,206,5,39,
        0,0,206,207,5,27,0,0,207,29,1,0,0,0,208,209,5,18,0,0,209,210,5,19,
        0,0,210,31,1,0,0,0,211,212,3,58,29,0,212,213,3,44,22,0,213,214,3,
        58,29,0,214,220,1,0,0,0,215,216,5,52,0,0,216,217,3,44,22,0,217,218,
        3,58,29,0,218,220,1,0,0,0,219,211,1,0,0,0,219,215,1,0,0,0,220,33,
        1,0,0,0,221,222,7,1,0,0,222,35,1,0,0,0,223,224,3,56,28,0,224,225,
        3,44,22,0,225,226,3,56,28,0,226,37,1,0,0,0,227,228,3,56,28,0,228,
        229,3,46,23,0,229,230,3,56,28,0,230,39,1,0,0,0,231,241,3,34,17,0,
        232,241,3,30,15,0,233,241,5,20,0,0,234,241,3,38,19,0,235,241,3,36,
        18,0,236,237,3,56,28,0,237,238,5,27,0,0,238,241,1,0,0,0,239,241,
        3,56,28,0,240,231,1,0,0,0,240,232,1,0,0,0,240,233,1,0,0,0,240,234,
        1,0,0,0,240,235,1,0,0,0,240,236,1,0,0,0,240,239,1,0,0,0,241,41,1,
        0,0,0,242,243,3,40,20,0,243,43,1,0,0,0,244,245,7,2,0,0,245,45,1,
        0,0,0,246,247,7,3,0,0,247,47,1,0,0,0,248,250,5,23,0,0,249,251,5,
        11,0,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,1,0,0,0,252,253,5,
        24,0,0,253,49,1,0,0,0,254,255,7,4,0,0,255,51,1,0,0,0,256,257,7,5,
        0,0,257,53,1,0,0,0,258,262,5,12,0,0,259,260,5,13,0,0,260,262,5,14,
        0,0,261,258,1,0,0,0,261,259,1,0,0,0,262,55,1,0,0,0,263,264,7,6,0,
        0,264,57,1,0,0,0,265,268,5,52,0,0,266,267,5,1,0,0,267,269,5,52,0,
        0,268,266,1,0,0,0,268,269,1,0,0,0,269,272,1,0,0,0,270,273,3,64,32,
        0,271,273,3,66,33,0,272,270,1,0,0,0,272,271,1,0,0,0,272,273,1,0,
        0,0,273,277,1,0,0,0,274,277,3,60,30,0,275,277,3,62,31,0,276,265,
        1,0,0,0,276,274,1,0,0,0,276,275,1,0,0,0,277,59,1,0,0,0,278,282,5,
        50,0,0,279,280,5,2,0,0,280,282,5,50,0,0,281,278,1,0,0,0,281,279,
        1,0,0,0,282,61,1,0,0,0,283,287,5,51,0,0,284,285,5,2,0,0,285,287,
        5,51,0,0,286,283,1,0,0,0,286,284,1,0,0,0,287,63,1,0,0,0,288,291,
        5,3,0,0,289,291,5,4,0,0,290,288,1,0,0,0,290,289,1,0,0,0,291,65,1,
        0,0,0,292,295,5,5,0,0,293,295,5,6,0,0,294,292,1,0,0,0,294,293,1,
        0,0,0,295,67,1,0,0,0,35,71,84,87,94,98,101,104,107,111,116,119,122,
        125,131,134,137,144,147,150,156,161,164,179,183,219,240,250,261,
        268,272,276,281,286,290,294
    ]

class parkingsignParser ( Parser ):

    grammarFileName = "parkingsign.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'12'", "'AM'", "'A.M.'", "'PM'", 
                     "'P.M.'", "'NO'", "'PARKING'", "'TO'", "'THRU'", "'-'", 
                     "'ANYTIME'", "'ANY'", "'TIME'", "'EXCEPT'", "'DAILY'", 
                     "'NIGHTLY'", "'SCHOOL'", "'DAYS'", "'HOLIDAYS'", "'AND'", 
                     "'&'", "'TOW'", "'AWAY'", "'STOPPING'", "'VALET'", 
                     "'ONLY'", "'VEHICLES'", "'WITH'", "'DISTRICT'", "'PERMITS'", 
                     "'EXEMPTED'", "'EXEMPT'", "'HOUR'", "'MINUTE'", "'MIN'", 
                     "'TEMPORARY'", "'PASSENGER'", "'LOADING'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'STREET'", "'SWEEPING'", 
                     "'CLEANING'", "'NOON'", "'MIDNIGHT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NO", "PARKING", 
                      "TO", "THRU", "DASH", "ANYTIME", "ANY", "TIME", "EXCEPT", 
                      "DAILY", "NIGHTLY", "SCHOOL", "DAYS", "HOLIDAYS", 
                      "AND", "AMPERSAND", "TOW", "AWAY", "STOPPING", "VALET", 
                      "ONLY", "VEHICLES", "WITH", "DISTRICT", "PERMITS", 
                      "EXEMPTED", "EXEMPT", "HOUR", "MINUTE", "MIN", "TEMPORARY", 
                      "PASSENGER", "LOADING", "MON", "TUE", "WED", "THU", 
                      "FRI", "SAT", "SUN", "STREET", "SWEEPING", "CLEANING", 
                      "NOON", "MIDNIGHT", "INT", "WS" ]

    RULE_parkingSigns = 0
    RULE_parkingSign = 1
    RULE_streetSweepingSign = 2
    RULE_noParkingSign = 3
    RULE_noStoppingSign = 4
    RULE_passengerLoadingSign = 5
    RULE_temporaryNoParkingSign = 6
    RULE_singleTimeLimitSign = 7
    RULE_doubleTimeLimitSign = 8
    RULE_permitSign = 9
    RULE_streetSweeping = 10
    RULE_noParking = 11
    RULE_noStopping = 12
    RULE_valetOnly = 13
    RULE_loadingOnly = 14
    RULE_schoolDays = 15
    RULE_timeRange = 16
    RULE_everyDay = 17
    RULE_dayToDay = 18
    RULE_dayAndDay = 19
    RULE_dayRange = 20
    RULE_dayRangePlus = 21
    RULE_to = 22
    RULE_and_ = 23
    RULE_towAway = 24
    RULE_minute = 25
    RULE_exempt = 26
    RULE_anyTime = 27
    RULE_day = 28
    RULE_time = 29
    RULE_twelveNoon = 30
    RULE_twelveMidnight = 31
    RULE_am = 32
    RULE_pm = 33

    ruleNames =  [ "parkingSigns", "parkingSign", "streetSweepingSign", 
                   "noParkingSign", "noStoppingSign", "passengerLoadingSign", 
                   "temporaryNoParkingSign", "singleTimeLimitSign", "doubleTimeLimitSign", 
                   "permitSign", "streetSweeping", "noParking", "noStopping", 
                   "valetOnly", "loadingOnly", "schoolDays", "timeRange", 
                   "everyDay", "dayToDay", "dayAndDay", "dayRange", "dayRangePlus", 
                   "to", "and_", "towAway", "minute", "exempt", "anyTime", 
                   "day", "time", "twelveNoon", "twelveMidnight", "am", 
                   "pm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NO=7
    PARKING=8
    TO=9
    THRU=10
    DASH=11
    ANYTIME=12
    ANY=13
    TIME=14
    EXCEPT=15
    DAILY=16
    NIGHTLY=17
    SCHOOL=18
    DAYS=19
    HOLIDAYS=20
    AND=21
    AMPERSAND=22
    TOW=23
    AWAY=24
    STOPPING=25
    VALET=26
    ONLY=27
    VEHICLES=28
    WITH=29
    DISTRICT=30
    PERMITS=31
    EXEMPTED=32
    EXEMPT=33
    HOUR=34
    MINUTE=35
    MIN=36
    TEMPORARY=37
    PASSENGER=38
    LOADING=39
    MON=40
    TUE=41
    WED=42
    THU=43
    FRI=44
    SAT=45
    SUN=46
    STREET=47
    SWEEPING=48
    CLEANING=49
    NOON=50
    MIDNIGHT=51
    INT=52
    WS=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParkingSignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(parkingsignParser.EOF, 0)

        def parkingSign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.ParkingSignContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.ParkingSignContext,i)


        def getRuleIndex(self):
            return parkingsignParser.RULE_parkingSigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParkingSigns" ):
                listener.enterParkingSigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParkingSigns" ):
                listener.exitParkingSigns(self)




    def parkingSigns(self):

        localctx = parkingsignParser.ParkingSignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parkingSigns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7881575643492484) != 0):
                self.state = 68
                self.parkingSign()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(parkingsignParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParkingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def streetSweepingSign(self):
            return self.getTypedRuleContext(parkingsignParser.StreetSweepingSignContext,0)


        def noParkingSign(self):
            return self.getTypedRuleContext(parkingsignParser.NoParkingSignContext,0)


        def noStoppingSign(self):
            return self.getTypedRuleContext(parkingsignParser.NoStoppingSignContext,0)


        def passengerLoadingSign(self):
            return self.getTypedRuleContext(parkingsignParser.PassengerLoadingSignContext,0)


        def singleTimeLimitSign(self):
            return self.getTypedRuleContext(parkingsignParser.SingleTimeLimitSignContext,0)


        def doubleTimeLimitSign(self):
            return self.getTypedRuleContext(parkingsignParser.DoubleTimeLimitSignContext,0)


        def temporaryNoParkingSign(self):
            return self.getTypedRuleContext(parkingsignParser.TemporaryNoParkingSignContext,0)


        def permitSign(self):
            return self.getTypedRuleContext(parkingsignParser.PermitSignContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_parkingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParkingSign" ):
                listener.enterParkingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParkingSign" ):
                listener.exitParkingSign(self)




    def parkingSign(self):

        localctx = parkingsignParser.ParkingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_parkingSign)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.streetSweepingSign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.noParkingSign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.noStoppingSign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.passengerLoadingSign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.singleTimeLimitSign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.doubleTimeLimitSign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.temporaryNoParkingSign()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.permitSign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StreetSweepingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def timeRange(self):
            return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,0)


        def day(self):
            return self.getTypedRuleContext(parkingsignParser.DayContext,0)


        def streetSweeping(self):
            return self.getTypedRuleContext(parkingsignParser.StreetSweepingContext,0)


        def noParking(self):
            return self.getTypedRuleContext(parkingsignParser.NoParkingContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_streetSweepingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStreetSweepingSign" ):
                listener.enterStreetSweepingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStreetSweepingSign" ):
                listener.exitStreetSweepingSign(self)




    def streetSweepingSign(self):

        localctx = parkingsignParser.StreetSweepingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_streetSweepingSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 86
                self.noParking()


            self.state = 89
            self.timeRange()
            self.state = 90
            self.day()
            self.state = 91
            self.streetSweeping()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoParkingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anyTime(self):
            return self.getTypedRuleContext(parkingsignParser.AnyTimeContext,0)


        def timeRange(self):
            return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,0)


        def noParking(self):
            return self.getTypedRuleContext(parkingsignParser.NoParkingContext,0)


        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_noParkingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoParkingSign" ):
                listener.enterNoParkingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoParkingSign" ):
                listener.exitNoParkingSign(self)




    def noParkingSign(self):

        localctx = parkingsignParser.NoParkingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_noParkingSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 93
                self.noParking()


            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13]:
                self.state = 96
                self.anyTime()
                pass
            elif token in [2, 50, 51, 52]:
                self.state = 97
                self.timeRange()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 100
                self.match(parkingsignParser.EXCEPT)


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 139637978234880) != 0):
                self.state = 103
                self.dayRange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoStoppingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noStopping(self):
            return self.getTypedRuleContext(parkingsignParser.NoStoppingContext,0)


        def valetOnly(self):
            return self.getTypedRuleContext(parkingsignParser.ValetOnlyContext,0)


        def towAway(self):
            return self.getTypedRuleContext(parkingsignParser.TowAwayContext,0)


        def timeRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.TimeRangeContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,i)


        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_noStoppingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoStoppingSign" ):
                listener.enterNoStoppingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoStoppingSign" ):
                listener.exitNoStoppingSign(self)




    def noStoppingSign(self):

        localctx = parkingsignParser.NoStoppingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_noStoppingSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 106
                self.towAway()


            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 109
                self.noStopping()
                pass
            elif token in [26]:
                self.state = 110
                self.valetOnly()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 114 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self.timeRange()

                else:
                    raise NoViableAltException(self)
                self.state = 116 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 118
                self.match(parkingsignParser.EXCEPT)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 139637978234880) != 0):
                self.state = 121
                self.dayRange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassengerLoadingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadingOnly(self):
            return self.getTypedRuleContext(parkingsignParser.LoadingOnlyContext,0)


        def towAway(self):
            return self.getTypedRuleContext(parkingsignParser.TowAwayContext,0)


        def timeRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.TimeRangeContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,i)


        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_passengerLoadingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassengerLoadingSign" ):
                listener.enterPassengerLoadingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassengerLoadingSign" ):
                listener.exitPassengerLoadingSign(self)




    def passengerLoadingSign(self):

        localctx = parkingsignParser.PassengerLoadingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_passengerLoadingSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 124
                self.towAway()


            self.state = 127
            self.loadingOnly()
            self.state = 129 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 128
                    self.timeRange()

                else:
                    raise NoViableAltException(self)
                self.state = 131 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 133
                self.match(parkingsignParser.EXCEPT)


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 139637978234880) != 0):
                self.state = 136
                self.dayRange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemporaryNoParkingSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def towAway(self):
            return self.getTypedRuleContext(parkingsignParser.TowAwayContext,0)


        def TEMPORARY(self):
            return self.getToken(parkingsignParser.TEMPORARY, 0)

        def noParking(self):
            return self.getTypedRuleContext(parkingsignParser.NoParkingContext,0)


        def anyTime(self):
            return self.getTypedRuleContext(parkingsignParser.AnyTimeContext,0)


        def timeRange(self):
            return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,0)


        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_temporaryNoParkingSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemporaryNoParkingSign" ):
                listener.enterTemporaryNoParkingSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemporaryNoParkingSign" ):
                listener.exitTemporaryNoParkingSign(self)




    def temporaryNoParkingSign(self):

        localctx = parkingsignParser.TemporaryNoParkingSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_temporaryNoParkingSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.towAway()
            self.state = 140
            self.match(parkingsignParser.TEMPORARY)
            self.state = 141
            self.noParking()
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13]:
                self.state = 142
                self.anyTime()
                pass
            elif token in [2, 50, 51, 52]:
                self.state = 143
                self.timeRange()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 146
                self.match(parkingsignParser.EXCEPT)


            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 139637978234880) != 0):
                self.state = 149
                self.dayRange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTimeLimitSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARKING(self):
            return self.getToken(parkingsignParser.PARKING, 0)

        def timeRange(self):
            return self.getTypedRuleContext(parkingsignParser.TimeRangeContext,0)


        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def INT(self):
            return self.getToken(parkingsignParser.INT, 0)

        def HOUR(self):
            return self.getToken(parkingsignParser.HOUR, 0)

        def minute(self):
            return self.getTypedRuleContext(parkingsignParser.MinuteContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_singleTimeLimitSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTimeLimitSign" ):
                listener.enterSingleTimeLimitSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTimeLimitSign" ):
                listener.exitSingleTimeLimitSign(self)




    def singleTimeLimitSign(self):

        localctx = parkingsignParser.SingleTimeLimitSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleTimeLimitSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 152
                self.match(parkingsignParser.INT)
                self.state = 153
                self.match(parkingsignParser.HOUR)
                pass

            elif la_ == 2:
                self.state = 154
                self.match(parkingsignParser.INT)
                self.state = 155
                self.minute()
                pass


            self.state = 158
            self.match(parkingsignParser.PARKING)
            self.state = 159
            self.timeRange()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 160
                self.match(parkingsignParser.EXCEPT)


            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 139637978234880) != 0):
                self.state = 163
                self.dayRange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleTimeLimitSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(parkingsignParser.INT, 0)

        def HOUR(self):
            return self.getToken(parkingsignParser.HOUR, 0)

        def PARKING(self):
            return self.getToken(parkingsignParser.PARKING, 0)

        def dayRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.DayRangeContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.DayRangeContext,i)


        def time(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.TimeContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.TimeContext,i)


        def TO(self, i:int=None):
            if i is None:
                return self.getTokens(parkingsignParser.TO)
            else:
                return self.getToken(parkingsignParser.TO, i)

        def EXCEPT(self):
            return self.getToken(parkingsignParser.EXCEPT, 0)

        def HOLIDAYS(self):
            return self.getToken(parkingsignParser.HOLIDAYS, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_doubleTimeLimitSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleTimeLimitSign" ):
                listener.enterDoubleTimeLimitSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleTimeLimitSign" ):
                listener.exitDoubleTimeLimitSign(self)




    def doubleTimeLimitSign(self):

        localctx = parkingsignParser.DoubleTimeLimitSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_doubleTimeLimitSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(parkingsignParser.INT)
            self.state = 167
            self.match(parkingsignParser.HOUR)
            self.state = 168
            self.match(parkingsignParser.PARKING)
            self.state = 169
            self.dayRange()
            self.state = 170
            self.dayRange()
            self.state = 171
            self.time()
            self.state = 172
            self.time()
            self.state = 173
            self.match(parkingsignParser.TO)
            self.state = 174
            self.match(parkingsignParser.TO)
            self.state = 175
            self.time()
            self.state = 176
            self.time()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 177
                self.match(parkingsignParser.EXCEPT)
                self.state = 178
                self.match(parkingsignParser.HOLIDAYS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PermitSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISTRICT(self):
            return self.getToken(parkingsignParser.DISTRICT, 0)

        def NO(self):
            return self.getToken(parkingsignParser.NO, 0)

        def INT(self):
            return self.getToken(parkingsignParser.INT, 0)

        def PERMITS(self):
            return self.getToken(parkingsignParser.PERMITS, 0)

        def exempt(self):
            return self.getTypedRuleContext(parkingsignParser.ExemptContext,0)


        def VEHICLES(self):
            return self.getToken(parkingsignParser.VEHICLES, 0)

        def WITH(self):
            return self.getToken(parkingsignParser.WITH, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_permitSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermitSign" ):
                listener.enterPermitSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermitSign" ):
                listener.exitPermitSign(self)




    def permitSign(self):

        localctx = parkingsignParser.PermitSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_permitSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 181
                self.match(parkingsignParser.VEHICLES)
                self.state = 182
                self.match(parkingsignParser.WITH)


            self.state = 185
            self.match(parkingsignParser.DISTRICT)
            self.state = 186
            self.match(parkingsignParser.NO)
            self.state = 187
            self.match(parkingsignParser.INT)
            self.state = 188
            self.match(parkingsignParser.PERMITS)
            self.state = 189
            self.exempt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StreetSweepingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STREET(self):
            return self.getToken(parkingsignParser.STREET, 0)

        def SWEEPING(self):
            return self.getToken(parkingsignParser.SWEEPING, 0)

        def CLEANING(self):
            return self.getToken(parkingsignParser.CLEANING, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_streetSweeping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStreetSweeping" ):
                listener.enterStreetSweeping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStreetSweeping" ):
                listener.exitStreetSweeping(self)




    def streetSweeping(self):

        localctx = parkingsignParser.StreetSweepingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_streetSweeping)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(parkingsignParser.STREET)
            self.state = 192
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoParkingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(parkingsignParser.NO, 0)

        def PARKING(self):
            return self.getToken(parkingsignParser.PARKING, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_noParking

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoParking" ):
                listener.enterNoParking(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoParking" ):
                listener.exitNoParking(self)




    def noParking(self):

        localctx = parkingsignParser.NoParkingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_noParking)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(parkingsignParser.NO)
            self.state = 195
            self.match(parkingsignParser.PARKING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoStoppingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(parkingsignParser.NO, 0)

        def STOPPING(self):
            return self.getToken(parkingsignParser.STOPPING, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_noStopping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoStopping" ):
                listener.enterNoStopping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoStopping" ):
                listener.exitNoStopping(self)




    def noStopping(self):

        localctx = parkingsignParser.NoStoppingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_noStopping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(parkingsignParser.NO)
            self.state = 198
            self.match(parkingsignParser.STOPPING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValetOnlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALET(self):
            return self.getToken(parkingsignParser.VALET, 0)

        def PARKING(self):
            return self.getToken(parkingsignParser.PARKING, 0)

        def ONLY(self):
            return self.getToken(parkingsignParser.ONLY, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_valetOnly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValetOnly" ):
                listener.enterValetOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValetOnly" ):
                listener.exitValetOnly(self)




    def valetOnly(self):

        localctx = parkingsignParser.ValetOnlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_valetOnly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(parkingsignParser.VALET)
            self.state = 201
            self.match(parkingsignParser.PARKING)
            self.state = 202
            self.match(parkingsignParser.ONLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadingOnlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASSENGER(self):
            return self.getToken(parkingsignParser.PASSENGER, 0)

        def LOADING(self):
            return self.getToken(parkingsignParser.LOADING, 0)

        def ONLY(self):
            return self.getToken(parkingsignParser.ONLY, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_loadingOnly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadingOnly" ):
                listener.enterLoadingOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadingOnly" ):
                listener.exitLoadingOnly(self)




    def loadingOnly(self):

        localctx = parkingsignParser.LoadingOnlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loadingOnly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(parkingsignParser.PASSENGER)
            self.state = 205
            self.match(parkingsignParser.LOADING)
            self.state = 206
            self.match(parkingsignParser.ONLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchoolDaysContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCHOOL(self):
            return self.getToken(parkingsignParser.SCHOOL, 0)

        def DAYS(self):
            return self.getToken(parkingsignParser.DAYS, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_schoolDays

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchoolDays" ):
                listener.enterSchoolDays(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchoolDays" ):
                listener.exitSchoolDays(self)




    def schoolDays(self):

        localctx = parkingsignParser.SchoolDaysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_schoolDays)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(parkingsignParser.SCHOOL)
            self.state = 209
            self.match(parkingsignParser.DAYS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def time(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.TimeContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.TimeContext,i)


        def to(self):
            return self.getTypedRuleContext(parkingsignParser.ToContext,0)


        def INT(self):
            return self.getToken(parkingsignParser.INT, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_timeRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeRange" ):
                listener.enterTimeRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeRange" ):
                listener.exitTimeRange(self)




    def timeRange(self):

        localctx = parkingsignParser.TimeRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_timeRange)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.time()
                self.state = 212
                self.to()
                self.state = 213
                self.time()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(parkingsignParser.INT)
                self.state = 216
                self.to()
                self.state = 217
                self.time()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EveryDayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DAILY(self):
            return self.getToken(parkingsignParser.DAILY, 0)

        def NIGHTLY(self):
            return self.getToken(parkingsignParser.NIGHTLY, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_everyDay

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEveryDay" ):
                listener.enterEveryDay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEveryDay" ):
                listener.exitEveryDay(self)




    def everyDay(self):

        localctx = parkingsignParser.EveryDayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_everyDay)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DayToDayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def day(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.DayContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.DayContext,i)


        def to(self):
            return self.getTypedRuleContext(parkingsignParser.ToContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_dayToDay

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDayToDay" ):
                listener.enterDayToDay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDayToDay" ):
                listener.exitDayToDay(self)




    def dayToDay(self):

        localctx = parkingsignParser.DayToDayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dayToDay)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.day()
            self.state = 224
            self.to()
            self.state = 225
            self.day()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DayAndDayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def day(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parkingsignParser.DayContext)
            else:
                return self.getTypedRuleContext(parkingsignParser.DayContext,i)


        def and_(self):
            return self.getTypedRuleContext(parkingsignParser.And_Context,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_dayAndDay

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDayAndDay" ):
                listener.enterDayAndDay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDayAndDay" ):
                listener.exitDayAndDay(self)




    def dayAndDay(self):

        localctx = parkingsignParser.DayAndDayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dayAndDay)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.day()
            self.state = 228
            self.and_()
            self.state = 229
            self.day()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DayRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def everyDay(self):
            return self.getTypedRuleContext(parkingsignParser.EveryDayContext,0)


        def schoolDays(self):
            return self.getTypedRuleContext(parkingsignParser.SchoolDaysContext,0)


        def HOLIDAYS(self):
            return self.getToken(parkingsignParser.HOLIDAYS, 0)

        def dayAndDay(self):
            return self.getTypedRuleContext(parkingsignParser.DayAndDayContext,0)


        def dayToDay(self):
            return self.getTypedRuleContext(parkingsignParser.DayToDayContext,0)


        def day(self):
            return self.getTypedRuleContext(parkingsignParser.DayContext,0)


        def ONLY(self):
            return self.getToken(parkingsignParser.ONLY, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_dayRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDayRange" ):
                listener.enterDayRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDayRange" ):
                listener.exitDayRange(self)




    def dayRange(self):

        localctx = parkingsignParser.DayRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dayRange)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.everyDay()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.schoolDays()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(parkingsignParser.HOLIDAYS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.dayAndDay()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
                self.dayToDay()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 236
                self.day()
                self.state = 237
                self.match(parkingsignParser.ONLY)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 239
                self.day()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DayRangePlusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dayRange(self):
            return self.getTypedRuleContext(parkingsignParser.DayRangeContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_dayRangePlus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDayRangePlus" ):
                listener.enterDayRangePlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDayRangePlus" ):
                listener.exitDayRangePlus(self)




    def dayRangePlus(self):

        localctx = parkingsignParser.DayRangePlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dayRangePlus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.dayRange()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(parkingsignParser.TO, 0)

        def DASH(self):
            return self.getToken(parkingsignParser.DASH, 0)

        def THRU(self):
            return self.getToken(parkingsignParser.THRU, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_to

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTo" ):
                listener.enterTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTo" ):
                listener.exitTo(self)




    def to(self):

        localctx = parkingsignParser.ToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_to)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(parkingsignParser.AND, 0)

        def AMPERSAND(self):
            return self.getToken(parkingsignParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_and_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_" ):
                listener.enterAnd_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_" ):
                listener.exitAnd_(self)




    def and_(self):

        localctx = parkingsignParser.And_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_and_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TowAwayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOW(self):
            return self.getToken(parkingsignParser.TOW, 0)

        def AWAY(self):
            return self.getToken(parkingsignParser.AWAY, 0)

        def DASH(self):
            return self.getToken(parkingsignParser.DASH, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_towAway

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTowAway" ):
                listener.enterTowAway(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTowAway" ):
                listener.exitTowAway(self)




    def towAway(self):

        localctx = parkingsignParser.TowAwayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_towAway)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(parkingsignParser.TOW)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 249
                self.match(parkingsignParser.DASH)


            self.state = 252
            self.match(parkingsignParser.AWAY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinuteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIN(self):
            return self.getToken(parkingsignParser.MIN, 0)

        def MINUTE(self):
            return self.getToken(parkingsignParser.MINUTE, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_minute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinute" ):
                listener.enterMinute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinute" ):
                listener.exitMinute(self)




    def minute(self):

        localctx = parkingsignParser.MinuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_minute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExemptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXEMPT(self):
            return self.getToken(parkingsignParser.EXEMPT, 0)

        def EXEMPTED(self):
            return self.getToken(parkingsignParser.EXEMPTED, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_exempt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExempt" ):
                listener.enterExempt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExempt" ):
                listener.exitExempt(self)




    def exempt(self):

        localctx = parkingsignParser.ExemptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exempt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnyTimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANYTIME(self):
            return self.getToken(parkingsignParser.ANYTIME, 0)

        def ANY(self):
            return self.getToken(parkingsignParser.ANY, 0)

        def TIME(self):
            return self.getToken(parkingsignParser.TIME, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_anyTime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnyTime" ):
                listener.enterAnyTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnyTime" ):
                listener.exitAnyTime(self)




    def anyTime(self):

        localctx = parkingsignParser.AnyTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_anyTime)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(parkingsignParser.ANYTIME)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(parkingsignParser.ANY)
                self.state = 260
                self.match(parkingsignParser.TIME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MON(self):
            return self.getToken(parkingsignParser.MON, 0)

        def TUE(self):
            return self.getToken(parkingsignParser.TUE, 0)

        def WED(self):
            return self.getToken(parkingsignParser.WED, 0)

        def THU(self):
            return self.getToken(parkingsignParser.THU, 0)

        def FRI(self):
            return self.getToken(parkingsignParser.FRI, 0)

        def SAT(self):
            return self.getToken(parkingsignParser.SAT, 0)

        def SUN(self):
            return self.getToken(parkingsignParser.SUN, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_day

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDay" ):
                listener.enterDay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDay" ):
                listener.exitDay(self)




    def day(self):

        localctx = parkingsignParser.DayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_day)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 139637976727552) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(parkingsignParser.INT)
            else:
                return self.getToken(parkingsignParser.INT, i)

        def am(self):
            return self.getTypedRuleContext(parkingsignParser.AmContext,0)


        def pm(self):
            return self.getTypedRuleContext(parkingsignParser.PmContext,0)


        def twelveNoon(self):
            return self.getTypedRuleContext(parkingsignParser.TwelveNoonContext,0)


        def twelveMidnight(self):
            return self.getTypedRuleContext(parkingsignParser.TwelveMidnightContext,0)


        def getRuleIndex(self):
            return parkingsignParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = parkingsignParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(parkingsignParser.INT)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 266
                    self.match(parkingsignParser.T__0)
                    self.state = 267
                    self.match(parkingsignParser.INT)


                self.state = 272
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4]:
                    self.state = 270
                    self.am()
                    pass
                elif token in [5, 6]:
                    self.state = 271
                    self.pm()
                    pass
                elif token in [-1, 2, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 23, 26, 28, 30, 38, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.twelveNoon()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.twelveMidnight()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TwelveNoonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOON(self):
            return self.getToken(parkingsignParser.NOON, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_twelveNoon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTwelveNoon" ):
                listener.enterTwelveNoon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTwelveNoon" ):
                listener.exitTwelveNoon(self)




    def twelveNoon(self):

        localctx = parkingsignParser.TwelveNoonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_twelveNoon)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(parkingsignParser.NOON)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(parkingsignParser.T__1)
                self.state = 280
                self.match(parkingsignParser.NOON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TwelveMidnightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIDNIGHT(self):
            return self.getToken(parkingsignParser.MIDNIGHT, 0)

        def getRuleIndex(self):
            return parkingsignParser.RULE_twelveMidnight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTwelveMidnight" ):
                listener.enterTwelveMidnight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTwelveMidnight" ):
                listener.exitTwelveMidnight(self)




    def twelveMidnight(self):

        localctx = parkingsignParser.TwelveMidnightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_twelveMidnight)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(parkingsignParser.MIDNIGHT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(parkingsignParser.T__1)
                self.state = 285
                self.match(parkingsignParser.MIDNIGHT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parkingsignParser.RULE_am

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAm" ):
                listener.enterAm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAm" ):
                listener.exitAm(self)




    def am(self):

        localctx = parkingsignParser.AmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_am)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(parkingsignParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(parkingsignParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parkingsignParser.RULE_pm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPm" ):
                listener.enterPm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPm" ):
                listener.exitPm(self)




    def pm(self):

        localctx = parkingsignParser.PmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_pm)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(parkingsignParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(parkingsignParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





