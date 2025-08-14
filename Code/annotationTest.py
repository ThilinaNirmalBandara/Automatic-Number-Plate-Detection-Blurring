import cv2
import xml.etree.ElementTree as ET
import os

# Paths

image_folder = r"C:/Users/thili/OneDrive/Desktop/SrilankaVehicles/Numberplate"
annotation_folder = r"C:/Users/thili/OneDrive/Desktop/SrilankaVehicles/Numberplate"


# Pick one image
image_file = "250.jpg"
image_path = os.path.join(image_folder, image_file)
annotation_path = os.path.join(annotation_folder, image_file.replace(".jpg", ".xml"))

# Load image
img = cv2.imread(image_path)

# Parse XML
tree = ET.parse(annotation_path)
root = tree.getroot()

# Draw bounding boxes
for obj in root.findall('object'):
    name = obj.find('name').text
    bndbox = obj.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)

    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    cv2.putText(img, name, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

# Show image
cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
