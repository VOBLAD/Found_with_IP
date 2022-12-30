import geocoder
import webbrowser as wb


try:
    g = geocoder.ip("me")   # your ip
    q = str(g.latlng)
    wb.open('http://www.google.com/maps/place/search?q=' + q[1:-1])
except:
    print("Error!:Please check your IP")

