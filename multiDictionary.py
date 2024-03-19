import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizio =d.Dictionary()
        #self.rich = rw.RichWord()
        pass

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        lista_richwords=[]
        sbagliate=[]
        diz=self.dizio.loadDictionary(language)

        for parola in words:
            a = rw.RichWord(parola)

            if (diz.__contains__(parola)):
                a.corretta=True
            else:
                a.corretta=False
                sbagliate.append(a)

            lista_richwords.append(a)
        return sbagliate

        pass


