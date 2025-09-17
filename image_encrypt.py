import cv2

def encrypt_image(path, key):
    image = cv2.imread(path)

    # Check if image loaded properly
    if image is None:
        print(f"[ERROR] Could not load image at: {path}")
        return

    print("[INFO] Image loaded successfully!")

    # Perform pixel manipulation
    encrypted = (image.astype('uint16') + key) % 256
    encrypted = encrypted.astype('uint8')

    cv2.imwrite("encrypted.jpg", encrypted)
    print("[SUCCESS] Image encrypted and saved as encrypted.jpg")

def decrypt_image(path, key):
    image = cv2.imread(path)

    if image is None:
        print(f"[ERROR] Could not load image at: {path}")
        return

    print("[INFO] Image loaded successfully!")

    decrypted = (image.astype('uint16') - key) % 256
    decrypted = decrypted.astype('uint8')

    cv2.imwrite("decrypted.jpg", decrypted)
    print("[SUCCESS] Image decrypted and saved as decrypted.jpg")

if __name__ == "__main__":
    key = int(input("Enter encryption key (number): "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    path = input("Enter path of image: ")

    if choice == "e":
        encrypt_image(path, key)
    elif choice == "d":
        decrypt_image(path, key)
    else:
        print("[ERROR] Invalid choice!")
