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
    print("Getting response")
    description = DescriptionGen(name, atributes)
    #description = "Hello"
    print("Response received")
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
    for times in range(4):
        times += 1
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
        urllib.request.urlretrieve(url, f"image{times}.png")
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
    doc = canvas.Canvas("Idea.pdf", pagesize=letter)

    # Create a flowables list to hold elements
    elements = []

    # Add the image to the PDF
    image_path1 = "image1.png"
    image_path2 = "image2.png"
    image_path3 = "image3.png"
    image_path4 = "image4.png"
    #print(image_path, inch)
    # img1 = Image(image_path1, 3*inch, 1.5*inch)
    # img2 = Image(image_path2, 3*inch, 1.5*inch)
    # img3 = Image(image_path3, 3*inch, 1.5*inch)
    # img4 = Image(image_path4, 3*inch, 1.5*inch)
    # elements.append(Paragraph(name, Heading))
    # elements.append(img1)
    # elements.append(Paragraph("|", Description))
    # elements.append(img2)
    # elements.append(Paragraph("|", Description))
    # elements.append(img3)
    # elements.append(Paragraph("|", Description))
    # elements.append(img4)
    
    images = ["image1.png", "image2.png", "image3.png", "image4.png"]
    positions = [(90, 425), (307, 425), (90, 175), (307, 175)]

# Add images to the PDF in a 2x2 grid pattern
    for i in range(len(images)):
        doc.drawImage(images[i], positions[i][0], positions[i][1], width=200, height=200)
    doc.setFont("Helvetica", 15)
    text_width = doc.stringWidth(name, "Helvetica", 15)
    doc.drawCentredString(letter[0] / 2, letter[1] / 2, name)
    text_width = doc.stringWidth(description, "Helvetica", 12)
    # Add a spacer to push the paragraph to the right
    # elements.append(doc)
    # elements.append(Spacer(1, 1))

    # # Add the paragraph to the PDF
    # styles = getSampleStyleSheet()
    
    #elements.append(Paragraph(description, Description))

    # Build the PDF document
    doc.save()



def Printer():
    os.startfile("Idea.pdf", "print")


main()
