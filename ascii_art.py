import sys
from PIL import Image

# Define your ASCII character ramp, from dark to light.
# You can experiment with different ramps for different effects.
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."

def resize_image(image, new_width=100):
    """Resizes an image while maintaining its aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width * 0.55) # 0.55 is a correction factor for char aspect ratio
    new_image = image.resize((new_width, new_height))
    return new_image

def image_to_grayscale(image):
    """Converts an image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Maps each pixel to an ASCII character based on its brightness."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        # Map the 0-255 pixel value to an index in our ASCII ramp
        index = int(pixel_value / 255 * (len(ASCII_CHARS) - 1))
        ascii_str += ASCII_CHARS[index]
    return ascii_str

def main():
    """The main function that ties everything together."""
    # Get the image path from the command line arguments
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: python ascii_converter.py <image_path>")
        return

    # Open the image
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    # 1. Resize the image
    resized_image = resize_image(image)

    # 2. Convert to grayscale
    grayscale_image = image_to_grayscale(resized_image)

    # 3. Convert pixels to ASCII characters
    ascii_str = pixels_to_ascii(grayscale_image)

    # 4. Print the result
    img_width = grayscale_image.width
    for i in range(0, len(ascii_str), img_width):
        print(ascii_str[i:i+img_width])

if __name__ == '__main__':
    main()