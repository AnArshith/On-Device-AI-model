

import json
import os

# Example class mapping
class_mapping = {
    "Name": 0,
    "Num": 1,
    "Address": 2,
    "Birthdate": 3,
    "ExpDate": 4,
    "IssueDate": 5
}

def convert_to_yolo_format(json_file, output_dir):
    with open(json_file, 'r') as f:
        data = json.load(f)

    img_width = data["size"]["width"]
    img_height = data["size"]["height"]
    objects = data["outputs"]["object"]
    img_name = os.path.splitext(data["path"])[0]
    yolo_labels = []

    for obj in objects:
        class_id = class_mapping[obj["name"]]
        bndbox = obj["bndbox"]
        xmin = bndbox["xmin"]
        ymin = bndbox["ymin"]
        xmax = bndbox["xmax"]
        ymax = bndbox["ymax"]
        
        # Calculate normalized coordinates
        x_center = (xmin + xmax) / 2.0 / img_width
        y_center = (ymin + ymax) / 2.0 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_labels.append(f"{class_id} {x_center} {y_center} {width} {height}")

    # Write to the YOLO format file
    output_file = os.path.join(output_dir, img_name + ".txt")
    with open(output_file, 'w') as f:
        f.write("\n".join(yolo_labels))

# Usage example
# json_file = "path_to_your_json_file.json"
# output_dir = "path_to_your_output_directory"
# convert_to_yolo_format(json_file, output_dir)

for i in range(500) :
    json_file = "/Users/arshith/Downloads/intern_srib/syn_trial/json/k" + str(i) + ".json"
    #json_file = json.load(open(json_path)) # have little doubt on it
    output_dir = "/Users/arshith/Downloads/intern_srib/syn_trial/labels"
    convert_to_yolo_format(json_file, output_dir)