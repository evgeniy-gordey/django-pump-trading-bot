import requests

from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from yobit import Yobit

@api_view(['POST'])
@permission_classes([])
def trade(request): 
    amount = request.data.get('amount')
    buy_rate = request.data.get('buyRate')
    sell_rate = request.data.get('sellRate')
    currency = request.data.get('currency')
    
    pair = currency + '_btc'
    
    yobit = Yobit()
    # ticker = yobit.ticker(pair)
    get_info = yobit.get_info()
    
    return JsonResponse(get_info, safe=False)