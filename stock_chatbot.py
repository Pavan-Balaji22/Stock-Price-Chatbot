import spacy
import pandas as pd
import yfinance as yf

nlp = spacy.load("en_core_web_trf")
# symbols = pd.read_csv("nasdaq_screener_1649871223347.csv").iloc[:,:2]

def get_response(statement,symbols):
    if len(statement.split()) > 1:
        doc = nlp(statement.title())
        entities = list()
        for ent in doc.ents:
            entities.append(ent.text)
        try:
            req = symbols[symbols["Name"].str.contains(entities[0].title()) & symbols["Name"].str.contains("Common Stock")].iloc[0,0]
            print(req)
            return("The latest stock price of {} is {:.2f}".format(entities[0],yf.download(tickers=req, period='1d', interval='5m',progress= False).iloc[-1,1])) 
        except:
            return("Symbol not found, can you provide the nasdaq symbol of the Company?")
        
    else:
        try:
         req = symbols[symbols["Symbol"].str.contains(statement.upper())].iloc[0,1] 
         return("The latest stock price of {} is {:.2f}".format(req,yf.download(tickers=statement, period='1d', interval='5m',progress= False).iloc[-1,1]),0) 
        except:
            return("Sorry the information on the stock cannot be found!Please try again!")

# print("Hello welcome to Stock price retrival chatbot!!!!!")
# flag = True
# s = None
# while flag:
#     if s == None:
#         print("StockBot: What stock information do you want?")
#         s=input("User: ")
#         get_response(s,symbols)
#     else:
#         s=input("Stockbot: Can i help you with something else: ")
#         if s == "quit":
#             flag = False
#         else:
#             print("StockBot: What stock information do you want?")
#             s=input("User: ")
#             get_response(s,symbols)
        
    



