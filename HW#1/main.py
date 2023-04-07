import sys
import cowsay

def say(argv):
    if len(argv) > 3:
        raise Exception("Too many arguments") 
    elif len(argv) == 1:
        raise Exception("Not enough arguments") 
    
    animal = argv[1]
    if animal not in cowsay.char_names:
        raise Exception("Wow, this animal doesn't exist")
    
    if len(argv) == 3:
        text = argv[2]
        print(cowsay.get_output_string(animal, text))  
    else:
        try:
            with open('docker/speech.txt', 'r') as f:
                text = f.read()
                print(cowsay.get_output_string(animal, text))  
        except:
            print("Something went wrong with your speech file, so it is time for jokes")
            joke = 'У мужика глисты завелись.\n Ему врач посоветовала пить 6 дней кефир с булочкой, а на 7 день только кефир. Мужик так и сделал: 6 дней пил кефир с булочкой, a на седьмой день выпил только кефир.\n Вылезает глист: а где булочка?'
            print(cowsay.get_output_string(animal, joke))
    

if __name__ == "__main__":
    say(sys.argv)