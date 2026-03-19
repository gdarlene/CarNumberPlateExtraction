# Car Number Plate Extraction 

## Overview

This project implements a **Car Number Plate Extraction** feature on car plates using OCR.

This pipeline deals with different important mechanisms to detect the plater number of a certain car thereby making decisions useful in areas such as transport management, parkings and other areas.


## How Plate number extraction Works in real world

1. The plate is detected that is the area is captured.
2. Plate alignment involves Correcting tilt, skew, and perspective so that characters appear upright and evenly spaced.
3. OCR is then implemented where text extraction from the aligned plate image.


## Project Structure

```
car-number-plate-extraction/
├── data/
│   ├── plates/
│   ├── logs/
├── src/                 
│   ├── camera.py               
│   ├── detect.py                           
│   ├── ocr.py             
│   ├── validate.py           
│   └── temporal.py         
├── README.md
├── .gitignore
├── init_project.py
└── book/                       
```