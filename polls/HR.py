import urllib.request
import json

data = {
    "Inputs": {
        "input1":
            [
                # {
                    # 'satisfaction_level': "0.34",
                    # 'last_evaluation': "0.34",
                    # 'number_project': "1",
                    # 'average_montly_hours': "1",
                    # 'time_spend_company': "1",
                    # 'Work_accident': "1",
                    # 'left': "1",
                    # 'promotion_last_5years': "1",
                    # 'department': "Sales",
                    # 'salary': "HIgh",
                    {'satisfaction_level': '24', 'last_evaluation': '4.5', 'left': "1",'number_project': 2, 'average_montly_hours': 2, 'time_spend_company': 2, 'Work_accident': 2, 'promotion_last_5years': 2, 'department': 'sales', 'salary': 'Low'}
                # }
            ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/4c65cbce7ecf40f2bf7c75eafe8191ef/services/a0e6771c07104d1a9a7075b09098e345/execute?api-version=2.0&format=swagger'
api_key = 'kHiRrxJUPXWpoEnykOD7Byxt4Lw0kBTpYsi872c4SsHFH9UlmcfpMvKGrkY5Y7AqKtDG0Q7GsRSTBpOkiCzVZQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
#
#
import re
# import json
# file_object = open(r"C:\Users\xsmaddurve\Downloads\Chaitanya_Pratice\HR_Prediction\output_code.txt", 'r')
# data_to_read = file_object.read()
#
# # json_code = json.loads(data_to_read,
# #                        encoding='utf-8')
# print(file_object.read())
# print(data_to_read)
# file_object.close()
# print(json_code)