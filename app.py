from flask import Flask, request
from os import environ
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import paytm_money_operations

app = Flask(__name__)

def test_schedule():
    print("Scheduler is alive")

sched = BackgroundScheduler(daemon=True)
# sched.add_job(get_paytm_holdings_value, 'interval', minutes=1)
sched.start()

trigger_start = CronTrigger(
    year="*", month="*", day="*", hour="09", minute="15", second="0"
)

trigger_end = CronTrigger(
    year="*", month="*", day="*", hour="15", minute="10", second="0"
)
sched.add_job(
    paytm_money_operations.sell_close_ongc_order,
    trigger=trigger_start,
)

sched.add_job(
    paytm_money_operations.buy_open_ongc_order,
    trigger=trigger_end,
)

@app.route('/get_resource_token/')
def get_resource_token():
    success = request.args.get('success')
    print(f'The query parameter is: {success} and the type of this variable is {type(success)}')
    if success == 'true':
        request_token = request.args.get('requestToken')
        print(f'The request token is: {request_token}')
        environ['PAYTM_REQUEST_TOKEN'] = request_token

        # Calling the generation of the access token also
        get_access_token()
    
    return 'Success'

@app.route('/get_access_token/')
def get_access_token():
    access_token = request.args.get('accessToken')
    print('This is the Access Token: {access_token}')
    paytm_request_token = environ.get('PAYTM_REQUEST_TOKEN')
    paytm_api_key = environ.get('PAYTM_API_KEY')
    paytm_api_secret = environ.get('PAYTM_API_SECRET')
    print(f'This is the request token in another API call: {paytm_request_token}')

    # Call the access token API of Paytm
    url = 'https://developer.paytmmoney.com/accounts/v2/gettoken'
    data = {'api_key': paytm_api_key, 'api_secret_key': paytm_api_secret, 'request_token': paytm_request_token}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)

    response = r.json()
    access_token = response['access_token']
    environ['PAYTM_ACCESS_TOKEN'] = access_token

    print(f'The response of the API call is: {access_token}')

    return 'paytm_access_token'

@app.route('/get_holdings_value/')
def get_holdings_value():
    paytm_access_token = environ.get('PAYTM_ACCESS_TOKEN')

    # Call the access token API of Paytm
    url = 'https://developer.paytmmoney.com/holdings/v1/get-holdings-value'
    headers = {'x-jwt-token': paytm_access_token}
    r = requests.get(url=url, headers=headers)

    response = r.json()

    print(f'The response of the API call is: {response}')

    return 'response'

if __name__ == '__main__':
    app.run()