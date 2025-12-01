# Tomato Pest Detection using YOLOv8

This repository contains a complete setup for training YOLOv8 models to detect and classify 8 common tomato pests using Roboflow dataset format.

## Project Structure

```
TomatoPest/
├── dataset/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   └── labels.cache
├── models/
│   └── tomato_pest_detector/
│       ├── weights/
│       │   ├── best.pt
│       │   └── last.pt
│       └── training_results/
├── configs/
│   └── tomato_pest.yaml
├── scripts/
│   ├── train.py
│   └── prepare_roboflow_dataset.py
├── yolov8n.pt
├── yolo11n.pt
├── requirements.txt
└── setup.bat
```

## Pest Classes (Roboflow Format)

The dataset uses Roboflow's YOLO format with the following class IDs (as defined in `configs/tomato_pest.yaml`):

| ID | Class Name | Scientific Name | Common Name (Indonesian) |
|----|------------|----------------|--------------------------|
| 0 | Beet Armyworm-3 | Spodoptera exigua | Ulat grayak bawang |
| 1 | Cotton Bollworm-1 | Helicoverpa armigera | Ulat buah kapas |
| 2 | Green Peach Aphid-2 | Myzus persicae | Kutu daun hijau |
| 3 | Melon Fruit Fly-7 | Zeugodacus cucurbitae | Lalat buah labu |
| 4 | Silverleaf Whitefly-0 | Bemisia argentifolii | Kutu kebul |
| 5 | Tobacco Cutworm-4 | Spodoptera litura | Ulat grayak tembakau |
| 6 | Two-spotted Spider Mite-6 | Tetranychus urticae | Kutu laba-laba dua bercak |
| 7 | Western Flower Thrips-5 | Thrips palmi | Thrips melon |

**Note**: Class names include numeric suffixes from Roboflow export. The numbering follows the configuration file order.

## Setup Instructions

### 1. Activate Virtual Environment

```bash
# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies

**GPU Training (Recommended):**
```bash
pip install -r requirements.txt
```

**Note:** This project requires CUDA-compatible PyTorch for GPU training. The requirements.txt includes PyTorch with CUDA 11.8 support. Make sure you have:
- NVIDIA GPU with CUDA support
- CUDA Toolkit 11.8 or compatible version
- Latest NVIDIA drivers

**CPU Training (Slower):**
If you don't have a compatible GPU, you can install CPU-only PyTorch:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt --ignore-dependencies
```

### 3. Prepare Dataset

**Using Roboflow Dataset (Current Setup)**
1. Download Roboflow dataset ZIP file
2. Extract contents to `dataset/` folder
3. Run the preparation script:
   ```bash
   python scripts/prepare_roboflow_dataset.py
   ```

The script will:
- Validate dataset structure
- Check class distribution
- Generate/update configuration file
- Ensure all images have matching labels

### 4. Train Model

```bash
python scripts/train.py
```

## Dataset Requirements

### Roboflow Dataset Format
- **Image format**: JPG, PNG, JPEG
- **Label format**: YOLO .txt files with class_id x_center y_center width height (normalized)
- **Recommended image size**: 640x640 pixels
- **Minimum images per class**: 100+ for good results
- **Data split**: Pre-defined by Roboflow (train/valid/test folders)
- **Structure**: 
  ```
  dataset/
  ├── train/
  │   ├── images/
  │   └── labels/
  ├── valid/
  │   ├── images/
  │   └── labels/
  └── test/
      ├── images/
      └── labels/
  ```

## Training Configuration

The model uses YOLOv8 nano (yolov8n.pt) by default. You can change to:
- yolov8s.pt (small)
- yolov8m.pt (medium) 
- yolov8l.pt (large)
- yolov8x.pt (extra large)

**Available model files:**
- `yolov8n.pt` - Currently used for training
- `yolo11n.pt` - Available for future YOLOv11 experiments

Edit `configs/tomato_pest.yaml` to modify training parameters.

## Model Evaluation

After training, model will be saved in `models/tomato_pest_detector/` with:
- Best weights: `best.pt`
- Last weights: `last.pt`
- Training metrics and plots
- Performance curves and confusion matrices

## Testing the Model

### Test on Single Image:
```bash
python scripts/simple_test.py path/to/image.jpg
```

### Test on Validation/Test Sets:
```bash
python scripts/simple_test.py
```

## Quick Start Guide

1. **Setup Environment:**
   ```bash
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Prepare Dataset:**
   ```bash
   python scripts/prepare_roboflow_dataset.py
   ```

3. **Train Model:**
   ```bash
   python scripts/train.py
   ```

4. **Test Model:**
   ```bash
   python scripts/simple_test.py dataset/test/images/your_test_image.jpg
   ```

## For Custom Dataset:
1. Collect and organize your pest images
2. Annotate images with bounding boxes (using Roboflow, LabelImg, etc.)
3. Convert to YOLO format with train/valid/test structure
4. Update `configs/tomato_pest.yaml` with your class names
5. Run training script
6. Evaluate model performance
7. Deploy for inference

### For Custom Dataset:
1. Collect and organize your pest images
2. Annotate images with bounding boxes (using Roboflow, LabelImg, etc.)
3. Convert to YOLO format
4. Run training script
5. Evaluate model performance
6. Deploy for inference

## Roboflow Dataset Information

- **Workspace**: esocfall
- **Project**: tomato_yolo-xmckl
- **Version**: 4
- **License**: CC BY 4.0
- **URL**: https://universe.roboflow.com/esocfall/tomato_yolo-xmckl/dataset/4

## Current Model Performance

Based on training results:
- **Validation mAP50**: 81.9%
- **Test mAP50**: 90.4%
- **Best performing classes**: Melon Fruit Fly (97.5%), Cotton Bollworm (94.9%), Tobacco Cutworm (95.2%)
- **Training time**: ~1.1 hours for 100 epochs
- **Model size**: 6.3MB (optimized)

## Troubleshooting

### Common Issues:
1. **CUDA errors**: Ensure you have compatible NVIDIA drivers and CUDA toolkit
2. **Dataset not found**: Check that dataset is extracted to correct folder structure
3. **Memory issues**: Reduce batch size in `train.py` if GPU memory is insufficient
4. **Poor performance**: Check class distribution and consider data augmentation

### Getting Help:
- Check training logs in `models/tomato_pest_detector/`
- Review confusion matrix and performance plots
- Ensure dataset quality and proper labeling