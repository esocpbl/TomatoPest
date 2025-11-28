@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete!
echo.
echo Next steps:
echo 1. Place your pest images in dataset/train/[pest_class]/
echo 2. Place validation images in dataset/val/[pest_class]/
echo 3. Run training with: python scripts/train.py
echo.
pause