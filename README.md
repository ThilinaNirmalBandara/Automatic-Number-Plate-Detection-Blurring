# Automatic Number Plate Detection & Blurring

This project implements a **custom deep learning model** to detect number plates in vehicle images and automatically blur them for privacy. The model is trained from scratch using PyTorch and annotated datasets in XML format.  

## Features
- Detects number plates accurately, even when there are other numbers or texts in the background.  
- Automatically blurs the detected number plates to protect privacy.  
- Handles images of various sizes, scaling them appropriately while preserving aspect ratio.  
- Can be trained on a custom dataset with bounding box annotations.  

## Technology Stack
- **Framework:** PyTorch  
- **Data Processing:** OpenCV, XML parsing  
- **Transforms & Data Loading:** Torchvision transforms, DataLoader  

## Dataset
- Annotated images in XML format (bounding boxes for number plates).  
- Dataset obtained from [Roboflow License Plate Recognition](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e).  
- Supports training on custom datasets.  

## How it Works
1. Images are loaded and preprocessed (resized, normalized).  
2. Bounding box annotations are read from XML files.  
3. A neural network predicts bounding boxes for number plates.  
4. Detected plates can be automatically blurred using OpenCV.  

## Usage
```python
import cv2
import torch

# Load image
img_path = "path/to/your/image.jpg"
image = cv2.imread(img_path)

# Preprocess and pass through your trained model
# model = load_your_model()
# boxes = model.predict(image)

# Blur detected number plates
for box in boxes:
    x1, y1, x2, y2 = box
    roi = image[y1:y2, x1:x2]
    blurred_roi = cv2.GaussianBlur(roi, (15, 15), 30)
    image[y1:y2, x1:x2] = blurred_roi

# Save or display result
cv2.imwrite("blurred_image.jpg", image)
cv2.imshow("Blurred Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
