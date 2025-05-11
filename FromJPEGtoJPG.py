from PIL import Image # type: ignore

def convert_to_jpg(image_path):
    img = Image.open(image_path)
    
    # Change the extension from .jpeg to .jpg
    new_image_path = image_path.rsplit('.', 1)[0] + '.jpg'
    
    # Save the image as .jpg
    img.convert('RGB').save(new_image_path, 'PNG')
    print(f"Image saved as: {new_image_path}")

# Example usage
image_path = 'IMG_9452.PNG'
convert_to_jpg(image_path)
