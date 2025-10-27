# ship_detection Web App
A Streamlit-based web application for detecting ships using a YOLO model.

## setup

1. Clone the repository:
git clone
cd ship_detection

2. Build Doucker image:
docker build -t ship-detection-app

3. Run the container:
doucker run -p 8501:8501 ship-detection-app

4. Visit [http://localhost:8501](http://localhost:8051)
## Requirements
- python 3.10
- Docker
- Streamlit
- Ultralytics
