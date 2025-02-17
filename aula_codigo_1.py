import os
import requests
from io import BytesIO
from PIL import Image
from transformers import pipeline
 
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(PROJECT_DIR, 'object_detection_reports')
os.makedirs(REPORTS_DIR, exist_ok=True)
 
def detect_objects_from_url(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGB")
 
        object_detector = pipeline("object-detection", model="facebook/detr-resnet-50")
 
        detections = object_detector(img)
 
        url_filename = image_url.split('/')[-1]
        report_filename = f"{os.path.splitext(url_filename)[0]}_detection_report.txt"
        report_path = os.path.join(REPORTS_DIR, report_filename)
 
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(f"Relatório de Detecção de Objetos\n")
            report_file.write(f"URL da Imagem: {image_url}\n")
            report_file.write(f"Número total de objetos detectados: {len(detections)}\n\n")
 
            for i, detection in enumerate(detections, 1):
                label = detection["label"]
                score = detection["score"]
 
                report_file.write(f"Objeto {i}:\n")
                report_file.write(f"  - Classe: {label}\n")
                report_file.write(f"  - Confiança: {score:.2%}\n")
 
        print(f"Relatório gerado: {report_path}")
 
    except requests.RequestException as e:
        print(f"Erro ao baixar a imagem: {e}")
    except Exception as e:
        print(f"Erro durante a detecção de objetos: {e}")
 
 
image_url = "https://1.bp.blogspot.com/-6jIbpfcxq3E/WWQdHq3ovCI/AAAAAAAAX24/3tA90PrWViIP9XAlL9U5GRxQ4zJOQkNJwCLcBGAs/s1600/ESTRADAS.jpg"
detect_objects_from_url(image_url)