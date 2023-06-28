from PIL import Image

# Open the image file
image = Image.open("image.png")

# Display information about the image
print("Image format:", image.format)
print("Image size:", image.size)
print("Image mode:", image.mode)

# Show the image
image.show()
