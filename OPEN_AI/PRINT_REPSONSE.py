from openai import OpenAI
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import urllib.request 
#from PIL import Image

def main():
    print("Welcome to Z_AI!\n")
    system = "blank"
    system = pickSystem(system)
    #image = input("Image Generate? y/n: ")
    question = input("Enter to AI: " )
    tokens = int(input("Enter max tokens: "))
    PRINT = input("print? (will auto exit) y/n: ")
    x = AskAI(question, system, tokens)
    print("========" * 5)
    print(x)
    print("========" * 5)
    print()
    if PRINT == "y" or PRINT == "Y":
        file = open("response.txt","w")
        file.write(x)
        file.close
        os.startfile("response.txt", "print")
        exit()

def pickSystem(system):
        print()
        print()
        x1 = "1. The Sage: Wise, knowledgeable, and always ready to provide insightful information."
        x2 = "2. The Jester: Witty, humorous, and able to lighten the mood with jokes and playful banter."
        x3 = "3. The Guardian: Protective, reassuring, and focused on ensuring the user's safety and security."
        x4 = "4. The Optimist: Positive, encouraging, and always looking for the bright side of things."
        x5 = "5. The Detective: Inquisitive, analytical, and adept at finding solutions to complex problems."
        x6 = "6. he Artist: Creative, imaginative, and able to express information in engaging and visually appealing ways."
        x7 = "7. The Mentor: Supportive, patient, and dedicated to guiding users through challenges and learning experiences."
        x8 = "8. The Futurist: Forward-thinking, visionary, and focused on exploring emerging technologies and trends."
        x9 = "9. The Fact: Only provide factual information without any additional remarks."
        x10 = "10. Custom"
        x11 = "11. Standard"
        x12 = "12. The Musician: Master musician, Vast repertoire knowledge, Mastery of musical theory, Collaborative mindset, Impeccable listening skills."
        print(f"{x1}\n{x2}\n{x3}\n{x4}\n{x5}\n{x6}\n{x7}\n{x8}\n{x9}\n{x10}\n{x11}")
        print()
        choice = int(input("Choice: "))
        if choice == 1:
            system = x1
        elif choice == 2:
            system = x2
        elif choice == 3:
            system = x3
        elif choice == 4:
            system = x4
        elif choice == 5:
            system = x5
        elif choice == 6:
            system = x6
        elif choice == 7:
            system = x7
        elif choice == 8:
            system = x8
        elif choice == 9:
            system = x9
        elif choice == 10:
            system = input("Enter AI characteristics: ")
        elif choice == 11:
            system = x11
        elif choice == 12:
            system = x12
        return system

def AskAI(question, system, tokens):
    os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'
    client = OpenAI()
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      max_tokens = tokens,
          messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question}
          ]
    )

    return completion.choices[0].message.content


    

main()
