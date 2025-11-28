import os
import cv2
import numpy as np
from pathlib import Path
import shutil
from sklearn.model_selection import train_test_split

def prepare_dataset():
    """
    Organize dataset into YOLO format if images are in separate folders
    """
    dataset_path = Path("dataset")
    
    # Create YOLO format directories
    yolo_path = dataset_path / "yolo_format"
    yolo_path.mkdir(exist_ok=True)
    
    for split in ['train', 'val', 'test']:
        (yolo_path / 'images' / split).mkdir(parents=True, exist_ok=True)
        (yolo_path / 'labels' / split).mkdir(parents=True, exist_ok=True)
    
    print("YOLO format directories created successfully!")

def convert_to_yolo_format():
    """
    Instructions for converting dataset to YOLO format
    """
    print("\n" + "="*50)
    print("DATASET PREPARATION INSTRUCTIONS")
    print("="*50)
    print("1. Upload your images to a labeling tool like Roboflow or CVAT.")
    print("2. Draw bounding boxes around each pest.")
    print("3. Export the dataset in 'YOLOv8' format.")
    print("4. Extract the exported files into the 'dataset' folder so it looks like this:")
    print("   dataset/")
    print("   ├── train/")
    print("   │   ├── images/ (contains .jpg/.png)")
    print("   │   └── labels/ (contains .txt)")
    print("   ├── val/")
    print("   │   ├── images/")
    print("   │   └── labels/")
    print("   └── test/")
    print("       ├── images/")
    print("       └── labels/")
    print("="*50 + "\n")

def visualize_dataset():
    """
    Visualize sample images from each class
    """
    import matplotlib.pyplot as plt
    
    dataset_path = Path("dataset/train")
    classes = ['BA', 'HA', 'MP', 'SE', 
               'SL', 'TP', 'TU', 'ZC']
    
    fig, axes = plt.subplots(2, 4, figsize=(15, 8))
    axes = axes.ravel()
    
    for i, pest_class in enumerate(classes):
        class_path = dataset_path / pest_class
        if class_path.exists():
            images = list(class_path.glob("*.jpg")) + list(class_path.glob("*.png"))
            if images:
                img_path = images[0]
                img = cv2.imread(str(img_path))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                axes[i].imshow(img)
                axes[i].set_title(pest_class)
                axes[i].axis('off')
    
    plt.tight_layout()
    plt.savefig('dataset_samples.png')
    print("Dataset samples saved as dataset_samples.png")

if __name__ == "__main__":
    prepare_dataset()
    convert_to_yolo_format()
    visualize_dataset()