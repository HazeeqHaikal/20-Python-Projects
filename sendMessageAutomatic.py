import accountDetail
import requests
import schedule
import time

def sendMessage():
    resp = requests.post('https://textbelt.com/text', {
        'phone': accountDetail.phoneNumber,
        'message': 'Good morning, Haikal. This is an automated message.',
        'key': 'textbelt',
    })
    
    print(resp.json())

if __name__ == "__main__":
    schedule.every().day.at("08:00").do(sendMessage)
    # schedule.every(10).seconds.do(sendMessage)
    while True:
        schedule.run_pending()
        time.sleep(1)