from pathlib import Path

structure = {
    "data/plates":[],
    "data/logs":[],
"src":[
    # helps to capture the plate region
    "camera.py",
    "detect.py",
    "align.py",
    "ocr.py",
    "validate.py",
    "temporal.py",
],
"book":[],
}
for folder, files in structure.items():
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)
    
    for file in files:
        file_path = folder_path / file
        if not file_path.touch(exist_ok=True):
            file_path.touch()
print("Car Number Plate Detection project created successfully.")
            
        
