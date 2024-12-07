from Fetch_Data import fetch_google_sheet_data
from Generate_SS import generate_salary_slip
from Save_SS import save_salary_slip_in_folder
from Convert_DOC_to_PDF import convert_docx_to_pdf
import os
from datetime import datetime
import time
import re
from datetime import datetime
import os

def process_salary_slips(sheet_id, sheet_name, credentials_file, template_path, output_base_dir):
    
    # Fetch data from Google Sheet
    data = fetch_google_sheet_data(sheet_id, sheet_name, credentials_file)
    
    if data:
        headers = data[0]  # First row contains headers/placeholders
        employees = data[1:]  # Remaining rows contain employee data

        # Get the current date and calculate the previous month
        current_date = datetime.now()
        previous_month = current_date.month - 1 if current_date.month > 1 else 12
        year = current_date.year if previous_month != 12 else current_date.year - 1
        
        # Get the previous month name as the first three letters
        previous_month_name = datetime(year, previous_month, 1).strftime('%b')
        
        # Format the folder name as 'mon-yy'
        previous_month_str = f"{previous_month_name}-{year % 100:02d}"
        
        for employee_data in employees:
            try:
                # Generate the salary slip for the employee
                template = generate_salary_slip(template_path, employee_data, headers)
                
                # Create a temporary DOCX file for the salary slip
                employee_name = employee_data[0]
                temp_docx_path = os.path.join(output_base_dir, f"{employee_name}_Salary_Slip.docx")
                template.save(temp_docx_path)
                
                # Convert the DOCX file to PDF
                temp_pdf_path = temp_docx_path.replace('.docx', '.pdf')
                convert_docx_to_pdf(temp_docx_path, temp_pdf_path)
                
                # Save the PDF in the appropriate folder
                folder_id = employee_data[2]  # Assuming folder ID is in the third column
                employee_folder_path = os.path.join(output_base_dir, f"{employee_name}_{previous_month_str}_Salary_Slip")
                
                # Create the folder if it doesn't exist
                os.makedirs(employee_folder_path, exist_ok=True)
                
                # Save the PDF inside the employee's folder
                final_pdf_path = os.path.join(employee_folder_path, f"{employee_name}_{previous_month_str}_Salary_Slip.pdf")
                save_salary_slip_in_folder(temp_pdf_path, folder_id, final_pdf_path)
                
                # Clean up temporary DOCX file
                os.remove(temp_docx_path)
            except Exception as e:
                print(f"Error processing salary slip for {employee_data[0]}: {e}")
    else:
        print("No data fetched from the Google Sheet.")