#this program makes audiobook from any .pdf file.
import pyttsx3
import PyPDF2
book = open("class-11-Accountancy-part-1.pdf", 'rb')
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
print(pages)
speaker = pyttsx3.init()
for i in range(0,pages):
    page = reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    