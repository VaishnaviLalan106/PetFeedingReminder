from PIL import Image
import os

# Input PNG/JPG image
img = Image.open("paw_transparent.png")  # or paw.jpg if you prefer

# Save as ICO with multiple sizes (better for Windows)
img.save("paw.ico", format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])

print("✅ Icon created as paw.ico")
