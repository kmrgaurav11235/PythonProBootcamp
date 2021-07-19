# Install colorgram: https://pypi.org/project/colorgram.py/
from colorgram import extract

extracted_color_list = extract("image.jpg", 30)  # Extract 30 colors from image.

color_list_rgb = []
for color in extracted_color_list:
    # colorgram.extract() returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    color_rgb = color.rgb
    color_list_rgb.append((color_rgb.r, color_rgb.g, color_rgb.b))

# print(color_list_rgb)

# First 3 are shades of White
color_list_rgb = color_list_rgb[3:]
print("Final Extracted Color List: ")
print(color_list_rgb)  # Final List
