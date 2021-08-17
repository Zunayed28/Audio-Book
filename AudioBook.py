import pyttsx3
import PyPDF2

book = open("Book.pdf", 'rb')   # mention any PDF file with location
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
speaker = pyttsx3.init()

for i in range(2, pages):
    page = reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
