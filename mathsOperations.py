import json

def lambda_handler(event, context):
    print (event)
    #number1=json.loads(event['queryStringParameters'][number1])
    #number2=json.loads(event['queryStringParameters'][number2])
    nos1=event['queryStringParameters']['number1']
    nos2=event['queryStringParameters']['number2']
    print ("number 1 is "+ nos1)
    print ("number 2 is "+ nos2)
    number3 = int(nos1) + int(nos2)
    print ("number3 is "+ str(number3))
    numberResponse = {}
    numberResponse['number1'] = nos1
    numberResponse['number2'] = nos2
    numberResponse['number3'] = number3
    
    responseObject = {}
    responseObject['body']=json.dumps(numberResponse)
    return responseObject
