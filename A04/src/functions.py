"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports

# Constants


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    level = ""
    if aqi > 300:
        level += "Hazardous"
    elif aqi > 200:
        level += "Very Unhealthy"
    elif aqi > 150:
        level += "Unhealthy"
    elif aqi > 100:
        level += "Unhealthy for Sensitive Groups"
    elif aqi > 50:
        level += "Moderate"
    elif aqi >= 0:
        level += "Good"
    else:
        level += "Error"
    return level


def day_of_week(day_number):
    """
     -------------------------------------------------------
    Returns the day of the week in number (1,2,3...):
    Returns "Error" if day is 1<day>7.
    Use: day = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - Day of the Week (int)
    Returns:

    ------------------------------------------------------
    """
    day = ""
    if day_number == 1:
        day = day + "Monday"
    elif day_number == 2:
        day = day + "Tuesday"
    elif day_number == 3:
        day = day + "Wednesday"
    elif day_number == 4:
        day = day + "Thursday"
    elif day_number == 5:
        day = day + "Friday"
    elif day_number == 6:
        day = day + "Saturday"
    elif day_number == 7:
        day = day + "Sunday"

    else:
        day = day + "Error"

    return day


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 < v2 and v1 < v3:
        product = v2 * v3
    elif v2 < v1 and v2 < v3:
        product = v1 * v3
    elif v3 < v2 and v3 < v1:
        product = v1 * v3
    else:
        product = "Error"

    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    colour = ""
    if (rgb1 == "red" and rgb2 == "blue") or (rgb1 == "blue" and rgb2 == "red"):
        colour += "fuchsia"
    elif (rgb1 == "red" and rgb2 == "green") or (rgb1 == "green" and rgb2 == "red"):
        colour += "yellow"
    elif (rgb1 == "green" and rgb2 == "blue") or (rgb1 == "blue" and rgb2 == "green"):
        colour += "aqua"
    elif (rgb1 == "red" and rgb2 == "red") or (rgb1 == "red" and rgb2 == "red"):
        colour += "red"
    elif (rgb1 == "blue" and rgb2 == "blue") or (rgb1 == "blue" and rgb2 == "blue"):
        colour += "blue"
    elif (rgb1 == "green" and rgb2 == "green") or (rgb1 == "green" and rgb2 == "green"):
        colour += "green"
    else:
        colour += "Error"

    return colour


def yee_ha(number):
    """
     -------------------------------------------------------
    Returns "Yee" or "Ha" or "Yee" or "Nada":
    Returns "Error" if anything else.
    Use: ...yee_ha(int)
    -------------------------------------------------------
    Parameters:
        "Yee" if number is evenly divisible by 3
        "Ha" if number is evenly divisible by 7
        "Yee Ha" if number is evenly divisible by both 3 and 7
        "Nada" if number is none of the above
    Returns:
        (str)
    ------------------------------------------------------
    """
    if(number % 3 == 0 and number % 7 == 0):
        result = "Yee Ha"
    elif(number % 3 == 0):
        result = "Yee"
    elif(number % 7 == 0):
        result = "Ha"
    else:
        result = "Nada"

    return result

# figure variable colours
# Step 1: what colour addition equals to
# Step 2: other than that is error
# Step 3: return
