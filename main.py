import MetaTrader5 as mt5
from pyrogram import Client, filters
import re
from time import sleep

print('HELLO!')

channels = {
    -1001307641116: {'type': 'channel', 'trading': 'scalping', 'url': '@fattahmastertrader'},  #
    -1001763160769: {'type': 'channel', 'trading': 'scalping', 'url': '@GenjiTheJapanTrader'},  #
    -1001573760715: {'type': 'channel', 'trading': 'scalping', 'url': '@moiforexsignals'},  #
    -1001629728154: {'type': 'channel', 'trading': 'scalping', 'url': '@bizko'},  #
    # -1001416233252: {'type': 'channel', 'trading': 'str_long', 'url': 'test'},  #
    # -1001416233252: {'type': 'channel', 'trading': 'str_long', 'url': 'test'},  #
    # -1001445377985: {'type': 'channel', 'trading': 'str_long', 'url': '@americanforexspecialist'},  #
    # -1001349935562: {'type': 'channel', 'trading': 'gold',     'url': '@bestForexSignalsPips'},  #
    # -1001246538371: {'type': 'channel', 'trading': 'scalping', 'url': '@bestforextradinggroup'},  #
    # -1001291056071: {'type': 'channel', 'trading': 'scalping', 'url': '@fXReaperFreeForexSignals'},  #
    # -1001383532475: {'type': 'channel', 'trading': 'scalping', 'url': '@forexMoneyNLFree'},  #
    # -1001411820913: {'type': 'channel', 'trading': 'scalping', 'url': '@forexPipsFactory2'},  #
    # -1001480924116: {'type': 'channel', 'trading': 'scalping', 'url': '@forex_Signals_PIPs_Signal_Fx'},  #
    # -1001270204996: {'type': 'channel', 'trading': 'scalping', 'url': '@forex_xlab1'},  #
    # -1001126668980: {'type': 'group',   'trading': 'scalping', 'url': '@forexgreenpips958'},  #
    # -1001414424977: {'type': 'group',   'trading': 'scalping', 'url': '@forexgroup1111'},  #
    # -1001414424977: {'type': 'group',   'trading': 'scalping', 'url': '@Forexgroup112'},  #
    # -1001414424977: {'type': 'group',   'trading': 'scalping', 'url': '@Forexkiller1123'},  #
    # -1001311844342: {'type': 'channel', 'trading': 'scalping', 'url': '@forexsignalfactory'},  #
    # -1001491035512: {'type': 'channel', 'trading': 'scalping', 'url': '@forexsignalsolutions'},  #
    # -1001316056319: {'type': 'channel', 'trading': 'scalping', 'url': '@forexsignalsstreet'},  #
    # -1001470291934: {'type': 'channel', 'trading': 'scalping', 'url': '@forexsignalvalue'},  #
    # -1001420572107: {'type': 'channel', 'trading': 'scalping', 'url': '@forexsignalzz'},  #
    # -1001062012353: {'type': 'group',   'trading': 'str_long', 'url': '@FxGlobal5'},  #
    # -1001341052202: {'type': 'channel', 'trading': 'scalping', 'url': '@fxSignals_Gold'},  #
    # -1001298489655: {'type': 'channel', 'trading': 'scalping', 'url': '@fxpipsaction1'},  #
    # -1001399543862: {'type': 'channel', 'trading': 'scalping', 'url': '@fxpipsfactory'},  #
    # -1001399543862: {'type': 'group',   'trading': 'scalping', 'url': '@fx_globaltrades'},  #
    # -1001157841207: {'type': 'channel', 'trading': 'scalping', 'url': '@greenpipsforex'},  #
    # -1001203106845: {'type': 'channel', 'trading': 'scalping', 'url': 'https://t.me/joinchat/AAAAAEe19B0ZIeRRXNOpAg'},
    # -1001355784993: {'type': 'channel', 'trading': 'scalping', 'url': 'https://t.me/joinchat/AAAAAFDPoyF6DXvyQDYpDw'},
    # -1001302273796: {'type': 'channel', 'trading': 'scalping', 'url': '@m5MacDScalpers'},  #
    # -1001449789431: {'type': 'channel', 'trading': 'scalping', 'url': '@mADIFOREX_SIGNAL_MASTAR'},  #
    # -1001299535263: {'type': 'channel', 'trading': 'scalping', 'url': '@metatrader4Signals0'},  #
    # -1001494412791: {'type': 'channel', 'trading': 'scalping', 'url': '@metatrader5signal1'},  #
    # -1001171155421: {'type': 'channel', 'trading': 'scalping', 'url': '@octaFxsignalx'},  #
    # -1001148641286: {'type': 'channel', 'trading': 'scalping', 'url': '@pipstowin'},  #
    # -1001392466168: {'type': 'channel', 'trading': 'scalping', 'url': '@proFxSecretStrategy'},  #
    # -1001473518645: {'type': 'channel', 'trading': 'scalping', 'url': '@professoroff'},  #
    # -1001391473841: {'type': 'channel', 'trading': 'scalping', 'url': '@ronaldpatrick'},  #
    # -1001141061818: {'type': 'channel', 'trading': 'scalping', 'url': '@signal4000'},  #
    # -1001409206299: {'type': 'channel', 'trading': 'scalping', 'url': '@signalfxoption'},  #
    # -1001471162189: {'type': 'group',   'trading': 'scalping', 'url': '@signalsscalping12'},  #
    # -1001127289760: {'type': 'channel', 'trading': 'scalping', 'url': '@sureshotforex'},  #
    # -1001331117752: {'type': 'channel', 'trading': 'scalping', 'url': '@taarget_plus'},  #
    # -1001296877896: {'type': 'channel', 'trading': 'scalping', 'url': '@trendFriend12'},  #
    # -1001188607041: {'type': 'channel', 'trading': 'scalping', 'url': '@vipCoinexhangePump'},  #
    # -1001398995940: {'type': 'channel', 'trading': 'str_long', 'url': '@voltforex'},
}

