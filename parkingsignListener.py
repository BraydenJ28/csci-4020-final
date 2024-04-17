# Generated from parkingsign.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .parkingsignParser import parkingsignParser
else:
    from parkingsignParser import parkingsignParser

# This class defines a complete listener for a parse tree produced by parkingsignParser.
class parkingsignListener(ParseTreeListener):

    # Enter a parse tree produced by parkingsignParser#parkingSigns.
    def enterParkingSigns(self, ctx:parkingsignParser.ParkingSignsContext):
        pass

    # Exit a parse tree produced by parkingsignParser#parkingSigns.
    def exitParkingSigns(self, ctx:parkingsignParser.ParkingSignsContext):
        pass


    # Enter a parse tree produced by parkingsignParser#parkingSign.
    def enterParkingSign(self, ctx:parkingsignParser.ParkingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#parkingSign.
    def exitParkingSign(self, ctx:parkingsignParser.ParkingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#streetSweepingSign.
    def enterStreetSweepingSign(self, ctx:parkingsignParser.StreetSweepingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#streetSweepingSign.
    def exitStreetSweepingSign(self, ctx:parkingsignParser.StreetSweepingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#noParkingSign.
    def enterNoParkingSign(self, ctx:parkingsignParser.NoParkingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#noParkingSign.
    def exitNoParkingSign(self, ctx:parkingsignParser.NoParkingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#noStoppingSign.
    def enterNoStoppingSign(self, ctx:parkingsignParser.NoStoppingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#noStoppingSign.
    def exitNoStoppingSign(self, ctx:parkingsignParser.NoStoppingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#passengerLoadingSign.
    def enterPassengerLoadingSign(self, ctx:parkingsignParser.PassengerLoadingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#passengerLoadingSign.
    def exitPassengerLoadingSign(self, ctx:parkingsignParser.PassengerLoadingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#temporaryNoParkingSign.
    def enterTemporaryNoParkingSign(self, ctx:parkingsignParser.TemporaryNoParkingSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#temporaryNoParkingSign.
    def exitTemporaryNoParkingSign(self, ctx:parkingsignParser.TemporaryNoParkingSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#singleTimeLimitSign.
    def enterSingleTimeLimitSign(self, ctx:parkingsignParser.SingleTimeLimitSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#singleTimeLimitSign.
    def exitSingleTimeLimitSign(self, ctx:parkingsignParser.SingleTimeLimitSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#doubleTimeLimitSign.
    def enterDoubleTimeLimitSign(self, ctx:parkingsignParser.DoubleTimeLimitSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#doubleTimeLimitSign.
    def exitDoubleTimeLimitSign(self, ctx:parkingsignParser.DoubleTimeLimitSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#permitSign.
    def enterPermitSign(self, ctx:parkingsignParser.PermitSignContext):
        pass

    # Exit a parse tree produced by parkingsignParser#permitSign.
    def exitPermitSign(self, ctx:parkingsignParser.PermitSignContext):
        pass


    # Enter a parse tree produced by parkingsignParser#streetSweeping.
    def enterStreetSweeping(self, ctx:parkingsignParser.StreetSweepingContext):
        pass

    # Exit a parse tree produced by parkingsignParser#streetSweeping.
    def exitStreetSweeping(self, ctx:parkingsignParser.StreetSweepingContext):
        pass


    # Enter a parse tree produced by parkingsignParser#noParking.
    def enterNoParking(self, ctx:parkingsignParser.NoParkingContext):
        pass

    # Exit a parse tree produced by parkingsignParser#noParking.
    def exitNoParking(self, ctx:parkingsignParser.NoParkingContext):
        pass


    # Enter a parse tree produced by parkingsignParser#noStopping.
    def enterNoStopping(self, ctx:parkingsignParser.NoStoppingContext):
        pass

    # Exit a parse tree produced by parkingsignParser#noStopping.
    def exitNoStopping(self, ctx:parkingsignParser.NoStoppingContext):
        pass


    # Enter a parse tree produced by parkingsignParser#valetOnly.
    def enterValetOnly(self, ctx:parkingsignParser.ValetOnlyContext):
        pass

    # Exit a parse tree produced by parkingsignParser#valetOnly.
    def exitValetOnly(self, ctx:parkingsignParser.ValetOnlyContext):
        pass


    # Enter a parse tree produced by parkingsignParser#loadingOnly.
    def enterLoadingOnly(self, ctx:parkingsignParser.LoadingOnlyContext):
        pass

    # Exit a parse tree produced by parkingsignParser#loadingOnly.
    def exitLoadingOnly(self, ctx:parkingsignParser.LoadingOnlyContext):
        pass


    # Enter a parse tree produced by parkingsignParser#schoolDays.
    def enterSchoolDays(self, ctx:parkingsignParser.SchoolDaysContext):
        pass

    # Exit a parse tree produced by parkingsignParser#schoolDays.
    def exitSchoolDays(self, ctx:parkingsignParser.SchoolDaysContext):
        pass


    # Enter a parse tree produced by parkingsignParser#timeRange.
    def enterTimeRange(self, ctx:parkingsignParser.TimeRangeContext):
        pass

    # Exit a parse tree produced by parkingsignParser#timeRange.
    def exitTimeRange(self, ctx:parkingsignParser.TimeRangeContext):
        pass


    # Enter a parse tree produced by parkingsignParser#everyDay.
    def enterEveryDay(self, ctx:parkingsignParser.EveryDayContext):
        pass

    # Exit a parse tree produced by parkingsignParser#everyDay.
    def exitEveryDay(self, ctx:parkingsignParser.EveryDayContext):
        pass


    # Enter a parse tree produced by parkingsignParser#dayToDay.
    def enterDayToDay(self, ctx:parkingsignParser.DayToDayContext):
        pass

    # Exit a parse tree produced by parkingsignParser#dayToDay.
    def exitDayToDay(self, ctx:parkingsignParser.DayToDayContext):
        pass


    # Enter a parse tree produced by parkingsignParser#dayAndDay.
    def enterDayAndDay(self, ctx:parkingsignParser.DayAndDayContext):
        pass

    # Exit a parse tree produced by parkingsignParser#dayAndDay.
    def exitDayAndDay(self, ctx:parkingsignParser.DayAndDayContext):
        pass


    # Enter a parse tree produced by parkingsignParser#dayRange.
    def enterDayRange(self, ctx:parkingsignParser.DayRangeContext):
        pass

    # Exit a parse tree produced by parkingsignParser#dayRange.
    def exitDayRange(self, ctx:parkingsignParser.DayRangeContext):
        pass


    # Enter a parse tree produced by parkingsignParser#dayRangePlus.
    def enterDayRangePlus(self, ctx:parkingsignParser.DayRangePlusContext):
        pass

    # Exit a parse tree produced by parkingsignParser#dayRangePlus.
    def exitDayRangePlus(self, ctx:parkingsignParser.DayRangePlusContext):
        pass


    # Enter a parse tree produced by parkingsignParser#to.
    def enterTo(self, ctx:parkingsignParser.ToContext):
        pass

    # Exit a parse tree produced by parkingsignParser#to.
    def exitTo(self, ctx:parkingsignParser.ToContext):
        pass


    # Enter a parse tree produced by parkingsignParser#and_.
    def enterAnd_(self, ctx:parkingsignParser.And_Context):
        pass

    # Exit a parse tree produced by parkingsignParser#and_.
    def exitAnd_(self, ctx:parkingsignParser.And_Context):
        pass


    # Enter a parse tree produced by parkingsignParser#towAway.
    def enterTowAway(self, ctx:parkingsignParser.TowAwayContext):
        pass

    # Exit a parse tree produced by parkingsignParser#towAway.
    def exitTowAway(self, ctx:parkingsignParser.TowAwayContext):
        pass


    # Enter a parse tree produced by parkingsignParser#minute.
    def enterMinute(self, ctx:parkingsignParser.MinuteContext):
        pass

    # Exit a parse tree produced by parkingsignParser#minute.
    def exitMinute(self, ctx:parkingsignParser.MinuteContext):
        pass


    # Enter a parse tree produced by parkingsignParser#exempt.
    def enterExempt(self, ctx:parkingsignParser.ExemptContext):
        pass

    # Exit a parse tree produced by parkingsignParser#exempt.
    def exitExempt(self, ctx:parkingsignParser.ExemptContext):
        pass


    # Enter a parse tree produced by parkingsignParser#anyTime.
    def enterAnyTime(self, ctx:parkingsignParser.AnyTimeContext):
        pass

    # Exit a parse tree produced by parkingsignParser#anyTime.
    def exitAnyTime(self, ctx:parkingsignParser.AnyTimeContext):
        pass


    # Enter a parse tree produced by parkingsignParser#day.
    def enterDay(self, ctx:parkingsignParser.DayContext):
        pass

    # Exit a parse tree produced by parkingsignParser#day.
    def exitDay(self, ctx:parkingsignParser.DayContext):
        pass


    # Enter a parse tree produced by parkingsignParser#time.
    def enterTime(self, ctx:parkingsignParser.TimeContext):
        pass

    # Exit a parse tree produced by parkingsignParser#time.
    def exitTime(self, ctx:parkingsignParser.TimeContext):
        pass


    # Enter a parse tree produced by parkingsignParser#twelveNoon.
    def enterTwelveNoon(self, ctx:parkingsignParser.TwelveNoonContext):
        pass

    # Exit a parse tree produced by parkingsignParser#twelveNoon.
    def exitTwelveNoon(self, ctx:parkingsignParser.TwelveNoonContext):
        pass


    # Enter a parse tree produced by parkingsignParser#twelveMidnight.
    def enterTwelveMidnight(self, ctx:parkingsignParser.TwelveMidnightContext):
        pass

    # Exit a parse tree produced by parkingsignParser#twelveMidnight.
    def exitTwelveMidnight(self, ctx:parkingsignParser.TwelveMidnightContext):
        pass


    # Enter a parse tree produced by parkingsignParser#am.
    def enterAm(self, ctx:parkingsignParser.AmContext):
        pass

    # Exit a parse tree produced by parkingsignParser#am.
    def exitAm(self, ctx:parkingsignParser.AmContext):
        pass


    # Enter a parse tree produced by parkingsignParser#pm.
    def enterPm(self, ctx:parkingsignParser.PmContext):
        pass

    # Exit a parse tree produced by parkingsignParser#pm.
    def exitPm(self, ctx:parkingsignParser.PmContext):
        pass



del parkingsignParser