from tkinter import *
from PIL import ImageTk
import random
from tkinter import messagebox

# Define color themes
red = ["#BD726E", "#ffffff", "#7d4545"]
pink = ["#f8e3f6", "#e7a8d7", "#ad8baa"]

all_color_groups = [red, pink]
used_color = random.choice(all_color_groups)

root = Tk()
root.title("Recipes App")
root.geometry("900x700")
root.configure(bg=used_color[0])

mainframe = Frame(root, bg=used_color[0])
fram = Frame(mainframe, bg=used_color[0])

removed_recipes = []
fav_recipes = []
recipes = [
    ("Asparagus Pasta with Pesto", "1) pasta noodle\n2) asparagus\n3) garlic\n4) olive oil\n5) onion basil\n6) parmesan cheese"),
    ("Italian Rice and Peas", "1) Frozen pea\n2) long-grain rice\n3) onion\n4) celery\n5) dry white wine\n6) boiling water\n7) chicken stock cube butter\n8) parmesan cheese\n9) salt and pepper"),
    ("Orecchiette With Spinach, Garlic and Bacon", "1) frozen spinach\n2) bacon\n3) onion\n4) garlic\n5) olive oil\n6) orecchiette pasta\n7) salt and pepper"),
    ("Pasta With Green Olives, Bacon, Mushroom and Artichoke", "1) penne pasta\n2) green olive\n3) bacon\n4) mushroom\n5) artichoke\n6) spaghetti sauce\n7) dry white wine\n8) oregano\n9) garlic powder onion powder\n10) basil"),
    ("Spaghetti Sauce", "1) tomato and tomato sauce\n2) salt\n3) tomato paste\n4) ground beef\n5) onion\n6) mushroom\n7) green bell pepper\n8) garlic\n9) oregano basil\n10) parmesan cheese\n11) pepper")
]

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def user_login():
    clear(fram)

    def login():
        if "@" in email_entry.get() and username_entry.get():
            load_frame1()
        elif "@" not in email_entry.get():
            messagebox.showerror("ERROR", "Invalid Email")
        else:
            messagebox.showerror("ERROR", "Please enter a username")

    Label(fram, text="Login To Recipes App", bg=used_color[0], fg="white", font=("Arial", 30)).grid(pady=20)
    Label(fram, text="Username", bg=used_color[0], fg="white", font=("Arial", 16)).grid(pady=5)
    username_entry = Entry(fram, font=("Arial", 16))
    username_entry.grid(pady=5)

    Label(fram, text="Email", bg=used_color[0], fg="white", font=("Arial", 16)).grid(pady=5)
    email_entry = Entry(fram, font=("Arial", 16))
    email_entry.grid(pady=5)

    Button(fram, text="Login", bg=used_color[1], fg="white", font=("Arial", 16), command=login).grid(pady=20)

def load_frame1():
    clear(fram)
    try:
        logo_image = ImageTk.PhotoImage(file=r"c:\Users\pc1\Downloads\eat_v-removebg-preview.png")
        logo_widget = Label(fram, image=logo_image, bg=used_color[0])
        logo_widget.image = logo_image
        logo_widget.grid()
    except:
        pass  # Skip image if path is invalid

    Label(fram, text="Ready To Shuffle Recipes?", font=("", 20), bg=used_color[0], fg="white").grid(pady=10)
    Button(fram, text="SHUFFLE", font=("", 25), bg=used_color[2], fg="white", command=load_frame2).grid(pady=10)
    Button(fram, text="See Favorite Recipes", bg=used_color[1], command=load_frame3).grid(pady=10)
    Button(fram, text="See Removed Recipes", bg=used_color[1], command=load_frame4).grid(pady=10)

def load_frame2():
    clear(fram)
    available = [r for r in recipes if r not in removed_recipes]
    if not available:
        Label(fram, text="No recipes left!", bg=used_color[0], fg="white").grid(pady=20)
        Button(fram, text="Back", bg=used_color[1], command=load_frame1).grid(pady=10)
        return

    recipe = random.choice(available)
    recipe_name, recipe_ingred = recipe

    try:
        logo_image = ImageTk.PhotoImage(file=r"c:\Users\pc1\Downloads\eat_v-removebg-preview.png")
        logo_widget = Label(fram, image=logo_image, bg=used_color[0])
        logo_widget.image = logo_image
        logo_widget.grid()
    except:
        pass

    Label(fram, text=recipe_name, font=("", 25), bg=used_color[0], fg="white").grid(pady=10)
    Label(fram, text=recipe_ingred, font=("", 14), bg=used_color[2], fg="white").grid(pady=10)

    def toggle_favorite():
        if recipe in fav_recipes:
            fav_recipes.remove(recipe)
        else:
            fav_recipes.append(recipe)
        load_frame1()

    fav_button_text = "Remove From Favorite" if recipe in fav_recipes else "Add To Favorite"
    O = 0 if recipe in fav_recipes else 1
    Button(fram, text=fav_button_text, bg=used_color[O], command=toggle_favorite).grid(pady=5)
    Button(fram, text="Don't Show Again", bg="salmon", command=lambda: remove_recipe(recipe)).grid(pady=5)
    Button(fram, text="Back", bg=used_color[1], command=load_frame1).grid(pady=20)

def remove_recipe(recipe):
    if recipe in recipes and recipe not in removed_recipes:
        removed_recipes.append(recipe)
    load_frame1()

def load_frame3():
    clear(fram)
    Label(fram, text="Favorite Recipes", font=("", 20), bg=used_color[0], fg="white").grid(pady=10)
    if not fav_recipes:
        Label(fram, text="No favorites yet.", bg=used_color[0], fg="white").grid(pady=5)
    for recipe_name, _ in fav_recipes:
        frame = Frame(fram, bg=used_color[0])
        frame.grid(pady=5)
        Label(frame, text=recipe_name, bg=used_color[1], fg="white", width=40).grid()
        Button(frame, text="Remove", bg="salmon", command=lambda r=(recipe_name, _): remove_from_favorite(r)).grid()

    Button(fram, text="Back", bg="oldlace", fg=used_color[0], command=load_frame1).grid(pady=20)

def remove_from_favorite(recipe):
    if recipe in fav_recipes:
        fav_recipes.remove(recipe)
    load_frame3()

def load_frame4():
    clear(fram)
    Label(fram, text="Removed Recipes", font=("", 20), bg=used_color[0], fg="white").grid(pady=10)
    if not removed_recipes:
        Label(fram, text="No removed recipes.", bg=used_color[0], fg="white").grid(pady=5)
    for recipe_name, _ in removed_recipes:
        frame = Frame(fram, bg=used_color[0])
        frame.grid(pady=5)
        Label(frame, text=recipe_name, bg="salmon", fg="white", width=40).grid()
        Button(frame, text="Restore", bg=used_color[1], command=lambda r=(recipe_name, _): restore_recipe(r)).grid()

    Button(fram, text="Back", bg="oldlace", fg=used_color[0], command=load_frame1).grid(pady=20)

def restore_recipe(recipe):
    if recipe in removed_recipes:
        removed_recipes.remove(recipe)
    load_frame4()

user_login()
fram.pack()
mainframe.pack()
root.mainloop()

