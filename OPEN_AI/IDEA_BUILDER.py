from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from openai import OpenAI
import os
import urllib.request 
from reportlab.lib.utils import ImageReader




def main():
    print("Main function")
    print("Write the name of your thing")
    name = input("Enter: ")
    print("Write the atributes of this thing")
    atributes = input("Enter: ")
    print("Print? y/n")
    choice = input("Enter: ")
    #name = "Design me a name for a cool gadget"
    print("Getting response")
    description = DescriptionGen(name, atributes)
    #description = "Testing testing testings"
    print("Response received")
    #print(description)
    # file = open("Name and Description.txt","w")
    # #file.write(name)
    # file.write("\n")
    # file.write(description)
    # file.close()
    print("Generating Image")
    ImageGen(description)
    PDFBuilder(name, description)
    if choice == "y" or choice == "Y":
        Printer()
    
    
def DescriptionGen(name, atributes):
    AI_prompt = f"Write me a description of {name} with atributes such as {atributes}"
    tokens = 2000
    os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'
    client = OpenAI()
    system = "Normal"
    #system = "Creative Vision, Technical Proficiency, Attention to Detail, Innovation, Adaptability, Emotional Depth, Communication Skills, Persistence, Influence, Business Acumen"
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      max_tokens = tokens,
          messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": AI_prompt}
          ]
    )

    return completion.choices[0].message.content
    
    

def ImageGen(description):
    os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'
    client = OpenAI()
    completion = client.images.generate(
          #image=open("example.png", "rb"),
          model="dall-e-3",
          prompt=description,
          size="1024x1024",
          quality="standard",
          n=1,
    )
    image_url = completion.data[0].url
    #print(image_url)
    url = image_url
    urllib.request.urlretrieve(url, "image.png") 
    #img = Image.open(r"image.png")
    #img.show()
    
    
    
    

def PDFBuilder(name, description):
    Heading = ParagraphStyle('heading',
                            fontName="Helvetica-Bold",
                            fontSize=25,
                            #parent=style['Heading2'],
                            alignment=1,
                            spaceAfter=20)
    Description = ParagraphStyle('description',
                            fontName="Helvetica-Bold",
                            fontSize=10,
                            borderPadding = (7,2,20),
                            borderWidth = 1.5,
                            #parent=style['Heading2'],
                            alignment=1,
                            spaceAfter=30)


    # Create a PDF document
    doc = SimpleDocTemplate("Idea.pdf", pagesize=letter)

    # Create a flowables list to hold elements
    elements = []

    # Add the image to the PDF
    image_path = "image.png"
    print(image_path, inch)
    img = Image(image_path, 4*inch, 3.2*inch)
    elements.append(img)

    # Add a spacer to push the paragraph to the right
    elements.append(Spacer(1, 1))

    # Add the paragraph to the PDF
    styles = getSampleStyleSheet()
    elements.append(Paragraph(name, Heading))
    elements.append(Paragraph(description, Description))

    # Build the PDF document
    doc.build(elements)



def Printer():
    os.startfile("Idea.pdf", "print")


main()
