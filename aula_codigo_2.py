import os
from PIL import Image
from transformers import pipeline
import tkinter as tk
from tkinter import filedialog
 
def detect_objects_and_generate_report(image_path):
    object_detector = pipeline("object-detection", model="facebook/detr-resnet-50")
    img = Image.open(image_path).convert("RGB")
    detections = object_detector(img)
    report_path = os.path.splitext(image_path)[0] + "_detection_report.txt"
 
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"Relatório de Detecção de Objetos\n")
        report_file.write(f"Imagem: {os.path.basename(image_path)}\n")
        report_file.write(f"Número total de objetos detectados: {len(detections)}\n\n")
 
        for i, detection in enumerate(detections, 1):
            label = detection["label"]
            score = detection["score"]
 
            report_file.write(f"Objeto {i}:\n")
            report_file.write(f"  - Classe: {label}\n")
            report_file.write(f"  - Confiança: {score:.2%}\n")
 
    print(f"Relatório gerado: {report_path}")
 
def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
            ("Todos os arquivos", "*.*")
        ]
    )
 
    if file_path:
        detect_objects_and_generate_report(file_path)
 
select_image()