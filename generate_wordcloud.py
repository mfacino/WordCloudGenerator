import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog

# --- Setup file selection - prompt user to select csv ---
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select CSV file",
    filetypes=[("CSV files", "*.csv")]
)

if not file_path:
    raise FileNotFoundError("No file was selected.")

# --- Load and process the CSV ---
df = pd.read_csv(file_path)

# define the column to use for the word cloud - change as needed *CASE-SENSITIVE*
title_column = 'Title'

if title_column not in df.columns:
    raise ValueError(f"Column '{title_column}' not found. Available columns: {list(df.columns)}")

# --- Normalize text: lowercase and concatenate ---
titles_text = ' '.join(df[title_column].dropna().astype(str).str.lower().values)

# --- Optional: ask if user wants to use a custom shape ---
use_mask = messagebox.askyesno("Use Shape Mask", "Would you like to use a custom image shape for the word cloud?")

mask = None
if use_mask:
    mask_path = filedialog.askopenfilename(
        title="Select Mask Image (PNG/JPG)",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if not mask_path:
        raise FileNotFoundError("You selected 'yes' but did not choose an image.")

    mask_image = Image.open(mask_path).convert('L')  # Grayscale
    mask = np.array(mask_image)
    if np.sum(mask > 0) < mask.size * 0.05:
        messagebox.showerror(
            "Mask Error",
            "The selected image does not provide enough drawable space for a word cloud.\n"
            "Please use a silhouette-style image with a dark shape on a white background."
        )
        exit()

# --- Optional: ask user to select a font file ---
use_font = messagebox.askyesno("Custom Font", "Would you like to use a custom font?")
font_path = None
if use_font:
    font_path = filedialog.askopenfilename(
        title="Select Font File (.ttf or .otf)",
        filetypes=[("Font files", "*.ttf *.otf")]
    )
    if not font_path:
        messagebox.showwarning("Font Warning", "No font selected. Default font will be used.")
        font_path = None

# --- Optional: define a color function ---
import random

color_func = None  # Default behavior (WordCloud's internal coloring)

color_mode = messagebox.askquestion(
    "Color Scheme",
    "Would you like to choose a color scheme?\n\nYes = Customize colors\nNo = Use default WordCloud colors",
    icon='question'
)

if color_mode == 'yes':
    scheme_type = messagebox.askquestion(
        "Color Scheme Type",
        "Choose a color scheme type:\n\nYes = Single color\nNo = Multicolor or Random",
        icon='question'
    )

    if scheme_type == 'yes':
        user_color = simpledialog.askstring(
            "Color Input",
            "Enter a single color (name or hex, e.g., 'green' or '#00ff00')"
        )

        if user_color:
            def color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
                return user_color
    else:
        use_random = messagebox.askyesno("Multicolor Mode", "Use fully random colors? (No = Multicolor preset)")

        if use_random:
            def color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
                return f"hsl({random.randint(0, 360)}, 100%, 40%)"
        else:
            colors = [
                "hsl(210, 80%, 40%)",  # deep sea blue
                "hsl(185, 60%, 45%)",  # soft teal
                "hsl(200, 50%, 35%)",  # navy blue
                "hsl(170, 50%, 40%)",  # sea green
                "hsl(195, 40%, 50%)"   # muted aqua
            ]
            def color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
                return random.choice(colors)

# --------------------------------
# Optional: Uncomment to define and remove stopwords
# --------------------------------
# custom_stopwords = set(STOPWORDS)
# custom_stopwords.update([
#     'study', 'analysis', 'effect', 'among', 'using', 'based',
#     'students', 'student', 'perspective', 'relationship', 'role',
#     'cognitive', 'affective', 'emotional', 'social', 'medical', 'title'
# ])
# stopwords = custom_stopwords
# --------------------------------

try:
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        mask=mask,
        font_path=font_path,
        color_func=color_func,
        collocations=False,
        # stopwords=stopwords,  # Uncomment if using custom stopwords
    ).generate(titles_text)

    # --- Plot the word cloud ---
    plt.figure(figsize=(10, 5) if not use_mask else (10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud of {title_column} Column ({'Shaped' if use_mask else 'Rectangular'})")
    plt.tight_layout()
    plt.show()

except ValueError as e:
    messagebox.showerror(
        "Word Cloud Generation Error",
        "The word cloud could not be generated.\n\n"
        "Reason: " + str(e) + "\n\n"
        "Please ensure your image provides enough usable area, "
        "or try using a different silhouette image."
    )