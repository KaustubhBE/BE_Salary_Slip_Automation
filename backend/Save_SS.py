import os
from datetime import datetime

def save_salary_slip_in_folder(pdf_path, folder_id, employee_name):

    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().strftime("%Y")
    
    # Create folder structure if it does not exist
    target_folder = os.path.join(folder_id, current_year, current_month)
    os.makedirs(target_folder, exist_ok=True)
    
    # Save the PDF to the target folder
    target_pdf_path = os.path.join(target_folder, f"{employee_name}_Salary_Slip.pdf")
    os.rename(pdf_path, target_pdf_path)  # Move the PDF to the correct folder
    print(f"Salary slip saved for {employee_name} at {target_pdf_path}")
