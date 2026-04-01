from pathlib import Path

def create_raw_image(filename="dfir_image.img", size_mb=100):
    output_dir = Path("output/images")
    output_dir.mkdir(parents=True, exist_ok=True)

    image_path = output_dir / filename

    print(f"[+] Creating image: {image_path}")
    print(f"[+] Size: {size_mb} MB")

    with open(image_path, "wb") as f:
        f.seek(size_mb * 1024 * 1024 - 1)
        f.write(b"\0")

    print("[+] Image created successfully")

    return image_path