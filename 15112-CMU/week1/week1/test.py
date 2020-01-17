# The following function is from this week's lecture notes
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def transformRGB(rgb1, rgb2, midpoints, n):
    blue1 = rgb1 % 10 ** 3
    green1 = (rgb1 // 10 ** 3) % (10 ** 3)
    red1 = (rgb1 // 10 ** 3) // 10 ** 3
    blue2 = rgb2 % 10 ** 3
    green2 = (rgb2 // 10 ** 3) % (10 ** 3)
    red2 = (rgb2 // 10 ** 3) // 10 ** 3
    equalblue = (blue1 - blue2) / (midpoints + 1)
    equalgreen = (green1 - green2) / (midpoints + 1)
    equalred = (red1 - red2) / (midpoints + 1)
    targetblue = roundHalfUp(blue1 - equalblue * n)
    targetgreen = roundHalfUp(green1 - equalgreen * n)
    targetred = roundHalfUp(red1 - equalred * n)

    if len(str(targetgreen)) == 1:
        targetgreen = "00" + str(targetgreen)
    elif len(str(targetgreen)) == 2:
        targetgreen = "0" + str(targetgreen)
    else:
        targetgreen = str(targetgreen)

    if len(str(targetblue)) == 1:
        targetblue = "00" + str(targetblue)
    elif len(str(targetblue)) == 2:
        targetblue = "0" + str(targetblue)
    else:
        targetblue = str(targetblue)

    targetred = str(targetred)
    return targetred + targetgreen + targetblue


def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > (midpoints+1):
        return None
    elif 0 <= n <= (midpoints + 1):
        return int(transformRGB(rgb1, rgb2, midpoints, n))


def testColorBlender():
    print("Testing colorBlender()...", end="")
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print("Passed.")

testColorBlender()




