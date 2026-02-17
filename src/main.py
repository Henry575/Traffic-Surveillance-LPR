import os
from datetime import datetime
from plate_detection import detect_plate
from ocr_reader import read_plate


# -----------------------------
# Step 1: Define Paths
# -----------------------------

IMAGE_PATH = "assets/car.jpg"
MODEL_PATH = "models/yolov8n.pt"
OUTPUT_FOLDER = "outputs"
DETECTED_TEXT_FILE = os.path.join(OUTPUT_FOLDER, "detected_number.txt")


# -----------------------------
# Step 2: Create outputs folder if not exists
# -----------------------------

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


# -----------------------------
# Step 3: Detect Plate
# -----------------------------

print("\n🚗 Detecting license plate...")

cropped_plate_path = detect_plate(
    image_path=IMAGE_PATH,
    model_path=MODEL_PATH,
    output_folder=OUTPUT_FOLDER
)

if cropped_plate_path is None:
    print("❌ Plate detection failed.")
    exit()

print("✅ Plate detected successfully.")


# -----------------------------
# Step 4: OCR Reading
# -----------------------------

print("\n🔍 Reading plate number...")

detected_number = read_plate(cropped_plate_path)

if detected_number is None or detected_number == "":
    print("❌ OCR failed.")
    exit()

print("✅ Detected Vehicle Number:", detected_number)


# Save detected number
with open(DETECTED_TEXT_FILE, "w") as f:
    f.write(detected_number)


# -----------------------------
# Step 5: Mock Vehicle Database
# -----------------------------

vehicle_data = {
    "MH20EE7602": {
        "RC Expiry": "2027-05-20",
        "Insurance Expiry": "2025-03-15",
        "PUC Expiry": "2024-12-10"
    }
}

# -----------------------------
# Step 6: Expiry Check
# -----------------------------

today = datetime.today()

print("\n📋 Checking Document Status...\n")

if detected_number in vehicle_data:
    for doc, expiry_date in vehicle_data[detected_number].items():

        expiry = datetime.strptime(expiry_date, "%Y-%m-%d")

        if expiry < today:
            print(f"{doc}: ❌ EXPIRED (Expired on {expiry_date})")
        else:
            print(f"{doc}: ✅ VALID (Expires on {expiry_date})")

else:
    print("⚠ Vehicle not found in database.")
