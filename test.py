import string
from googletrans import Translator
class Translator_text:


    def __init__(self, word_obj):
        self.word = word_obj
        self.russian_dict = {"я": "I", "яблоко": "apple", 'банан': "banana", 'город': 'city', 'человек': 'human'}
        self.english_dict = {'program': 'программа', 'technology': 'технология', 'innovation': 'инновация',
                        'super man': 'супермен'}
    def translator_text(self):
        if self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='ru').text
            return translate_word
        elif self.word[0].upper() not in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='en').text
            return translate_word


translator1 = Translator("technology")
print(translator1.translator_text())