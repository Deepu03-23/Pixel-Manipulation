from PIL import Image # type: ignore
import os
def encrypt_decrypt_image(input_path, output_path, key):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            pixels = img.load()

            width, height = img.size

            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    # Apply XOR operation with the key
                    pixels[x, y] = (
                        r ^ key,
                        g ^ key,
                        b ^ key
                    )
            img.save(output_path)
            print(f"Saved result to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice.")
        return

    input_path = input("Enter input image path: ").strip()
    if not os.path.exists(input_path):
        print("Image not found.")
        return

    output_path = input("Enter output image path: ").strip()
    try:
        key = int(input("Enter a numeric key (0-255): ").strip())
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print("Invalid key. Must be an integer between 0 and 255.")
        return

    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
