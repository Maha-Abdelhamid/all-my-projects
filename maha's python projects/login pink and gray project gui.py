

subject_list = []
study_days_list = []
studying_time_NOTlist = 0



def enter_data():
    global studying_time_NOTlist
    study_days_list.clear()
    subject_list.clear()
    

    if sunday_var.get() == "confirmed":
        study_days_list.append("Sunday")


    if monday_var.get() == "confirmed":
        study_days_list.append("Monday")


    if tuesday_var.get() == "confirmed":
        study_days_list.append("Tuesday")


    if wednesday_var.get() == "confirmed":
        study_days_list.append("Wednesday")


    if thursday_var.get() == "confirmed":
        study_days_list.append("Thursday")


    time_value = study_spinbox.get().strip()

    if time_value.isdigit():
        studying_time_NOTlist = int(time_value)

    else:
        messagebox.showerror("Error", "Please enter a valid number for study hours")
        return


    selected_indices = subjects_listbox.curselection()

    for index in selected_indices:
        subject_list.append(subjects_listbox.get(index))


    if not study_days_list or not subject_list or studying_time_NOTlist == 0:
        messagebox.showerror("Error", "Please select study days, subjects, and valid study hours.")
        return





