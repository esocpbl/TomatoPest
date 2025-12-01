import os
import torch
import torch.serialization
from ultralytics import YOLO
from pathlib import Path

def main():
    # Set device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    

    # Verify config exists
    config_path = Path('configs/tomato_pest.yaml')
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}. Make sure you run this script from the project root.")

    # Load YOLOv8 model
    print("Loading YOLOv8 model...")
    
    # Add safe globals for PyTorch 2.6+ compatibility
    torch.serialization.add_safe_globals(['ultralytics.nn.tasks.DetectionModel'])
    
    model = YOLO('yolov8n.pt')  # You can use yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt
    # Train the model
    results = model.train(
        data='configs/tomato_pest.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        device=device,
        project='models',
        name='tomato_pest_detector',
        save_period=10,
        patience=20,
        optimizer='Adam',
        lr0=0.001,
        weight_decay=0.0005,
        warmup_epochs=3,
        warmup_momentum=0.8,
        warmup_bias_lr=0.1,
        box=7.5,
        cls=0.5,
        dfl=1.5,
        pose=12.0,
        kobj=1.0,
        label_smoothing=0.0,
        nbs=64,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=0.0,
        translate=0.1,
        scale=0.5,
        shear=0.0,
        perspective=0.0,
        flipud=0.0,
        fliplr=0.5,
        mosaic=1.0,
        mixup=0.0,
        copy_paste=0.0,
        auto_augment='randaugment',
        erasing=0.4,
        crop_fraction=1.0
    )
    
    # Validate the model
    print("Validating model...")
    metrics = model.val()
    print(f"mAP50-95: {metrics.box.map}")
    print(f"mAP50: {metrics.box.map50}")
    print(f"mAP75: {metrics.box.map75}")
    
    # Test the model
    print("Testing model...")
    test_results = model.val(split='test')
    
    print("Training completed!")
    print(f"Model saved in: models/tomato_pest_detector/")

if __name__ == "__main__":
    main()