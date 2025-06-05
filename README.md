WordCloud Generator – CSV to Word Cloud (with Optional Shape, Font, and Color)

==========================================
ABOUT
==========================================
This script generates a word cloud based on the contents of a single column in a CSV file. 
It supports:
- Choosing which CSV column to visualize
- Using a custom silhouette image to shape the word cloud (optional)
- Selecting a custom font (optional)
- Choosing your color scheme (default, single color, multicolor, or random)
- Optionally filtering out unwanted words (stopwords)

Input is provided via pop-up prompts.

==========================================
INSTRUCTIONS
==========================================

1. REQUIREMENTS:
   Before running the script, open your terminal or command prompt and install the required packages:

   pip install pandas matplotlib wordcloud numpy pillow

2. HOW TO RUN:
   - Save the script as generate_wordcloud.py
   - Double-click it (if Python is set up), press the play button in Visual Studio Code, or run in terminal using:
     python generate_wordcloud.py

3. USING THE SCRIPT:
   - When prompted, select your CSV file.
   - Optionally choose whether to use a shape mask (e.g., a submarine outline PNG).
   - Optionally select a custom font (.ttf or .otf).
   - Choose your color scheme.
   - View the generated word cloud in a pop-up window.
   - Press the save button in the lower left corner or screenshot the image if you would like to keep it 
   (once you close the pop up window it will be gone and you will have to re-run the script to get it back)

4. CHANGING THE COLUMN TO VISUALIZE:
   - Open the script file in any text editor (e.g., Notepad or VS Code).
   - Find the following line near the top:
     
     title_column = 'Title'
     
   - Change `'Title'` to match the column name you want to visualise in your CSV (case-sensitive). For example:
     
     title_column = 'Authors'

5. OPTIONAL: FILTERING OUT WORDS (STOPWORDS):
   - In the script, scroll to the section labeled:
     
     # Optional: Uncomment to define and remove stopwords
     
   - Uncomment the block below it by removing the '#' characters at the start of each line.
   - You must additionally find the section:

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

   - Uncomment the line:
   
    # stopwords=stopwords,

   - You can add or remove any words in the `custom_stopwords.update([...])` list.
     Example:
       custom_stopwords.update([
           'study', 'analysis', 'effect', 'task', 'to', 'for', 'user'
       ])
   - This is useful to remove common filler words or specific keywords you do not want shown.

==========================================
IMAGE MASK GUIDELINES (Optional)
==========================================
- The image should have a black shape on a white background (e.g., a black submarine silhouette on white).
- Accepted formats: PNG, JPG.
- The script will alert you if the image is too sparse or complex.
- It might be picky about your image, but in general the simpler the shape, the easier of a time it will have.

==========================================
FONT CUSTOMIZATION (Optional)
==========================================
- You may optionally select a custom font file when prompted.
- Supported formats: .ttf, .otf
- If you skip this step, the default system font will be used.

==========================================
COLOR OPTIONS
==========================================
When prompted, you may:
- Use default WordCloud colors (no customization)
- Choose a single color (e.g., "green" or "#00ff00")
- Use a predefined multicolor palette
- Let the script assign random colors

==========================================
How to Change the Predefined Multicolor Palette
==========================================
If you choose the "multicolor" option when prompted, the script uses a small set of predefined colors.
To customize this palette:
1. Open the script in a text editor.
2. Search for the following line (near the color settings section):

   colors = [
                "hsl(210, 80%, 40%)",  # deep sea blue
                "hsl(185, 60%, 45%)",  # soft teal
                "hsl(200, 50%, 35%)",  # navy blue
                "hsl(170, 50%, 40%)",  # sea green
                "hsl(195, 40%, 50%)"   # muted aqua
            ]

3. Replace or add HSL or hex color values to change the palette.
   Examples:
     - Using HSL: "hsl(0, 100%, 50%)" for red
     - Using hex: "#ff6600" for orange
     - Using named colors: "navy", "gold", etc. (though HSL gives better variation)

4. Save the script and run it again.

Note: You can use online tools to help pick colors and get their HSL or hex codes.

==========================================
EXAMPLE CSV FORMAT
==========================================
Your CSV should look something like this:

Title
The psychology of human-AI interaction
Designing empathetic robots
Affective computing in education
...

Make sure the first row contains column headers!

==========================================
TROUBLESHOOTING
==========================================
- "No file was selected": You must choose a CSV when prompted.
- "Column not found": Ensure you typed the column name correctly in `title_column`. It is case sensitive!
- "Couldn't find space to draw": Try using a larger or clearer silhouette image with less white space.
- "No words appearing": Make sure the column you selected actually contains meaningful text.