from django.conf import settings
import uuid
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from io import BytesIO  
import os

def save_pdf(params:dict):
    template = get_template('pdf.html')
    html = template.render(params)
    # pdf = pisa.pisaDocument(BytesIO(html.encode('utf-8')),response)
    file_name = uuid.uuid4()
    file_path =os.path.join(settings.MEDIA_ROOT, f"{file_name}.pdf")
    try:
        with open(file_path,"wb+") as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('utf-8')),output)
    except Exception as e:
        print(e)
    
    if pdf.err :
        return "" , False
    
    return file_name , True
