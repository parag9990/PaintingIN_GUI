import colorgram

color_rgb = []

colors = colorgram.extract('img_1.jpg', 20)
# print(colors)
for i in colors:
    red = i.rgb.r
    green = i.rgb.g
    blue = i.rgb.b
    color = (red, green, blue)
    color_rgb.append(color)

# print(color_rgb)

