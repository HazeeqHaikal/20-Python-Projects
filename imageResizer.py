from PIL import Image

image = Image.open('./image/cr7.png')

print(f"Current image size: {image.size}")

resizeImage = image.resize((300, 300))

resizeImage.save('./image/cr7_resized.png')
print("Image resized successfully")