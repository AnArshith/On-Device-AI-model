# Text-extraction-model
Using object detection models and ocr models, making an On-device model that extracts the field data from driving licenses.

Using the real data of different driving licenses, we create the templates using Photoshop.
<img width="210" alt="Screenshot 2024-07-02 at 3 13 20 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/f6c49e51-5d4b-4549-9ac8-0490ffd80c16">

Using the libraries PILLOW, JSON and faker. and using different fonts, we create several copies of the same template that match with the original template in size and colour with different data on the selected fields and warp them with different perspectives.


<img width="609" alt="Screenshot 2024-07-02 at 3 16 33 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/ae7fcad3-9f1e-4959-a3f3-d04fe4b88517">

Train them on different Object Detection Models like yolo models like Yolov8n, Yolov10n and Yolov10s with a dataset of 3000 images and txt format labels.

Trained models are used to predict the classes and using pytesseract OCR model, extract the data from it

The output of V8n model trained on the 3000 images dataset, for 25 epochs:

<img width="721" alt="Screenshot 2024-07-02 at 3 21 38 PM" src="https://github.com/AnArshith/Text-extraction-model/assets/111214899/36ebab38-38cc-49a3-96c7-6aef0c62bf4a">
