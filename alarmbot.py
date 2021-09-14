import requests
import telegram


class Alarmbot:
    def __init__(self):
        token = "1977222686:AAEz7_F-QdlG3ERlmNmMxTXbtdxJVZt85IY"
        self.bot = telegram.Bot(token)
        pass

    def trace_klay_aklay(self):
        ratio = self.get_aklayratio()
        
        if(ratio > 1.03 or ratio < 1.005):
            msg = "1klay = {}aklay".format(ratio)
            self.bot.sendMessage(chat_id=1756685757 , text = msg)

        pass



    def get_klayprice(self):
        url_klayusdtLP : str = "https://api-cypress.scope.klaytn.com/v1/accounts/0xd83f1b074d81869eff2c46c530d7308ffec18036"
        url_klayusdtLPbalance : str = "https://api-cypress.scope.klaytn.com/v1/accounts/0xd83f1b074d81869eff2c46c530d7308ffec18036/balances"
        klaytnDecimal : int = 18

        response = requests.request("GET", url_klayusdtLP)
        data = response.json()
        klaytotal = pow(10 , -klaytnDecimal) * int(data['result']['balance'])

        response = requests.request("GET", url_klayusdtLPbalance)
        data = response.json()

        firstElem = next(iter(data['tokens'].items()))
        foundToken = (firstElem[1])
        usdtTotal = pow(10 , -int(foundToken['decimals'])) * int(data['result'][0]['amount'])
        
        return usdtTotal / klaytotal

    def get_aklayratio(self):
        url_klayaklayLP : str = "https://api-cypress.scope.klaytn.com/v1/accounts/0xe74c8d8137541c0ee2c471cdaf4dcf03c383cd22"
        url_klayaklayLPbalance : str = "https://api-cypress.scope.klaytn.com/v1/accounts/0xe74c8d8137541c0ee2c471cdaf4dcf03c383cd22/balances"
        klaytnDecimal : int = 18

        response = requests.request("GET", url_klayaklayLP)
        data = response.json()
        klaytotal = pow(10 , -klaytnDecimal) * int(data['result']['balance'])

        response = requests.request("GET", url_klayaklayLPbalance)
        data = response.json()

        firstElem = next(iter(data['tokens'].items()))
        foundToken = (firstElem[1])
        aklayTotal = pow(10 , -int(foundToken['decimals'])) * int(data['result'][0]['amount'])

        return aklayTotal / klaytotal
        




