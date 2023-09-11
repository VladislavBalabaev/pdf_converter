import os
from PIL import Image
from pathlib import Path

path = Path('to_convert')

if __name__ == '__main__':
    if not path.is_dir():
        path.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError('Please, add your images to newly created "to_convert" directory.')

    images = sorted(os.listdir(path))
    images = [Image.open(path / f) for f in images]

    pdf_name = input("write name of the file> ")
    pdf_name = pdf_name.strip("'").strip('"').replace('.pdf', '')
    pdf_name = f'{pdf_name}.pdf'


    images[0].save(pdf_name,
                   "PDF",
                   resolution=100.0, 
                   save_all=True, 
                   append_images=images[1:])

    print(f'{pdf_name} has been created.')

    exit()
