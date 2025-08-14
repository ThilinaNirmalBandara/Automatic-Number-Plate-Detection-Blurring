# Automatic Number Plate Detection & Blurring

This project implements a **custom deep learning model** to detect number plates in vehicle images and automatically blur them for privacy.It fine-tunes a **torchvision Faster R-CNN** detector on **PASCAL VOC XML** annotations where **images and XML files live in the same folder** for each split.

## Features
- **Train / Val / Test** with VOC XML annotations (one XML per image).
- **Subsampling**: cap training to 2000 images; validation size is a percentage of 2000 (default 20% → 400), and test is capped at 2000.
- **Simple augmentation**: random horizontal flip.
- **Evaluation**: Precision / Recall / F1 at **IoU=0.5**.
- **Visualization**: draw predicted boxes; **optional blur** using OpenCV.
- **Speed mode (CPU)**: switch to **MobileNetV3-320 FPN**, smaller input (e.g., 320), freeze backbone, and reduce proposals.

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

