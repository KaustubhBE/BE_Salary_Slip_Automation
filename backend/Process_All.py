from Process_SS import process_salary_slips

# Example usage
sheet_id = "Place your sheet id here"
sheet_name = "Sheet1"
credentials_file = r"C:\Users\Kaustubh\Desktop\BE_Salary_Slip_Automation\backend\credentials.json"
template_path = r"backend\ssformat.docx"
output_base_dir = r"C:\Users\Kaustubh\Desktop\BE_Salary_Slip_Automation\backend\Salary_Slips"

process_salary_slips(sheet_id, sheet_name, credentials_file, template_path, output_base_dir)
