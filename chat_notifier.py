import requests
import json

message = {
    'text': 'Ignore Me one last time!'
}

webhook = 'https://chat.googleapis.com/v1/spaces/AAAAnUmAWv4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&' \
          'token=g0YZh_JbbAvThOjf5ZSmJvCSpC2WaQaTgbzEIiN1x4g%3D&threadKey=TeamCityNotifications'

requests.post(webhook, json.dumps(message))

