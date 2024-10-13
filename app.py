from flask import Flask, request

app = Flask(__name__)

@app.route('/get_resource_token/')
def get_resource_token():
    success = request.args.get('success')
    print(f'The query parameter is: {success} and the type of this variable is {type(success)}')
    if success == 'true':
        request_token = request.args.get('requestToken')
        print(f'The request token is: {request_token}')
    
    return 'Success'

@app.route('/get_access_token/')
def get_access_token():
    access_token = request.args.get('accessToken')
    print('This is the Access Token: {access_token}')

if __name__ == '__main__':
    app.run()