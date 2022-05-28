# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

# find the most common color in the image
most_common_color = max(set(rgb_colors), key=rgb_colors.count)
print(most_common_color)