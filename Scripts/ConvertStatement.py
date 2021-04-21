import pdfplumber

fileWriter = open('C:\\Users\\vidrinen\\Desktop\\BankTest.txt', 'a')

with pdfplumber.open(r'C:\Users\vidrinen\Downloads\test.pdf') as pdf:
    for i in range(0, len(pdf.pages)):
        current_page = pdf.pages[i].extract_text()
        page = current_page.split("\n")
        correctInfo = False
        for line in page:
            words = line.split(" ")
            if(correctInfo):
                if(words[0]=="Continued"): correctInfo = False
                elif(words[0]=="TOTAL"):
                    correctInfo = False
                    fileWriter.write(line + "\n\n\n")
                elif(words[0]=="Eff."): continue
                else: fileWriter.write(words[0] + " " + words[1] + "\t" + words[2] + " " + words[3] + "\t" + words[len(words)-1] + "\n")
            else:
                if(line=='Deposits and Credits'): correctInfo = True
                elif(line=='ATM and Debit Card Withdrawals'): correctInfo = True
                elif(line=='Electronic Withdrawals'): correctInfo = True
    
fileWriter.close()