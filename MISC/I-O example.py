import time
class Pet:
    def __init__(self, name, Type, age):
        self.name = name
        self.Type = Type
        self.age = age
        get_name = name
        get_animal_type = Type
        get_age = age

    def main(self):
        

        start = input('Press enter to start: ')
        time.sleep(1)
        print()
        inputName = input("Enter the animal's name: ")
        inputType = input("Enterthe animal's type: ")
        inputAge = int(input("Enter the animal's age: "))
        finalAnimal = Pet(inputName, inputType, inputAge)
        print('Alright...')
        print()
        print()
        print(f'The name is {finalAnimal.name}')
        print(f'The type is {finalAnimal.Type}')
        print(f'The age is {finalAnimal.age}')


p1 = Pet('d','d','d')
p1.main()
