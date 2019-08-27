# import requests
import json

# Channel webhook definitions

slack_webhook = "https://hooks.slack.com/services/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"

gchat_webhook = "https://chat.googleapis.com/v1/spaces/AAAAnUmAWv4/messages?key=" \
                "AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=g0YZh_JbbAvThOjf5ZSmJvCSpC2WaQaTgbzEIiN1x4g%3D&" \
                "threadKey=TeamCityNotificationsNew"

# Default Payloads
payload_slack = {
    "username": "TeamCity Notification",
    "channel": "#qa",
    "text": "",
    "icon_emoji": ":teamcity:",
}

payload_googlechat = {
    "text": ""
}


def chat_helper(text):
    payload_slack["text"] = text
    payload_googlechat["text"] = text

    # requests.post(slack_webhook, json.dumps(payload_slack))
    # requests.post(gchat_webhook, json.dumps(payload_googlechat))
