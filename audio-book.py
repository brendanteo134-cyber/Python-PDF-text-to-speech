import pyttsx3
from pypdf import PdfReader # Use 'from pypdf import PdfReader'
from tkinter.filedialog import askopenfilename

book_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")]) 

if book_path:
    with open(book_path, 'rb') as file:
        pdfreader = PdfReader(file)
        pages = len(pdfreader.pages)
        print(f"Number of pages: {pages}")
        player = pyttsx3.init()
        for num in range(pages):
            page = pdfreader.pages[num]
            text = page.extract_text()
            if text:
                print(f"Reading page {num + 1}...")
                player.say(text)
                player.runAndWait()
            else:
                print(f"Could not extract text from page {num + 1}. Page may be an image.")

        player.stop()

