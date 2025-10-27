# ship_detection Web App
A Streamlit-based web application for detecting ships using a YOLO model.

## Live App
Acceess the deployed app here:
[Ship Detection App (Streamlit)](https://shipdetection-gfpqehysukeayqtfwnnsgr.streamlit.app/)

## Setup (local)

1. **Clone the repository:**
'''bash
git clone https://github.com/rama7rbi1/ship_detection.git
cd ship_detection

2. Build Doucker image:
docker build -t ship-detection-app .

3. Run the container:
doucker run -p 8501:8501 ship-detection-app

4. Visit [http://localhost:8501](http://localhost:8051)

## Requirements
- python 3.10
- Docker
- Streamlit
- Ultralytics
- OpenCV (opencv-python)
- Pillow

## Model
the app uses a YOLO model saved as best.pt placed in:
web_interface/models/best.pt
