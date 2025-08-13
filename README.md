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
- Supports training on custom datasets.

## How it Works
1. Images are loaded and preprocessed (resized, normalized).
2. Bounding box annotations are read from XML files.
3. A neural network predicts bounding boxes for number plates.
4. Detected plates can be automatically blurred using OpenCV.

## Credits
Inspired by deep learning techniques from IBM tutorials and PyTorch documentation.

