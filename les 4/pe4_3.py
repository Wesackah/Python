
def lang_genoeg():
    lengte = eval(input('Wat is je lengte in centimeters?'))
    if lengte >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

print(lang_genoeg())