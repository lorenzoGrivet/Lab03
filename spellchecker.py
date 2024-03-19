import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):
        start_time = time.time()
        testo = replaceChars(txtIn)
        lista_testo = testo.split(" ")
        risultato = self.multi.searchWord(lista_testo, language)
        end_time = time.time()
        tempo=end_time-start_time
        return risultato,tempo
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
    pass