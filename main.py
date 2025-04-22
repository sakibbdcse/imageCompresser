from PIL import Image
import os

def compress_image(input_path, output_path, quality=60):
    with Image.open(input_path) as img:
        ext = os.path.splitext(input_path)[1].lower()

        # Convert for transparency handling
        if ext == ".png":
            if img.mode not in ("RGBA", "P"):
                img = img.convert("RGBA")
            img.save(output_path, "PNG", optimize=True)
        else:
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(output_path, "JPEG", optimize=True, quality=quality)

        before = os.path.getsize(input_path)
        after = os.path.getsize(output_path)
        print(f"{os.path.basename(input_path)}: {before//1024}KB → {after//1024}KB")

def compress_folder(input_folder, output_folder, quality=60):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path, quality)

# Example usage
# compress_image("input.jpg", "output.jpg", quality=40)
# compress_folder("images", "compressed_images", quality=50)
# compress_image("media/inputmeida/cmimg.png", "media/outputmedia/cmimg.png", quality=40)
compress_folder("media/inputmeida/spice/", "media/outputmedia/spice", quality=60)

