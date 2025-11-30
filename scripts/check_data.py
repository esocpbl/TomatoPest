import os
from pathlib import Path

def check_data():
    raw_path = Path('dataset/raw_images')
    if not raw_path.exists():
        print(f"Error: {raw_path} does not exist.")
        return

    total_images = 0
    print(f"{'Class':<30} | {'Count':<10}")
    print("-" * 45)
    
    for class_dir in sorted(raw_path.iterdir()):
        if class_dir.is_dir():
            # Count images (jpg, jpeg, png, JPG, PNG)
            images = list(class_dir.glob('*.jpg')) + \
                     list(class_dir.glob('*.jpeg')) + \
                     list(class_dir.glob('*.png')) + \
                     list(class_dir.glob('*.JPG')) + \
                     list(class_dir.glob('*.PNG'))
            
            count = len(images)
            total_images += count
            print(f"{class_dir.name:<30} | {count:<10}")

    print("-" * 45)
    print(f"{'TOTAL':<30} | {total_images:<10}")

if __name__ == "__main__":
    check_data()