symbols = ['AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'AUDUSD', 'CADCHF', 'CADJPY', 'CHFJPY', 'GBPAUD', 'GBPCAD',
           'GBPCHF', 'GBPJPY', 'GBPNZD', 'GBPUSD', 'EURAUD', 'EURCAD', 'EURCHF', 'EURGBP', 'EURJPY', 'EURNZD',
           'EURUSD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDCNH', 'USDJPY', 'XAUUSD', 'GOLD']


app = Client("mt5_signals", api_id="1047128", api_hash="1402e406ccfaf6d7ca2a08469bc60558")

def correct_number(params):
    if (params.isdigit()):
        return params;
    else:
        return re.search(r'\d+', params).group();

def sltp(chat_id, text, Sl, Tp):
    text = text.lower()
    # print(re)
    try:
        try:
            PRICE = re.findall(r'[\d.]+', str(text.lower().split('\n')[0]))
            PRICE1 = float(correct_number(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0]))
            try:    
                PRICE2 = float(correct_number(PRICE[1]))
            except:
                PRICE2 = 0
            # print(PRICE)
            # PRICE1 = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
            # PRICE2 = float(re.findall(r'[\d.]+', str(text.split('\n')[1]))[0])
            SL = float(correct_number(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1]))
            TP1 = float(correct_number(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1]))


            splited_texts = re.findall(r'[\d.]+', str([i for i in text.lower().split('\n') if Tp in i]))
            sls = re.findall(r'[\d.]+', str([i for i in text.lower().split('\n') if Sl in i]))


            TP3 = "0"

            try:
                TP1 = splited_texts[1]
                TP2 = splited_texts[3]
                TP3 = splited_texts[5]
            except:
                TP1 = splited_texts[0]
                TP2 = splited_texts[1]
                
            
            
            # print(f"PRICE1: {PRICE1}\nPRICE2: {PRICE2}\nSL: {SL}\nTP1: {TP1}\nTP2: {TP2}\nTP3: {TP3}")

            # return False
            data = {}
            data['entries'] = [float(PRICE1), float(PRICE2)]
            data['tps'] = [float(TP1), float(TP2), float(TP3)]
            data['sl'] = float(correct_number(sls[0]))
            # print(data)
            return data

        except Exception as e:
            print(e)
            return False
            
        if chat_id == -1001307641116:  # fattahmastertrader
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001763160769:  # @GenjiTheJapanTrader
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001349935562:  # @bestForexSignalsPips
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001246538371:  # @bestforextradinggroup
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001291056071:  # @fXReaperFreeForexSignals
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001383532475:  # @forexMoneyNLFree
            try:
                PRICE = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'enter' in i][0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[0])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001411820913:  # @forexPipsFactory2
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001480924116:  # @forex_Signals_PIPs_Signal_Fx
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[2]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001270204996:  # @forex_xlab1
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001126668980:  # @forexgreenpips958
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001414424977:  # @Forexkiller1123
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001311844342:  # @forexsignalfactory
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001491035512:  # @forexsignalsolutions
            try:
                PRICE = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if '@' in i][0]))[-1])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001316056319:  # @forexsignalsstreet
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[4]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001470291934:  # @forexsignalvalue
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001420572107:  # @forexsignalzz
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[2]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'stop loss' in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'take profit' in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001062012353:  # @FxGlobal5
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001341052202:  # @fxSignals_Gold
            try:
                PRICE = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'entry' in i]))[-1])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001298489655:  # @fxpipsaction1
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001399543862:  # @fx_globaltrades
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[1]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001157841207:  # @greenpipsforex
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001203106845:  # https://t.me/joinchat/AAAAAEe19B0ZIeRRXNOpAg Exclusive
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001355784993:  # https://t.me/joinchat/AAAAAFDPoyF6DXvyQDYpDw 💲Horizon
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001302273796:  # @m5MacDScalpers
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001449789431:  # @mADIFOREX_SIGNAL_MASTAR
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001299535263:  # @metatrader4Signals0
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001494412791:  # @metatrader5signal1
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001171155421:  # @octaFxsignalx
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001148641286:  # @pipstowin
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001392466168:  # @proFxSecretStrategy
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[2]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001473518645:  # @professoroff
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[2]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001391473841:  # @ronaldpatrick
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                if ('loss' in text):
                    SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'stop loss' in i]))[-1])
                    TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'take profit' in i][-1]))[-1])
                else:
                    SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                    TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001141061818:  # @signal4000
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001409206299:  # @signalfxoption
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001471162189:  # @signalsscalping12
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001127289760:  # @sureshotforex
            try:
                if not ('order' in text):
                    PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                    SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                    TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                    print(PRICE, SL, TP)
            except:
                return False
        elif chat_id == -1001331117752:  # @taarget_plus
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[1]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001296877896:  # @trendFriend12
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001188607041:  # @vipCoinexhangePump
            try:
                PRICE = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if '  #' in i]))[-1])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Sl in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if Tp in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
        elif chat_id == -1001398995940:  # @voltforex
            try:
                PRICE = float(re.findall(r'[\d.]+', str(text.split('\n')[0]))[0])
                SL = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'stop loss' in i]))[-1])
                TP = float(re.findall(r'[\d.]+', str([i for i in text.split('\n') if 'take profit' in i][-1]))[-1])
                return [PRICE, SL, TP]
            except:
                return False
    except Exception as ex:
        app.send_message(-1001573760715, f"sltp.{str(chat_id)}: {ex}")


