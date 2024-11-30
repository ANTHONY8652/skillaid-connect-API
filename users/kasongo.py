import requests
import time

def submit_google_form(form_url, data, num_submissions):
    for i in range(num_submissions):
        response = requests.post(form_url, data=data)
        if response.status_code == 200:
            print(f"Form {i+1} submitted successfully.")
        else:
            print(f"Failed to submit form {i+1}. Status code: {response.status_code}")
        time.sleep(1)  # Add a delay to avoid rate limiting

# Example usage
form_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeOXMDQ09jupP0RsqgQaer74C_Wi_BrFLJLj30HG-ZxAf3Bkw/formResponse'  # Replace with your actual form URL
data = {
    'entry.2083386595': 'William Ruto',
    'entry.238261122': 'Reason: Since his inauguration in 2022, president Ruto has gone in a theft spree in the country leading to high end corruption cases while acknowledging that the country loses ksh 2 billion daily and he had done nothing to curb the vice. Recently, his government wanted to lease strategic national assets to Adani, a corrupt Indian Conglomerate until the later was indicted in the USA courts. He uses his friends and political associates to perpetuate theft of public funds and any opposition to corruption has so far been met with police brutality, abductions and killings of innocent Kenyans',
    'dlut': '1732382257793',
    'fvv': '1',
    'partialResponse': '[null,null,"-7253853047925745288"]',
    'pageHistory': '0',
    'fbzx': '-7253853047925745288',
    'submissionTimestamp': '1732382258764'
}
num_submissions = 5  # Number of times you want to submit the form

submit_google_form(form_url, data, num_submissions)
