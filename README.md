# Text-extraction-model

# On-Device Driving License Field Data Extraction

This project leverages object detection and OCR models to develop an on-device solution for extracting field data from driving licenses.

## **Overview**

Using real driving license data, we design and create templates with Photoshop to ensure accurate and efficient data extraction.

<img width="210" alt="Screenshot 2024-07-02 at 3 13 20 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/f6c49e51-5d4b-4549-9ac8-0490ffd80c16">

## **Key Features**

- **Template Generation**: Utilizing the libraries **PILLOW**, **JSON**, and **Faker**, we generate multiple copies of the same template. These templates match the original in size and color but contain different data in the selected fields.
- **Font Variation**: Different fonts are applied to each copy to enhance the robustness of the extraction process.
- **Perspective Warping**: Templates are warped with various perspectives to simulate real-world scenarios and improve model performance.


<img width="609" alt="Screenshot 2024-07-02 at 3 16 33 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/ae7fcad3-9f1e-4959-a3f3-d04fe4b88517">


## **Training Process**

- **Object Detection Models**: We train various object detection models such as **YOLOv8n**, **YOLOv10n**, and **YOLOv10s** using a dataset of 3000 images and corresponding TXT format labels.

- **OCR Integration**: The trained models are used to predict classes, and **pytesseract** OCR model is employed to extract data from the detected regions.

## **Model Performance**

The output of the **YOLOv8n** model trained on the 3000 images dataset for 25 epochs:

<img width="721" alt="Screenshot 2024-07-02 at 3 21 38 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/36ebab38-38cc-49a3-96c7-6aef0c62bf4a">
