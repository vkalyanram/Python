email="Sailaja@unisys.com"
n=(email.split('@'))
print("Hi {0}, Welcome to {1}".format((n[0].capitalize()),(((n[1].split('.'))[0]).capitalize())))
