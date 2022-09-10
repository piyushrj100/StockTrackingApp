from http.client import HTTPResponse
from django.shortcuts import render
from yahoo_fin.stock_info import * 
import time 


# Create your views here.

def stockPicker(request) :
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request,'mainapp/stockpicker.html',{'stockpicker' : stock_picker})

def stockTracker(request) :
    stockpicker = request.GET.getlist('stockpicker')
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker : 
        if i in available_stocks : 
            pass 
        else : 
            return HTTPResponse("Error")
    n_threads=len(stockpicker)
    thread_list=[]

    start=time.time()
    print(time)

    # for i in stockpicker : 
    #     details = get_quote_table(i)
    #     data.update({i:details})
    for i in range(n_threads) :
        thread = Thread(target = lambda q, args1: q.put({stockpicker[i] : get_quote_table(arg1)}), args=())
    end=time.time()
    time_taken= end-start
    print(time_taken)
    print(data)
    return render(request, 'mainapp/stocktracker.html')
