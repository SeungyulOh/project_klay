import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime


global TELEGRAMTOKEN
TELEGRAMTOKEN : str = "NONE"
global KLAYUSDTLP
KLAYUSDTLP : str = "0xd83f1b074d81869eff2c46c530d7308ffec18036"
global KLAYAKLAYLP
KLAYAKLAYLP : str = "0xe74c8d8137541c0ee2c471cdaf4dcf03c383cd22"
global KAIUSDTLP
KAIUSDTLP : str = "0x5787492d753d5f59365e2f98e2f18c3ae3bad6e7"
global KAIKSCOINBASELP
KAIKSCOINBASELP : str = '0x190d75dd77c6f870eb4b990f54b72d469e205928'
global KAIKSDUNAMULP
KAIKSDUNAMULP : str = '0xb7aa1890828d867c25725f0c2ef3182a1a1ec71e'
global KAIKSYANOLJALP
KAIKSYANOLJALP : str = '0xcb8bbcaacbc33d391930e9063d26f6c076cb3c73'
global KAIKSETHERIUMLP
KAIKSETHERIUMLP : str = '0x776898cad4f8ba58b533a2c20b975c880db57b63'
global KAIKSSOLLP
KAIKSSOLLP : str = '0xd5dc92f74e8392ef953ab81b3b4cb930daa956b8'
global KAIKSLUNALP
KAIKSLUNALP : str = '0xf444e2a6cd5b9a1d207aba33ac8026ae68d2c150'
global SBWPMUSDTLP
SBWPMUSDTLP : str = '0xb6eaa073881c9cac7141ef20b25a588914a367b2'
global KSDKUSDTLP
KSDKUSDTLP : str = '0xc9ad2f9c45c9cc3128c898fe55c14a146e7d1d88'
global JUNKUSDTLP
JUNKUSDTLP : str = '0x391330644903fd2d6ccb084965b1c350ff6c4c56'
global JUNSKUSDTLP
JUNSKUSDTLP : str = '0xff99d881e868d7f15a12b08cd1e390af675c0554'

global SYNTHESISURL
SYNTHESISURL : str = 'https://api.kaiprotocol.fi/getpricehistory?symbol={}&period=minutes'



