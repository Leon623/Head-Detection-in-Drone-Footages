import os
import shutil
from tqdm import tqdm

def convert_to_yolo_format(root, output_folder, mode="train"):
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "labels"), exist_ok=True)

    mode_folder = os.path.join(root, mode)

    for detection_folder in tqdm(os.listdir(mode_folder), colour="green"):

        image_folder = os.path.join(os.path.join(mode_folder, detection_folder), "img1")
        for image in os.listdir(image_folder):
            new_image_name = f"{detection_folder}_{image}"
            shutil.copy(os.path.join(image_folder, image),
                        os.path.join(output_folder, "images", new_image_name))

        gt_label = "gt" if os.path.exists(os.path.join(mode_folder, detection_folder, "gt")) else "det"
        detections_path = os.path.join(mode_folder, detection_folder, gt_label, f"{gt_label}.txt")

        with open(detections_path, 'r') as file:
            detections = file.readlines()

        for detection in detections:
            values = detection.strip().split(',')

            image_number = values[0]
            x, y, w, h = map(float, values[2:6])

            x_center = (x + w / 2)/1920
            y_center = (y + h / 2)/1080
            w = w/1920
            h = h/1080

            label_string = f"0 {x_center} {y_center} {w} {h}"

            image_number_formatted = image_number.zfill(6)

            label_file_path = os.path.join(output_folder, "labels", f"{detection_folder}_{image_number_formatted}.txt")

            with open(label_file_path, 'a') as label_file:
                label_file.write(label_string + '\n')


if __name__ == "__main__":
    root = 'HT21'
    output_folder = 'train'
    mode = "train"

    convert_to_yolo_format(root, output_folder, mode=mode)
