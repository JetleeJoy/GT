from codecs import encode
import os
from statistics import mean

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.META_extension = "TEXT"
        
        #counting the total number of words in file
        file = open(self.file_path, "rt",encoding="utf-8")
        data = file.read()
        self.wordCount = len(data.split())
        self.validate()


    #function to check the extension of file
    def validate(self):
        split = os.path.splitext(self.file_path);
        extension = split[-1]
        if extension == ".txt":
            self.META_extension = "TEXT"
        elif extension == ".xlsx":
            self.META_extension = "EXCEL"
        else:
            self.META_extension = "incompatible"


class KeyWord(FileManager):
    #initilizing parent class constructor and a  a list for storing keyword
    def __init__(self,file_path,Mark):
        super().__init__(file_path)
        self.keylist = []
        self.frequencyTable = {}
        self.densityTable = {}
        self.hitCount = 0
        self.parseChar = [',','.','!','“','”','(',')','{','}','[',']','"',"'"]     
        self.percentage = 0
        self.Q_mark = Mark
        self.A_mark = 0

    #funciton to manually insert a keyword
    def insertKey(self):
        limit = int(input("Enter the number of keywords : "))
        print("Enter Keywords")
        for i in range(limit):
            keyvalue = input()
            self.keylist.append(keyvalue)

    #function to read keyword from a cell in xlsx book.
    def insertKey(self,_PATH):
        file = open(_PATH, "rt",encoding="utf-8")
        for line in file:
            for key in line.split(","):
                self.keylist.append(key)

    #file to be managed by its extension 
    def parseFile(self):
        if self.META_extension == "TEXT":
            self.parseTextFile()
        elif self.META_extension == "EXCEL":
            pass

    def frequencyDesity(self):
        try:
            for keyword in self.frequencyTable:
                    if self.wordCount != 0:
                        self.densityTable[keyword] = self.frequencyTable[keyword] / self.wordCount
        
            #taking the mean of word density for comparitive anlaysis
            meanDensity = mean(self.densityTable[value] for value in self.densityTable)
        except:
            meanDensity = 0


    def markAssessment(self):
        self.percentage = (self.hitCount/len(self.keylist))*100
        self.A_mark = (self.percentage/100)*self.Q_mark
        print("Score : ",self.Q_mark)
        print("Score Obtained : ",self.A_mark)


    #function to generate the frequency of keywords in the given file
    def parseTextFile(self):
        with open(self.file_path, 'r', encoding="utf-8") as fp:
            for line in fp:
                for word in line.split():
                    #parsing the word for potential mismatches
                    for char in self.parseChar:
                        word = word.rstrip(char) #right side stripping
                        word = word.lstrip(char) #left side stripping
                    if word in self.keylist:
                        if word in self.frequencyTable:
                            self.frequencyTable[word] += 1
                        else:
                            self.hitCount += 1
                            self.frequencyTable[word] = 1
          

def main():
    #input_path = "C:/Users/jetle/Documents/resource/wrong.txt"
    #input_path = "C:/Users/jetle/Documents/resource/alt.txt"
    input_path = "C:/Users/jetle/Documents/resource/answer.txt"

    #input_path = "C:/Users/jetle/Documents/resource/wrong2.txt"
    #input_path = "C:/Users/jetle/Documents/resource/alt2.txt"
    #input_path = "C:/Users/jetle/Documents/resource/answer2.txt"

    _PATH = "C:/Users/jetle/Documents/resource/key.txt"
    #_PATH = "C:/Users/jetle/Documents/resource/key2.txt"

    fm = KeyWord(input_path,40)
    fm.insertKey(_PATH)
    fm.parseFile()
   # fm.frequencyDesity()
    fm.markAssessment()
   # print("word count : ",fm.wordCount)
   # print("keyword count : ",len(fm.keylist))
   # print("keyword hit : ",fm.hitCount)

if __name__ == "__main__":
    main()