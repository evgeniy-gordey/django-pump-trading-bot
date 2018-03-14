import requests

from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse

@api_view(['POST'])
@permission_classes([])
def trade(request): 
    amount = request.data.get('amount')
    buyRate = request.data.get('buyRate')
    sellRate = request.data.get('sellRate')
    currency = request.data.get('currency')
    url = 'https://yobit.net/api/2/' + currency + '_btc/ticker'
    r = requests.get(url)
    return JsonResponse(r.text, safe=False)