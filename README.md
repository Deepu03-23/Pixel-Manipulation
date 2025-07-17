# Pixel-Manipulation

This is a simple Python script that performs image encryption and decryption using a bitwise XOR operation. It works by applying a numeric key (0–255) to each pixel's RGB values. The same key is used to decrypt the image back to its original state.

🔍 How the Code Works

Your script performs image encryption and decryption using a bitwise XOR operation on each pixel's color values. Here's how:

1. User Input (CLI)

The script first asks the user:

Whether they want to encrypt or decrypt (E or D)

The path of the input image file

The desired output image file name

A numeric key (between 0 and 255)

This key will be used for the XOR operation.

