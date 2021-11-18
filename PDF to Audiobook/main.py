import PyPDF2
import pyttsx3

reader = PyPDF2.PdfFileReader('What_is_a_tiger.pdf')

pageObj = reader.getPage(2)

engine = pyttsx3.init()
engine.setProperty("rate", 145)
engine.say(pageObj.extractText())
engine.runAndWait()