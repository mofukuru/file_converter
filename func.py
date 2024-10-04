import img2pdf
from PIL import Image

class Converter:
    def __init__(self, image_file, pdf_file=None):
        self.image_file = image_file

        if pdf_file == None:
            self.pdf_file = self.image_file.split(".")[0]+".pdf"
        else:
            self.pdf_file = pdf_file

    def img_to_pdf(self):
        with open(self.pdf_file, "wb") as f:
            f.write(img2pdf.convert(Image.open(self.image_file).filename))
