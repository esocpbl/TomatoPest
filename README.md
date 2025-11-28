# Tomato Pest Detection using YOLOv8

This repository contains a complete setup for training YOLOv8 models to detect and classify 8 common tomato pests.

## Project Structure

```
TomatoPest/
├── dataset/
│   ├── train/
│   │   ├── aphids/
│   │   ├── whitefly/
│   │   ├── thrips/
│   │   ├── tomato_hornworm/
│   │   ├── cutworm/
│   │   ├── colorado_beetle/
│   │   ├── spider_mite/
│   │   └── leafminer/
│   ├── val/
│   │   └── [same 8 pest folders]
│   └── test/
│       └── [same 8 pest folders]
├── models/
├── configs/
│   └── tomato_pest.yaml
├── scripts/
│   ├── train.py
│   └── prepare_dataset.py
├── logs/
├── venv/
└── requirements.txt
```

## Pest Classes

1. **BA** - Bemisia Argentifolii (Kutu kebul / Whitefly)
2. **HA** - Helicoverpa Armigera (Ulat buah kapas / ulat penggerek buah jagung)
3. **MP** - Myzus Persicae (kutu daun hijau)
4. **SE** - Spodoptera Exigua (Ulat grayak bawang)
5. **SL** - Spodoptera Litura (Ulat grayak tembakau / ulat grayak daun)
6. **TP** - Thrips Palmi (thrips melon atau thrips kuning)
7. **TU** - Tetranychus Urticae (Kutu laba-laba dua bercak / Kutu merah)
8. **ZC** - Zeugodacus cucurbitae (Lalat buah labu)

## Setup Instructions

### 1. Activate Virtual Environment

```bash
# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare Dataset

Place your pest images in the appropriate folders:
- Training images: `dataset/train/[pest_class]/`
- Validation images: `dataset/val/[pest_class]/`
- Test images: `dataset/test/[pest_class]/`

### 4. Train Model

```bash
python scripts/train.py
```

## Dataset Requirements

- **Image format**: JPG, PNG, JPEG
- **Recommended image size**: 640x640 pixels
- **Minimum images per class**: 100+ for good results
- **Data split**: 70% train, 20% validation, 10% test

## Training Configuration

The model uses YOLOv8 nano (yolov8n.pt) by default. You can change to:
- yolov8s.pt (small)
- yolov8m.pt (medium) 
- yolov8l.pt (large)
- yolov8x.pt (extra large)

Edit `configs/tomato_pest.yaml` to modify training parameters.

## Model Evaluation

After training, the model will be saved in `models/tomato_pest_detector/` with:
- Best weights: `best.pt`
- Last weights: `last.pt`
- Training metrics and plots

## Next Steps

1. Collect and organize your pest images
2. Annotate images with bounding boxes (for detection)
3. Run training script
4. Evaluate model performance
5. Deploy for inference