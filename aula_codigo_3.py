import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from transformers import pipeline
import tkinter as tk
from tkinter import filedialog
 
def detect_objects_in_image(image_path):
    object_detector = pipeline("object-detection", model="facebook/detr-resnet-50")
    img = Image.open(image_path).convert("RGB")
    detections = object_detector(img)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    ax.imshow(img)
 
    for detection in detections:
        box = detection["box"]
        label = detection["label"]
        score = detection["score"]
 
        rect = patches.Rectangle(
            (box["xmin"], box["ymin"]), 
            box["xmax"] - box["xmin"],   
            box["ymax"] - box["ymin"],   
            linewidth=2,
            edgecolor="red",
            facecolor="none"
        )
        ax.add_patch(rect)
 
        ax.text(
            box["xmin"],
            box["ymin"] - 10,
            f"{label} ({score:.2f})",
            color="red",
            fontsize=12,
            backgroundcolor="white"
        )
 
    plt.title("Detecção de Objetos com DETR")
    plt.axis("off")
    plt.show()
 
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
        detect_objects_in_image(file_path)
 
select_image()