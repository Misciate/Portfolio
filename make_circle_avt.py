from PIL import Image, ImageDraw

def make_circle_avatar(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    img = img.resize((size, size))
    
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    result = Image.new("RGBA", (size, size))
    result.paste(img, (0, 0), mask)
    result.save(output_path)

make_circle_avatar("profile-pic1.jpg", "avatar_circle1.png")
make_circle_avatar("profile-pic2.jpg", "avatar_circle2.png")
