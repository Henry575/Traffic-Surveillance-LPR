def detect_plate(image_path, model_path, output_folder):
    from ultralytics import YOLO
    import cv2
    import os

    model = YOLO(model_path)
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return None

    results = model(image)

    vehicle_found = False
    output_path = os.path.join(output_folder, "detected_vehicle.jpg")

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            # Detect vehicles
            if label in ["car", "truck", "bus"]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                vehicle = image[y1:y2, x1:x2]

                cv2.imwrite(output_path, vehicle)
                print("Vehicle detected and saved as detected_vehicle.jpg")

                vehicle_found = True
                return output_path   # 🔥 VERY IMPORTANT

    if not vehicle_found:
        print("No vehicle detected.")
        return None
