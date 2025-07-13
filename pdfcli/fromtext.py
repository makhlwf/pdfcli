from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def from_text(output_path, input_path=None, text_content=None):
    if input_path:
        with open(input_path, 'r') as f:
            text = f.read()
    elif text_content:
        text = text_content
    else:
        raise ValueError("Either input_path or text_content must be provided.")

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    text_object = c.beginText(40, height - 40)
    for line in text.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()
