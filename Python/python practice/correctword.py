from spellchecker import SpellChecker

class Spellcheckerapp:
    def __init__(self):
        self.spell=SpellChecker()

    def corrected_text(self,text):
        words = text.split()
        corrected_words =[]

        for word in words:
            corrected_word =self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting {word} to {corrected_word}")
                corrected_words.append(corrected_word)

        return ' '.join(corrected_words)
    
    def run(self):
        print("\n Spell Checker")

        while True:
            text = input("Enter text to check (or type exit to quit)")

            if text.lower() == 'exit':
                print("Closing the program")
                break
            
            corrected_text =self.corrected_text(text)
            print(f"Corrected text : {corrected_text}")

if __name__ == "__main__":
    Spellcheckerapp().run()