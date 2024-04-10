from PDFGenderator.Template1 import Template1
import json

# Usage example
if __name__ == "__main__":
    with open("Data/resume.json", 'r') as file:
        resume = json.loads(file.read())
    pdf_generator = Template1("Data/resume.pdf",resumeData=resume)
    pdf_generator.create_pdf()
    pdf_generator.save()
