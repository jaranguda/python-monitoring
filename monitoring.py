#!/usr/bin/env python

import requests
import json
import yaml
import os


domain_file = os.environ['DOMAIN_FILE']

def check_url(url):
  status_code = ""
  error_messages= ""
  try:
    r = requests.get(url, timeout=10)
    if(r.ok):
      status_code = r.status_code
    else:
      status_code = r.status_code

  except requests.exceptions.HTTPError as err:
    error_messages = err
  except requests.exceptions.ConnectionError as err:
    error_messages = err
  except requests.exceptions.Timeout as err:
    error_messages = err
  except requests.exceptions.RequestException as err:
    error_messages = err
  finally:
    if status_code is not None:
        http_status_code = status_code
    else:
        http_status_code = ""
    if error_messages is not None:
        err_msg = error_messages
    else:
        err_msg = ""

    response = dict();
    response['status_code'] = http_status_code
    response['err_msg'] = str(err_msg).replace("'",'')
    return response

with open(domain_file, 'r') as file:
  urls = yaml.safe_load(file).items()
  for key,values in urls:
    for value in values:
      getData = check_url(value['url'])

      logs = {
      "project": key,
      "name": value['name'],
      "url": value['url'],
      "status_code": getData['status_code'],
      "messages": getData['err_msg']
      }

      print(logs)