class Alarmbot:
    def __init__(self):
        global TELEGRAMTOKEN
        self.bot = telegram.Bot(TELEGRAMTOKEN)
        
        # updater = Updater(TELEGRAMTOKEN)
        # dp = updater.dispatcher
        # dp.add_handler(CommandHandler(["setminmax"], self.setminmax))
        # updater.start_polling()

        self.max = 0.25
        self.min = 0.08
        self.prev = 0
        pass

    def setminmax(self, updates, ctx):
        self.min = float(ctx.args[0]) * 0.01
        self.max = float(ctx.args[1]) * 0.01
        pass
    

    def trace_klay_aklay(self):
        try:
            ratio = self.get_aklayratio()
            if(ratio > 1.03 or ratio < 1.005):
                msg = "1klay = {}aklay".format(ratio)
                self.bot.sendMessage(chat_id=1756685757 , text = msg)
        except:
            print('something wrong..')
            pass
        pass

    def trace_ksd_premium(self):
        try:
            # price = self.get_ksdprice()
            # if(price > 1.12):
            #     msg = "ksd = {:.2f}".format(price)
            #     self.bot.sendMessage(chat_id=1756685757 , text = msg)

            juns_price = self.get_junsprice()
            #jun_price = self.get_junprice()
            # if(jun_price < 2.0):
            #     msg = "jun = {:.2f}".format(jun_price)
            #     self.bot.sendMessage(chat_id=1756685757 , text = msg)

            if(juns_price < 42 or juns_price > 75):
                msg = "juns = {:.2f}".format(juns_price)
                self.bot.sendMessage(chat_id=1756685757 , text = msg)


                    

            
            pass

        except:
            print(datetime.datetime.now())
            pass
        pass

    def trace_synthetics_premium(self):
        try:
            print(datetime.datetime.now())

            dm_startprice = self.get_synthesis_price('ksDUNAMU')
            dm_currentprice = self.get_ksdunamuprice()
            dm_premium = (dm_currentprice - dm_startprice) / dm_startprice
            msg = "dunamu premium : {:.2f} %".format(dm_premium * 100)
            #print("{}".format(msg))
            if(dm_premium < self.min or dm_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            yj_startprice = self.get_synthesis_price('ksYANOLJA')
            yj_currentprice = self.get_ksyanolja()
            yj_premium = (yj_currentprice - yj_startprice) / yj_startprice
            msg = "yanolja premium : {:.2f} %".format(yj_premium * 100)
            #print("{}".format(msg))
            if(yj_premium < self.min or yj_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            cb_startprice = self.get_synthesis_price('ksCOINBASE')
            cb_currentprice = self.get_kscoinbaseprice()
            cb_premium = (cb_currentprice - cb_startprice) / cb_startprice
            msg = "coinbase premium : {:.2f} %".format(cb_premium * 100)
            #print("{}".format(msg))
            if(cb_premium < self.min or cb_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            eth_startprice = self.get_synthesis_price('ksETH')
            eth_currentprice = self.get_ksetherium()
            eth_premium = (eth_currentprice - eth_startprice) / eth_startprice
            msg = "ksETH premium : {:.2f} %".format(eth_premium * 100)
            #print("{}".format(msg))
            if(eth_premium < self.min or eth_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            sol_startprice = self.get_synthesis_price('ksSOL')
            sol_currentprice = self.get_ksSOL()
            sol_premium = (sol_currentprice - sol_startprice) / sol_startprice
            msg = "ksSOL premium : {:.2f} %".format(sol_premium * 100)
            #print("{}".format(msg))
            if(sol_premium < self.min or sol_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            luna_startprice = self.get_synthesis_price('ksLUNA')
            luna_currentprice = self.get_ksLUNA()
            luna_premium = (luna_currentprice - luna_startprice) / luna_startprice
            msg = "ksLUNA premium : {:.2f} %".format(luna_premium * 100)
            #print("{}".format(msg))
            if(luna_premium < self.min or luna_premium > self.max):
                self.bot.sendMessage(chat_id=1756685757 , text = msg)

            # sbwpm_price = self.get_sbwpmprice()
            # if(self.prev != sbwpm_price):
            #     self.prev = sbwpm_price
            #     delta = ((sbwpm_price - 3364.125) / 3364.125) * 100
            #     msg = "sbwpm_price : {:.2f} , {:.2f} %".format(sbwpm_price , delta)
            #     self.bot.sendMessage(chat_id=1756685757 , text = msg)

            
        except:
            pass
        pass

    def get_synthesis_price(self, symbol):
        global SYNTHESISURL
        url = SYNTHESISURL.format(symbol)
        response = requests.request("GET", url)
        data = response.json()
        return (data[-1]['oraclePrice'])

    def get_lp_url(self, adress):
        return "https://api-cypress.scope.klaytn.com/v1/accounts/{}".format(adress)
    def get_lpbalance_url(self, adress):
        return "https://api-cypress.scope.klaytn.com/v1/accounts/{}/balances".format(adress)

    def get_ksyanolja(self):
        global KAIKSYANOLJALP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSYANOLJALP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        ksyanolja_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksYANOLJA"):
                ksyanolja_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / ksyanolja_totalamount) * self.get_kaiprice()


    def get_ksLUNA(self):
        global KAIKSLUNALP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSLUNALP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        target_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksLUNA"):
                target_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / target_totalamount) * self.get_kaiprice()

    def get_ksSOL(self):
        global KAIKSSOLLP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSSOLLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        target_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksSOL"):
                target_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / target_totalamount) * self.get_kaiprice()

    def get_ksetherium(self):
        global KAIKSETHERIUMLP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSETHERIUMLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        target_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksETH"):
                target_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / target_totalamount) * self.get_kaiprice()

    def get_ksdunamuprice(self):
        global KAIKSDUNAMULP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSDUNAMULP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        ksdunamu_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksDUNAMU"):
                ksdunamu_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / ksdunamu_totalamount) * self.get_kaiprice()

    def get_kscoinbaseprice(self):
        global KAIKSCOINBASELP
        url_LP_balance : str = self.get_lpbalance_url(KAIKSCOINBASELP)
        
        response = requests.request("GET", url_LP_balance)
        data = response.json()

        kai_totalamount = 0
        kscoinbase_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "ksCOINBASE"):
                kscoinbase_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return (kai_totalamount / kscoinbase_totalamount) * self.get_kaiprice()

    def get_kaiprice(self):
        global KAIUSDTLP
        url_LP_balance : str = self.get_lpbalance_url(KAIUSDTLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()


        kai_totalamount = 0
        kusdt_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KAI"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "KUSDT"):
                kusdt_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return kusdt_totalamount / kai_totalamount

    def get_sbwpmprice(self):
        global SBWPMUSDTLP
        url_LP_balance : str = self.get_lpbalance_url(SBWPMUSDTLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()


        kai_totalamount = 0
        kusdt_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "sBWPM"):
                kai_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 
            if(value['symbol'] == "KUSDT"):
                kusdt_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 

        return kusdt_totalamount / kai_totalamount

    def get_ksdprice(self):
        global KSDKUSDTLP
        url_LP_balance : str = self.get_lpbalance_url(KSDKUSDTLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        src_totalamount = 0
        kusdt_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "KSD"):
                src_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 
            if(value['symbol'] == "KUSDT"):
                kusdt_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 

        return kusdt_totalamount / src_totalamount

    def get_junprice(self):
        global JUNKUSDTLP
        url_LP_balance : str = self.get_lpbalance_url(JUNKUSDTLP)

        response = requests.request("GET", url_LP_balance)
        data = response.json()

        src_totalamount = 0
        kusdt_totalamount = 0
        for key , value in data['tokens'].items():
            if(value['symbol'] == "JUN"):
                src_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][0]['amount']) 
            if(value['symbol'] == "KUSDT"):
                kusdt_totalamount = pow(10 , -int(value['decimals'])) *int(data['result'][1]['amount']) 

        return kusdt_totalamount / src_totalamount


    def get_klayprice(self):
        global KLAYUSDTLP
        url_klayusdtLP : str = self.get_lp_url(KLAYUSDTLP)
        url_klayusdtLPbalance : str = self.get_lpbalance_url(KLAYUSDTLP)
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
        global KLAYAKLAYLP
        url_klayaklayLP : str = self.get_lp_url(KLAYAKLAYLP)
        url_klayaklayLPbalance : str = self.get_lpbalance_url(KLAYAKLAYLP)
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

    def get_junsprice(self):
        global JUNSKUSDTLP
        url_klayaklayLP : str = self.get_lp_url(JUNSKUSDTLP)
        url_juns : str = self.get_lpbalance_url(JUNSKUSDTLP)
        klaytnDecimal : int = 18


        response = requests.request("GET", url_klayaklayLP)
        data = response.json()
        klaytotal = pow(10 , -klaytnDecimal) * int(data['result']['balance'])

        response = requests.request("GET", url_juns)
        data = response.json()

        firstElem = next(iter(data['tokens'].items()))
        foundToken = (firstElem[1])
        juns_total = pow(10 , -int(foundToken['decimals'])) * int(data['result'][0]['amount'])

        return (self.get_klayprice() * klaytotal) / juns_total 

        




