import math

def applyOptionPickedUpRaise(amount):
    return math.ceil(1.1 * amount)

def applyOneYearExtensionRaise(amount):
    raisedAmount = math.ceil(1.25 * amount)
    return max(5, raisedAmount)

def applyTwoYearExtensionRaise(amount):
    raisedAmount = math.ceil(1.5 * amount)
    return max(5, raisedAmount)