import comtypes.client
import os

def convert_docx_to_pdf(input_path, output_path):
    
    if not os.path.exists(input_path):
        print(f"File does not exist: {input_path}")
        return
    
    try:
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(input_path)
        doc.SaveAs(output_path, FileFormat=17)  # 17 stands for PDF
        doc.Close()
        word.Quit()
        print(f"PDF successfully created at {output_path}")
    except Exception as e:
        print(f"Error converting to PDF for {input_path}: {e}")

