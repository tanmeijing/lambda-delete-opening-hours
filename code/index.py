import sys
import logging
import pymysql
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
## Construct body of the response object
    transactionResponse = {}
    
#### DUMMY RETURN
    transactionResponse['id'] = '1'
    transactionResponse['username'] = 'customer1'
    transactionResponse['password'] = 'password1'
    transactionResponse['uin'] = 'S1234567X'
    transactionResponse['name'] = 'customer tan'
    transactionResponse['dob'] = '01/01/1990'
    transactionResponse['sex'] = 'm'
    transactionResponse['addr'] = 'Apple Street'
    transactionResponse['contactNo'] = '12345678'
    transactionResponse['email'] = 'dogs@hotmail.com'
    
# Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type']='application/json'
    responseObject['body'] = json.dumps(transactionResponse, sort_keys=True,default=str)

    return responseObject