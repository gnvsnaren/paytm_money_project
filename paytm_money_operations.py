from os import environ
import requests

def get_paytm_holdings_value():
    paytm_access_token = environ.get('PAYTM_ACCESS_TOKEN')

    # Call the access token API of Paytm
    url = 'https://developer.paytmmoney.com/holdings/v1/get-holdings-value'
    headers = {'x-jwt-token': paytm_access_token}
    r = requests.get(url=url, headers=headers)

    response = r.json()

    print(f'The response of the API call is: {response}')

    return 'response'

def buy_open_ongc_order():
    paytm_access_token = environ.get('PAYTM_ACCESS_TOKEN')

    # Call the access token API of Paytm
    url = 'https://developer.paytmmoney.com/orders/v1/place/regular'
    headers = {'x-jwt-token': paytm_access_token, 'Content-Type': 'application/json'}
    body = {'txn_type': 'B', 'exchange': 'BSE', 'segment': 'E', 'product': 'I', 'security_id': '500312', 'quantity': 1, 'validity': 'DAY', 'order_type': 'MKT', 'price': 0, 'source': 'W'}
    r = requests.post(url=url, headers=headers, json=body)

    response = r.json()

    print(f'The response of the API call is: {response}')

    return 'response'

def sell_close_ongc_order():
    paytm_access_token = environ.get('PAYTM_ACCESS_TOKEN')

    # Call the access token API of Paytm
    url = 'https://developer.paytmmoney.com/orders/v1/place/regular'
    headers = {'x-jwt-token': paytm_access_token, 'Content-Type': 'application/json'}
    body = {'txn_type': 'S', 'exchange': 'BSE', 'segment': 'E', 'product': 'I', 'security_id': '500312', 'quantity': 1, 'validity': 'DAY', 'order_type': 'MKT', 'price': 0, 'source': 'W'}
    r = requests.post(url=url, headers=headers, json=body)

    response = r.json()

    print(f'The response of the API call is: {response}')

    return 'response'