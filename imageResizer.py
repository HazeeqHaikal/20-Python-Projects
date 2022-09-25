from PIL import Image

def resizeImage(size1, size2):
    
    image = Image.open('./image/cr7.png')

    print(f"Current image size: {image.size}")

    resizeImage = image.resize((size1, size2))

    resizeImage.save('./image/cr7_resized.png')
    print("Image resized successfully")

if __name__ == '__main__':
    size1 = int(input("Enter the width of the image: "))
    size2 = int(input("Enter the height of the image: "))
    resizeImage(size1, size2)