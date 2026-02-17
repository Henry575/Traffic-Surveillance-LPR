def read_plate(image_path):
    import cv2
    import easyocr
    import re
    import os

    image = cv2.imread(image_path)

    if image is None:
        print("Vehicle image not found.")
        return None

    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)

    detected_number = ""

    for detection in results:
        text = detection[1]
        text = re.sub(r'[^A-Za-z0-9]', '', text)
        text = text.upper()

        match = re.search(r'[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}', text)
        if match:
            detected_number = match.group()
            break

    if detected_number != "":
        print("Detected Vehicle Number:", detected_number)

        # Save inside outputs folder
        output_path = os.path.join("outputs", "detected_number.txt")
        with open(output_path, "w") as f:
            f.write(detected_number)

        print("Detected number saved to outputs/detected_number.txt")

        return detected_number   # 🔥 IMPORTANT

    else:
        print("Valid plate format not detected.")
        return None
