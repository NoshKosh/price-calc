import tkinter as tk
from tkinter import ttk




def update_certificates_input():
    if certificates_var.get():
        wanted_documents_label.grid(row=10, column=0, padx=10, pady=5)
        wanted_documents_entry.grid(row=10, column=1, padx=10, pady=5)
    else:
        wanted_documents_label.grid_forget()
        wanted_documents_entry.grid_forget()

def calculate_price_left():
    try:
        num_employees = max(int(employees_entry_left.get()), 100)
        num_documents = max(int(documents_entry_left.get()), 500)
        num_managers = max(int(managers_entry_left.get()), 10)
        use_certificates = certificates_var.get()
        
        if use_certificates:
            num_wanted_documents = max(int(wanted_documents_entry.get()), 0)
        else:
            num_wanted_documents = 0

        base_price_per_employee = 6000
        base_price_per_document = 1200
        base_price_per_manager = 7800

        # Calculate additional costs for employees, documents, managers, and certifications
        additional_employee_cost = base_price_per_employee
        num_employees_over_100 = max((num_employees // 100 - 1), 0)
        for _ in range(num_employees_over_100):
            increase = additional_employee_cost * 0.027
            additional_employee_cost += increase

        additional_document_cost = base_price_per_document + (max(((num_documents - 500) // 500) * 300, 0))
        additional_manager_cost = base_price_per_manager
        num_managers_over_10 = max(((num_managers // 5) - 2), 0)
        additional_manager_cost += (num_managers_over_10 * (base_price_per_manager * 0.285))

        # Calculate additional cost for certifications if selected
        if use_certificates:
            num_certifications = num_employees * num_wanted_documents
            if num_certifications != 0 and num_certifications < 10000:
                additional_certifications_cost = 2500
            else:
                 additional_certifications_cost = (num_certifications // 10000) * 2500
        else:
            additional_certifications_cost = 0

        unit_price_manager = (additional_manager_cost / num_managers) / 12

        total_price = additional_employee_cost + \
                      additional_document_cost + \
                      additional_manager_cost + additional_certifications_cost

        # Ensure the total price is not lower than $15,000
        total_price = max(total_price, 15000)

        # Update the total price label first
        result_label_left.config(text=f"Total: ${total_price:.2f}")

        # Update labels to display the prices of additional components
        additional_employee_label_left.config(text=f"{additional_employee_cost:.2f}")
        additional_document_label_left.config(text=f"{additional_document_cost:.2f}")
        additional_manager_label_left.config(text=f" {additional_manager_cost:.2f}")
        if certificates_var.get():
            additional_certifications_label_left.grid(row=10, column=2, padx=10, pady=5, columnspan=2)
            additional_certifications_label_left.config(text=f"{additional_certifications_cost:.2f}")
        else:
            additional_certifications_label_left.grid_forget()
            


        


        # Display unit_price_manager
        unit_price_manager_label_left.config(text=f"{unit_price_manager:.2f}")

    except ValueError:
        result_label_left.config(text="Invalid input!")

def calculate_price_right():
    try:
        num_employees = max(int(employees_entry_right.get()), 100)
        num_documents = max(int(documents_entry_right.get()), 500)
        num_managers = max(int(managers_entry_right.get()), 10)
        num_submitters = max(int(submitters_entry_right.get()), 10)
        use_ocr = ocr_var.get()
        use_ai = ai_var.get()
        use_crm = crm_var.get()

        base_price_per_employee = 6000
        base_price_per_document = 1200
        base_price_per_manager = 7800
        base_price_per_submitter = 1200

        # Calculate additional costs for employees, documents, managers, and certifications
        additional_employee_cost = base_price_per_employee
        num_employees_over_100 = max((num_employees // 100 - 1), 0)
        for _ in range(num_employees_over_100):
            increase = additional_employee_cost * 0.027
            additional_employee_cost += increase
        
        additional_document_cost = base_price_per_document + (max(((num_documents - 500) // 500) * 300, 0))
        additional_manager_cost = base_price_per_manager
        num_managers_over_10 = max(((num_managers // 5.0) - 2.0), 0)
        additional_manager_cost += (num_managers_over_10 * (base_price_per_manager * 0.285))
        additional_submitter_cost = base_price_per_submitter
        num_submitter_over_10 = max(((num_submitters // 5.0) - 2.0), 0)
        
        additional_submitter_cost += (num_submitter_over_10 * (base_price_per_submitter * 0.285))
        # Calculate additional cost for OCR if selected
        if use_ocr:
            num_ocr_documents = num_documents
            additional_ocr_cost = 1800 + (max(((num_ocr_documents - 500) // 500), 0) * 300)
        else:
            additional_ocr_cost = 0

        # Calculate additional cost for AI if selected
        if use_ai:
            num_ai_documents = num_documents
            additional_ai_cost = 2000 + (max(((num_ai_documents - 500) // 500), 0) * 500)
        else:
            additional_ai_cost = 0

        # Calculate additional cost for CRM if selected
        if use_crm:
            additional_crm_cost = (num_managers + num_submitters) * 150
        else:
            additional_crm_cost = 0

        unit_price_manager = (additional_manager_cost / num_managers) / 12

        total_price = additional_employee_cost + \
                      additional_document_cost + \
                      additional_manager_cost + additional_ocr_cost + additional_ai_cost + \
                      additional_crm_cost + additional_submitter_cost

        # Ensure the total price is not lower than $15,000
        total_price = max(total_price, 15000)

        # Update labels to display the prices of additional components
        additional_employee_label_right.config(text=f"{additional_employee_cost:.2f}")
        additional_document_label_right.config(text=f"{additional_document_cost:.2f}")
        additional_manager_label_right.config(text=f"{additional_manager_cost:.2f}")
        if ocr_var.get():
            additional_ocr_label_right.grid(row=10, column=2, padx=10, pady=5, columnspan=2)
            additional_ocr_label_right.config(text=f"{additional_ocr_cost:.2f}")
        else:
            additional_ocr_label_right.grid_forget()
        
        if ai_var.get():
            additional_ai_label_right.grid(row=11, column=2, padx=10, pady=5, columnspan=2)
            additional_ai_label_right.config(text=f"{additional_ai_cost:.2f}")
        else:
            additional_ai_label_right.grid_forget()

        additional_submitter_label_right.config(text=f"{additional_submitter_cost:.2f}")
        if crm_var.get():
            additional_crm_label_right.grid(row=12, column=2, padx=10, pady=5, columnspan=2)
            additional_crm_label_right.config(text=f"{additional_crm_cost:.2f}")
        else:
            additional_crm_label_right.grid_forget()

        # Display unit_price_manager
        unit_price_manager_label_right.config(text=f"{unit_price_manager:.2f}")

        # Update the total price label
        result_label_right.config(text=f"Total: ${total_price:.2f}")

    except ValueError:
        result_label_right.config(text="Invalid input!")

def go_back_to_welcome():
    left_frame.grid_forget()
    right_frame.grid_forget()
    welcome_frame.grid(row=0, column=0, columnspan=4)

def show_left_calculator():
    welcome_frame.grid_forget()
    right_frame.grid_forget()
    left_frame.grid(row=0, column=1)

def show_right_calculator():
    welcome_frame.grid_forget()
    left_frame.grid_forget()
    right_frame.grid(row=0, column=1)
def show_tell():
    if certificates_var.get():
        additional_certifications_label_left.grid(row=10, column=2, padx=10, pady=5, columnspan=2)
    else:
        additional_certifications_label_left.grid_forget()

app = tk.Tk()
app.title("Software Price Calculator")

# Welcome page UI components
welcome_frame = ttk.Frame(app)
welcome_frame.grid(row=0, column=0, columnspan=4)

welcome_label = ttk.Label(welcome_frame, text="Welcome to ConvergePoint!")
welcome_label.grid(row=0, column=0, padx=10, pady=5, columnspan=4)

left_button = ttk.Button(welcome_frame, text="Policy Management", command=show_left_calculator)
left_button.grid(row=1, column=0, padx=10, pady=5)

right_button = ttk.Button(welcome_frame, text="Contract Management", command=show_right_calculator)
right_button.grid(row=1, column=1, padx=10, pady=5)

# Left calculator UI components
left_frame = ttk.Frame(app)

empty_header_label_left = ttk.Label(left_frame, text="")
empty_header_label_left.grid(row=5, column=0, padx=10, pady=5)

metrics_header_label_left = ttk.Label(left_frame, text="Metrics")
metrics_header_label_left.grid(row=5, column=1, padx=10, pady=5)

cost_by_item_header_label_left = ttk.Label(left_frame, text="Cost by Item")
cost_by_item_header_label_left.grid(row=5, column=3, padx=10, pady=5)

unit_cost_header_label_left = ttk.Label(left_frame, text="Unit Cost")
unit_cost_header_label_left.grid(row=5, column=4, padx=10, pady=5)

employees_label_left = ttk.Label(left_frame, text="Number of Employees:")
employees_label_left.grid(row=6, column=0, padx=10, pady=5)
employees_entry_left = ttk.Entry(left_frame)
employees_entry_left.grid(row = 6, column=1, padx=10, pady=5)

# ... (Rest of the left calculator components)
documents_label_left = ttk.Label(left_frame, text="Number of Documents:")
documents_label_left.grid(row=7, column=0, padx=10, pady=5)
documents_entry_left = ttk.Entry(left_frame)
documents_entry_left.grid(row=7, column=1, padx=10, pady=5)

managers_label_left = ttk.Label(left_frame, text="Number of Managers:")
managers_label_left.grid(row=8, column=0, padx=10, pady=5)
managers_entry_left = ttk.Entry(left_frame)
managers_entry_left.grid(row=8, column=1, padx=10, pady=5)

certificates_label_left = ttk.Label(left_frame, text="Use Certificates:")
certificates_label_left.grid(row=9, column=0, padx=10, pady=5)
certificates_var = tk.BooleanVar()
certificates_var.set(False)  # Default value: No
certificates_button_left = ttk.Checkbutton(left_frame, variable=certificates_var, onvalue=True, offvalue=False, command=update_certificates_input)
certificates_button_left.grid(row=9, column=1, padx=10, pady=5)

wanted_documents_label = ttk.Label(left_frame, text="Wanted Documents:")


wanted_documents_entry = ttk.Entry(left_frame)



calculate_button_left = ttk.Button(left_frame, text="Calculate", command=calculate_price_left)
calculate_button_left.grid(row=11, column=0, padx=10, pady=5, columnspan=1)

# Labels to display the additional component prices (Duplicated from left calculator)
additional_employee_label_left = ttk.Label(left_frame, text="")
additional_employee_label_left.grid(row=6, column=2, padx=10, pady=5, columnspan=2)

additional_document_label_left = ttk.Label(left_frame, text="")
additional_document_label_left.grid(row=7, column=2, padx=10, pady=5, columnspan=2)

additional_manager_label_left = ttk.Label(left_frame, text="")
additional_manager_label_left.grid(row=8, column=2, padx=10, pady=5, columnspan=2)

additional_certifications_label_left = ttk.Label(left_frame, text="")


# Label to display unit_price_manager
unit_price_manager_label_left = ttk.Label(left_frame, text="")
unit_price_manager_label_left.grid(row=8, column=4, padx=10, pady=5, columnspan=1)

result_label_left = ttk.Label(left_frame, text="")
result_label_left.grid(row=11, column=1, padx=10, pady=5, columnspan=2)

go_back_left_button = ttk.Button(left_frame, text="Go Back", command=go_back_to_welcome)
go_back_left_button.grid(row=25, column=5, padx=10, pady=5, columnspan=2)

# Right calculator UI components
right_frame = ttk.Frame(app)

empty_header_label_right = ttk.Label(right_frame, text="")
empty_header_label_right.grid(row=5, column=0, padx=10, pady=5)

metrics_header_label_right = ttk.Label(right_frame, text="Metrics")
metrics_header_label_right.grid(row=5, column=1, padx=10, pady=5)

cost_by_item_header_label_right = ttk.Label(right_frame, text="Cost by Item")
cost_by_item_header_label_right.grid(row=5, column=3, padx=10, pady=5)

unit_cost_header_label_right = ttk.Label(right_frame, text="Unit Cost")
unit_cost_header_label_right.grid(row=5, column=4, padx=10, pady=5)

employees_label_right = ttk.Label(right_frame, text="Number of Employees:")
employees_label_right.grid(row=6, column=0, padx=10, pady=5)
employees_entry_right = ttk.Entry(right_frame)
employees_entry_right.grid(row=6, column=1, padx=10, pady=5)

# ... (Rest of the right calculator components)
documents_label_right = ttk.Label(right_frame, text="Number of Documents:")
documents_label_right.grid(row=7, column=0, padx=10, pady=5)
documents_entry_right = ttk.Entry(right_frame)
documents_entry_right.grid(row=7, column=1, padx=10, pady=5)

managers_label_right = ttk.Label(right_frame, text="Number of Managers:")
managers_label_right.grid(row=8, column=0, padx=10, pady=5)
managers_entry_right = ttk.Entry(right_frame)
managers_entry_right.grid(row =8, column=1, padx=10, pady=5)

submitters_label_right = ttk.Label(right_frame, text="Number of Submitters:")
submitters_label_right.grid(row=9, column=0, padx=10, pady=5)
submitters_entry_right = ttk.Entry(right_frame)
submitters_entry_right.insert(0, "0")  # Default value: 0
submitters_entry_right.grid(row=9, column=1, padx=10, pady=5)

ocr_label_right = ttk.Label(right_frame, text="OCR:")
ocr_label_right.grid(row=10, column=0, padx=10, pady=5)
ocr_var = tk.BooleanVar()
ocr_var.set(False)  # Default value: No
ocr_button_right = ttk.Checkbutton(right_frame, variable=ocr_var, onvalue=True, offvalue=False, command=calculate_price_right)
ocr_button_right.grid(row=10, column=1, padx=10, pady=5)

ai_label_right = ttk.Label(right_frame, text="AI:")
ai_label_right.grid(row=11, column=0, padx=10, pady=5)
ai_var = tk.BooleanVar()
ai_var.set(False)  # Default value: No
ai_button_right = ttk.Checkbutton(right_frame, variable=ai_var, onvalue=True, offvalue=False, command=calculate_price_right)
ai_button_right.grid(row=11, column=1, padx=10, pady=5)

crm_label_right = ttk.Label(right_frame, text="CRM:")
crm_label_right.grid(row=12, column=0, padx=10, pady=5)
crm_var = tk.BooleanVar()
crm_var.set(False)  # Default value: No
crm_button_right = ttk.Checkbutton(right_frame, variable=crm_var, onvalue=True, offvalue=False, command=calculate_price_right)
crm_button_right.grid(row=12, column=1, padx=10, pady=5)

calculate_button_right = ttk.Button(right_frame, text="Calculate Price", command=calculate_price_right)
calculate_button_right.grid(row=18, column=0, padx=10, pady=5, columnspan=1)

# Labels to display the additional component prices (Duplicated from right calculator)
additional_employee_label_right = ttk.Label(right_frame, text="")
additional_employee_label_right.grid(row=6, column=2, padx=10, pady=5, columnspan=2)

additional_document_label_right = ttk.Label(right_frame, text="")
additional_document_label_right.grid(row=7, column=2, padx=10, pady=5, columnspan=2)

additional_manager_label_right = ttk.Label(right_frame, text="")
additional_manager_label_right.grid(row=8, column=2, padx=10, pady=5, columnspan=2)

additional_ocr_label_right = ttk.Label(right_frame, text="")


additional_ai_label_right = ttk.Label(right_frame, text="")


additional_submitter_label_right = ttk.Label(right_frame, text="")
additional_submitter_label_right.grid(row=9, column=2, padx=10, pady=5, columnspan=2)

additional_crm_label_right = ttk.Label(right_frame, text="")


# Label to display unit_price_manager
unit_price_manager_label_right = ttk.Label(right_frame, text="")
unit_price_manager_label_right.grid(row=8, column=4, padx=10, pady=5, columnspan=1)


result_label_right = ttk.Label(right_frame, text="")
result_label_right.grid(row=14, column=1, padx=10, pady=5, columnspan=1)

go_back_right_button = ttk.Button(right_frame, text="Go Back", command=go_back_to_welcome)
go_back_right_button.grid(row=25, column=5, padx=10, pady=5, columnspan=2)

app.mainloop()