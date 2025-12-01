import os
import shutil
from pathlib import Path
import yaml

def validate_roboflow_dataset(dataset_path):
    """
    Validate Roboflow dataset structure and create necessary directories
    """
    dataset_root = Path(dataset_path)
    
    # Required directories for Roboflow format
    required_dirs = [
        dataset_root / 'train' / 'images',
        dataset_root / 'train' / 'labels',
        dataset_root / 'valid' / 'images', 
        dataset_root / 'valid' / 'labels',
        dataset_root / 'test' / 'images',
        dataset_root / 'test' / 'labels'
    ]
    
    print("Validating Roboflow dataset structure...")
    
    # Check if directories exist
    missing_dirs = []
    for dir_path in required_dirs:
        if not dir_path.exists():
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print(f"Missing directories: {missing_dirs}")
        print("Creating missing directories...")
        for dir_path in missing_dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created: {dir_path}")
    
    # Count files in each directory
    for split in ['train', 'valid', 'test']:
        images_dir = dataset_root / split / 'images'
        labels_dir = dataset_root / split / 'labels'
        
        if images_dir.exists():
            image_files = list(images_dir.glob('*'))
            image_files = [f for f in image_files if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
            
            if labels_dir.exists():
                label_files = list(labels_dir.glob('*.txt'))
                
                print(f"\n{split.upper()} set:")
                print(f"  Images: {len(image_files)}")
                print(f"  Labels: {len(label_files)}")
                
                # Check for matching pairs
                image_names = {f.stem for f in image_files}
                label_names = {f.stem for f in label_files}
                
                missing_labels = image_names - label_names
                missing_images = label_names - image_names
                
                if missing_labels:
                    print(f"  [WARNING] Images without labels: {len(missing_labels)}")
                if missing_images:
                    print(f"  [WARNING] Labels without images: {len(missing_images)}")
                    
                if not missing_labels and not missing_images:
                    print(f"  [OK] All images have matching labels")
            else:
                print(f"\n{split.upper()} set:")
                print(f"  Images: {len(image_files)}")
                print(f"  [WARNING] Labels directory missing")

def check_class_distribution(dataset_path):
    """
    Analyze class distribution in the dataset
    """
    dataset_root = Path(dataset_path)
    class_counts = {}
    
    # Class mapping from Roboflow
    class_names = {
        0: 'Silverleaf Whitefly',
        1: 'Cotton Bollworm', 
        2: 'Green Peach Aphid',
        3: 'Beet Armyworm',
        4: 'Tobacco Cutworm',
        5: 'Western Flower Thrips',
        6: 'Two-spotted Spider Mite',
        7: 'Melon Fruit Fly'
    }
    
    print("\nAnalyzing class distribution...")
    
    for split in ['train', 'valid', 'test']:
        labels_dir = dataset_root / split / 'labels'
        if not labels_dir.exists():
            continue
            
        split_counts = {i: 0 for i in range(8)}
        
        for label_file in labels_dir.glob('*.txt'):
            try:
                with open(label_file, 'r') as f:
                    for line in f:
                        if line.strip():
                            class_id = int(line.split()[0])
                            if 0 <= class_id <= 7:
                                split_counts[class_id] += 1
            except Exception as e:
                print(f"Error reading {label_file}: {e}")
        
        print(f"\n{split.upper()} distribution:")
        for class_id, count in split_counts.items():
            if count > 0:
                print(f"  {class_names[class_id]} (ID {class_id}): {count} instances")
                
        # Update total counts
        for class_id, count in split_counts.items():
            if class_id not in class_counts:
                class_counts[class_id] = 0
            class_counts[class_id] += count
    
    print(f"\nTotal dataset distribution:")
    for class_id, count in class_counts.items():
        if count > 0:
            print(f"  {class_names[class_id]} (ID {class_id}): {count} instances")

def create_data_yaml(dataset_path, output_path='configs/tomato_pest.yaml'):
    """
    Create or update data.yaml file for Roboflow dataset
    """
    dataset_root = Path(dataset_path)
    
    data_config = {
        'path': str(dataset_root.absolute()),
        'train': 'train/images',
        'val': 'valid/images', 
        'test': 'test/images',
        'nc': 8,
        'names': ['Beet Armyworm-3', 'Cotton Bollworm-1', 'Green Peach Aphid-2', 'Melon Fruit Fly-7', 'Silverleaf Whitefly-0', 'Tobacco Cutworm-4', 'Two-spotted Spider Mite-6', 'Western Flower Thrips-5']
    }
    
    # Add Roboflow metadata
    data_config['roboflow'] = {
        'workspace': 'esocfall',
        'project': 'tomato_yolo-xmckl', 
        'version': 4,
        'license': 'CC BY 4.0',
        'url': 'https://universe.roboflow.com/esocfall/tomato_yolo-xmckl/dataset/4'
    }
    
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        yaml.dump(data_config, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n[OK] Data configuration saved to: {output_file}")

def main():
    """
    Main function to prepare Roboflow dataset
    """
    dataset_path = 'dataset'
    
    print("=== Roboflow Dataset Preparation ===")
    print(f"Dataset path: {Path(dataset_path).absolute()}")
    
    # Validate dataset structure
    validate_roboflow_dataset(dataset_path)
    
    # Check class distribution
    check_class_distribution(dataset_path)
    
    # Create/update data.yaml
    create_data_yaml(dataset_path)
    
    print("\n=== Dataset Preparation Complete ===")
    print("You can now run training with: python scripts/train.py")

if __name__ == "__main__":
    main()