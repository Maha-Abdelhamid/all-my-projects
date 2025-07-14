import tkinter
from tkinter import messagebox
import itertools
import tkinter.commondialog
from PIL import ImageTk

filepath=(r"c:\Users\pc1\Desktop\movie1.jpg")



used_color="#D2e0d3"



window = tkinter.Tk()
window.title("Studying Time Allocation")
window.configure(bg=used_color)



frame = tkinter.Frame(window)


def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

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

    clear(frame)
    load_frame2()


 #dcb3a0
import tkinter as tkinter
import itertools
from PIL import ImageTk

def load_frame2():
    clear(frame)  

    schedule_frame = tkinter.LabelFrame(frame, text="Your Study Schedule", bg=used_color)
    schedule_frame.grid(padx=20, pady=10)

    
    study_schedule = {}
    subject_cycle = itertools.cycle(subject_list)


    for day in study_days_list:
        study_schedule[day] = []

        for _ in range(len(subject_list) // len(study_days_list) + (1 if len(subject_list) % len(study_days_list) > study_days_list.index(day) else 0)):
            study_schedule[day].append(next(subject_cycle))


    for day, subjects in study_schedule.items():
        subjects_with_hours = []

        if subjects:
            study_hours_per_subject = studying_time_NOTlist / len(subjects)
        else:
            study_hours_per_subject = 0
        
        for subject in subjects:
            display_time = f"{int(study_hours_per_subject)}h" if study_hours_per_subject >= 1 else f"{int(study_hours_per_subject * 60)} minutes"
            subjects_with_hours.append(f"{subject} ({display_time})")

        day_label = tkinter.Label(schedule_frame, text=f"{day}: {', '.join(subjects_with_hours)}", font=("Arial", 14),bg=used_color)
        day_label.grid(pady=5)

    back_button = tkinter.Button(frame,activebackground=used_color,bg="#fafcfa", text="Back", command=lambda: load_frame1())
    day_label.grid(pady=5, sticky="w")  


    logo_image = ImageTk.PhotoImage(file=filepath)

    logo_widget = tkinter.Label(frame, image=logo_image)
    logo_widget.image = logo_image  
    logo_widget.grid(pady=10)  

    # Add Back button to return to the previous frame
    back_button = tkinter.Button(frame, fg=used_color, text="Back", command=lambda: load_frame1(), bg="#fafcfa", font=30)



    back_button.grid(pady=10)



def load_frame1():
    frame.configure(bg=used_color)

    clear(frame)

    

    global study_spinbox, subjects_listbox
    global sunday_var, monday_var, tuesday_var, wednesday_var, thursday_var
    
    
    user_info_frame = tkinter.LabelFrame(frame,bg=used_color,text="Choose your available study days and hours")
    user_info_frame.grid(padx=20, pady=10)
    user_info_frame.configure(bg=used_color)

    sunday_var = tkinter.StringVar(value="not confirmed")
        
    monday_var = tkinter.StringVar(value="not confirmed")
    
    tuesday_var = tkinter.StringVar(value="not confirmed")
    
    wednesday_var = tkinter.StringVar(value="not confirmed")
    
    thursday_var = tkinter.StringVar(value="not confirmed")

    


    days = [("Sunday", sunday_var),
            ("Monday", monday_var), 
            ("Tuesday", tuesday_var),
            ("Wednesday", wednesday_var), 
            ("Thursday", thursday_var)]

    for i, (day, var) in enumerate(days):
        tkinter.Checkbutton(user_info_frame, bg=used_color,text=day, variable=var, onvalue="confirmed", offvalue="not confirmed").grid(row=0, column=i)


    study_time_label = tkinter.Label(user_info_frame, text="Study hours per day:",bg=used_color)
    study_time_label.grid(row=1, column=0, padx=10, pady=5)
    

    study_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=9)
    study_spinbox.grid(row=1, column=1, padx=10, pady=5)

    font = ('Arial', 25)
    courses_frame = tkinter.LabelFrame(frame, text="Choose subjects to study",bg=used_color,font=font)
    courses_frame.grid(padx=20, pady=10)
    courses_frame.configure(bg=used_color)

    
    
    font_2 = ('Arial', 20)

    subjects_listbox = tkinter.Listbox(courses_frame, selectmode="multiple",font=font_2)
    subjects_listbox.grid(padx=10, pady=10)



    all_subjects = ["Math", "English", "Arabic", "Social Studies", "Computer", "Science"]
    for subject in all_subjects:
        subjects_listbox.insert(tkinter.END, subject,)


    button = tkinter.Button(frame, text="Confirm", font=25,command=lambda: enter_data(),bg=used_color)
    button.grid(pady=10)
    

    
  

    

def login():
    clear(frame)
    frame.configure(bg=used_color)



    def check_login():
        if "@" in email_entry.get() and username_entry.get():
            clear(frame)
            load_frame1()
        else:
            messagebox.showerror("Error", "Invalid username or email")


    login_label = tkinter.Label(frame,fg="#fafcfa",text="Login to Study App", font=("Arial", 50), pady=20,bg=used_color)


    username_label = tkinter.Label(frame, text="Username:", font=("Arial", 30))

    username_entry = tkinter.Entry(frame, font=("Arial", 30))


    email_label = tkinter.Label(frame, text="Email:", font=("Arial", 30))

    email_entry = tkinter.Entry(frame, font=("Arial", 30))

    login_button = tkinter.Button(frame, text="Login", font=("Arial", 30), command=lambda:check_login())



#----------------------------------grid all characters---------------------------------------------


    login_label.grid(row=0,column=0,columnspan=2,sticky="news")

    username_label.grid(row=1,column=0,pady=20)

    username_entry.grid(row=1,column=1,pady=20)
    email_label.grid(row=2,column=0)

    email_entry.grid(row=2,column=1,pady=20,padx=20)
    login_button.grid(row=3,column=0,columnspan=2,pady=20)
    

frame.pack()
login()
window.mainloop()