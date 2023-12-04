import os
import random
import shutil


def copy_random_images(source_folder, destination_folder, num_images):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    all_images = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    num_images = min(num_images, len(all_images))

    selected_images = random.sample(all_images, num_images)

    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy2(source_path, destination_path)

    print(f"{num_images} random images copied to {destination_folder}")


if __name__ == "-_main__":
    source_folder = "lhq_1024_jpg"
    destination_folder = "background_images"
    num_images_to_copy = 2000

    copy_random_images(source_folder, destination_folder, num_images_to_copy)