def OrderSend(Symbol, Lot, Type, PRICE, Sl, Tp, Magic):
    selected = mt5.symbol_select(Symbol, True)
    # print(selected)
    if not selected:
        app.send_message(-1001573760715, f"OrderSend.symbol_select: {str(mt5.last_error())}")
        mt5.shutdown()
    symbol_info = mt5.symbol_info(Symbol)
    if (PRICE == 0.00 or Tp == 0.00 or Sl == 0.00):
        print('Invalid Price')
        return
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": Symbol,
        "volume": Lot,
        "type": Type,
        "price": float(PRICE),
        "sl": float(Sl),
        "tp": float(Tp),
        # "tp1": Tp+10,
        # "tp2": Tp+12,
        "deviation": 3,
        "magic": Magic,
        "comment": "Order ochish",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN
    }
    result = mt5.order_send(request)
    print('Bought', result, request)
    # app.send_message(-1001573760715, f"OrderSend.last_error: {str(mt5.last_error())}")
    mt5.shutdown()
    #quit()


@app.on_message(filters.channel)
# @app.on_message((filters.photo | filters.text) & (filters.channel | filters.chat))
def my_handler(client, message):
    # print(mt5.ORDER_TYPE_BUY_LIMIT)
    # print(message)
    if (message.text == "/status"):
        app.send_message(-1001573760715, "Still working alaye!")

    if (message.sender_chat.id not in channels):
        return
    Type = 150
    NOW_PRICE = 0
    Lot = 0.01
    chat_id = message.chat.id
    text = str(message.text).lower()
    if message.photo:
        if message.caption:
            text = message.caption
    if chat_id < 0:
        if 0 < len(text):
            if not ('limit' in text) and not ('sell stop' in text) and not ('buy stop' in text):
                if ('sl' in text and 'tp' in text) or ('stop loss' in text and 'take profit' in text):
                    print('hello')
                    for Symbol in symbols:
                        if Symbol.lower() in text:
                            if Symbol.lower() == "gold":
                                Symbol = "XAUUSD"
                            # print(text.lower())
                            if 'buy' in text.lower():
                                Type = mt5.ORDER_TYPE_BUY_LIMIT
                            if 'sell' in text.lower():
                                Type = mt5.ORDER_TYPE_SELL_LIMIT
                            st = sltp(chat_id, text, 'sl', 'tp')
                            # print(st)
                            
                            print(Symbol)
                            # if mt5.symbol_info_tick(Symbol) is not None:
                            for entry in st['entries']:
                                if st is not False and Type != 150:
                                    for tp in st['tps']:
                                        print('Entry no: ', entry, 'TP: ', tp, 'TPLEN', len(st['tps']), 'Symbol: ', Symbol)
                                        try:
                                            if mt5.initialize(login=40091749, server="OctaFX-Real",
                                                    password="y%u@UdUv"):
                                                
                                                OrderSend(Symbol.upper(), Lot, Type, entry, st['sl'], tp,
                                                            int(str(chat_id)[-10:]))

                                                mt5.shutdown()
                                                # quit()  
                                                sleep(5)

                                        except Exception as e:
                                            print('Error', str(e))
                                    # else:
                                        # print('Errror')
                                        # app.send_message(-1001573760715,
                                        #                     f"{str(mt5.last_error())}")
                                        # OrderSend(Symbol.upper(), Lot, Type, entry, st['sl'], tp,
                                        #             int(str(chat_id)[-10:]))
                                        # mt5.shutdown()


if __name__ == "__main__":
    app.run()
    # app.start()
    print('GETTING DIALOGS!')
    # print(app.get_chat('moiforexsignals'))