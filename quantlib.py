import QuantLib as ql
todaysDate = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = todaysDate
spotDates = [ql.Date(15, 1, 2015), ql.Date(15, 7, 2015), ql.Date(15, 1, 2016)]
spotRates = [0.0, 0.005, 0.007]
dayCount = ql.Thirty360()
calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Annual
spotCurve = ql.ZeroCurve(spotDates, spotRates, dayCount, calendar, interpolation,
                             compounding, compoundingFrequency)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)

print(spotCurveHandle.forwardRate(ql.Date(15, 1, 2015),ql.Date(15, 1, 2016),dayCount,compounding,compoundingFrequency))