from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "paw.jpg")

# Open in RGBA mode
paw_img = Image.open(img_path).convert("RGBA")
datas = paw_img.getdata()

newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0))  # transparent
    else:
        newData.append(item)

paw_img.putdata(newData)

output_path = os.path.join(script_dir, "paw_transparent.png")
paw_img.save(output_path, "PNG")

print("✅ Transparent image saved as:", output_path)
