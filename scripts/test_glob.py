from pathlib import Path

def test_glob():
    p = Path('dataset/raw_images/BA')
    jpgs = list(p.glob('*.jpg'))
    JPGs = list(p.glob('*.JPG'))
    
    print(f"*.jpg count: {len(jpgs)}")
    print(f"*.JPG count: {len(JPGs)}")
    
    # Check intersection
    set_jpg = set(jpgs)
    set_JPG = set(JPGs)
    intersection = set_jpg.intersection(set_JPG)
    print(f"Intersection count: {len(intersection)}")

if __name__ == "__main__":
    test_glob()
