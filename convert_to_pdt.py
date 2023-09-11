import os
from PIL import Image
from pathlib import Path

path = Path('to_convert')

if __name__ == '__main__':
    path.mkdir(parents=True, exist_ok=True)
    
    images = sorted(os.listdir(path))
    images = [Image.open(path / f) for f in images]
    
    pdf_name = input("write name of the file> ")
    pdf_name = pdf_name.strip("'").strip('"').replace('.pdf', '')

    images[0].save(f'{pdf_name}.pdf',
                   "PDF",
                   resolution=100.0, 
                   save_all=True, 
                   append_images=images[1:])
