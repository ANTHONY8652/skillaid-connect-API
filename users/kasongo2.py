import requests
import time
import random


fun_messages = [
    "Boom! Another reason sent! 🚀",
    "Keep 'em coming! 💪",
    "Ruto's not gonna like this! 🔥",
    "Justice is served, one form at a time! ⚖️",
    "Another nail in the coffin! 🔨",
    "The truth shall set you free! 🕊️",
    "Corruption exposed! 🔍",
    "The people demand justice! ✊",
    "Transparency wins! 🏆",
    "Another step towards accountability! 🌟",
]



# List of reasons
reasons = [
    "Reason 1: International Criminal Court (ICC) Indictment: William Ruto was indicted by the ICC in 2011 for crimes against humanity related to the 2007-2008 post-election violence in Kenya, which resulted in over 1,000 deaths and the displacement of hundreds of thousands of people. Although the charges were later withdrawn in 2016 due to a lack of evidence and witness intimidation, the indictment itself is a significant mark against his record.",
    "Reason 2: Land Scandals: Ruto has been accused of involvement in the illegal acquisition of public land, including the notorious Weston Hotel land scandal. The Weston Hotel was allegedly built on land that belonged to the Kenya Civil Aviation Authority (KCAA), raising serious questions about his integrity and respect for public property.",
    "Reason 3: Maize Scandal: During his tenure as the Minister for Agriculture, Ruto was implicated in a maize scandal where the government allegedly purchased maize at highly inflated prices. This scandal led to significant financial losses for the country and highlighted his role in mismanaging public funds for personal gain.",
    "Reason 4: Argor Sugarcane Scandal: Ruto was linked to a scandal involving the Argor Sugarcane Factory, where he was accused of misappropriating funds meant for the revival of the factory. This incident further tarnished his reputation and raised concerns about his involvement in corrupt practices.",
    "Reason 5: 2022 Presidential Election Controversies: The 2022 Kenyan presidential election, in which Ruto emerged as the winner, was marred by controversies and legal challenges. His main opponent, Raila Odinga, contested the results, alleging irregularities and fraud, which cast a shadow over the legitimacy of his victory.",
    "Reason 6: Corruption Allegations: Throughout his career, Ruto has faced numerous allegations of corruption and misuse of public funds. These allegations have painted a picture of a politician deeply entrenched in corrupt practices, using his position to enrich himself and his associates.",
    "Reason 7: Use of Political Associates: Ruto has been criticized for using his friends and political associates to perpetuate theft of public funds. This nepotism and cronyism have contributed to a culture of corruption within the government, undermining public trust and accountability.",
    "Reason 8: Police Brutality and Human Rights Abuses: Ruto's administration has been accused of using police brutality to suppress opposition and criticism. Reports of abductions, killings, and human rights abuses under his watch have raised serious concerns about his commitment to democratic principles and human rights.",
    "Reason 9: Leasing National Assets: Ruto's government attempted to lease strategic national assets to Adani, an Indian conglomerate. This deal was halted after Adani was indicted in the USA courts for corruption, highlighting Ruto's willingness to engage in questionable deals that could compromise national interests.",
    "Reason 10: High-End Corruption Cases: Ruto has acknowledged that Kenya loses Ksh 2 billion daily to corruption but has done little to curb this vice. His inaction in the face of such rampant corruption has been a major disappointment and a failure of leadership.",
    "Reason 11: Suppression of Opposition: Any opposition to corruption under Ruto's administration has been met with police brutality and suppression. This authoritarian approach has stifled dissent and prevented meaningful accountability, further entrenching a culture of impunity.",
    "Reason 12: International Criminal Court (ICC) Indictment: William Ruto was indicted by the ICC in 2011 for crimes against humanity related to the 2007-2008 post-election violence in Kenya, which resulted in over 1,000 deaths and the displacement of hundreds of thousands of people. Although the charges were later withdrawn in 2016 due to a lack of evidence and witness intimidation, the indictment itself is a significant mark against his record.",
    "Reason 13: Land Scandals: Ruto has been accused of involvement in the illegal acquisition of public land, including the notorious Weston Hotel land scandal. The Weston Hotel was allegedly built on land that belonged to the Kenya Civil Aviation Authority (KCAA), raising serious questions about his integrity and respect for public property.",
    "Reason 14: Maize Scandal: During his tenure as the Minister for Agriculture, Ruto was implicated in a maize scandal where the government allegedly purchased maize at highly inflated prices. This scandal led to significant financial losses for the country and highlighted his role in mismanaging public funds for personal gain.",
    "Reason 15: Argor Sugarcane Scandal: Ruto was linked to a scandal involving the Argor Sugarcane Factory, where he was accused of misappropriating funds meant for the revival of the factory. This incident further tarnished his reputation and raised concerns about his involvement in corrupt practices.",
    "Reason 16: 2022 Presidential Election Controversies: The 2022 Kenyan presidential election, in which Ruto emerged as the winner, was marred by controversies and legal challenges. His main opponent, Raila Odinga, contested the results, alleging irregularities and fraud, which cast a shadow over the legitimacy of his victory.",
    "Reason 17: Corruption Allegations: Throughout his career, Ruto has faced numerous allegations of corruption and misuse of public funds. These allegations have painted a picture of a politician deeply entrenched in corrupt practices, using his position to enrich himself and his associates.",
    "Reason 18: Use of Political Associates: Ruto has been criticized for using his friends and political associates to perpetuate theft of public funds. This nepotism and cronyism have contributed to a culture of corruption within the government, undermining public trust and accountability.",
    "Reason 19: Police Brutality and Human Rights Abuses: Ruto's administration has been accused of using police brutality to suppress opposition and criticism. Reports of abductions, killings, and human rights abuses under his watch have raised serious concerns about his commitment to democratic principles and human rights.",
    "Reason 20: Kimwarer and Arror Dams Scandal: Ruto was implicated in the Kimwarer and Arror dams scandal, where billions of shillings were allegedly misappropriated. The project was meant to provide water to residents but ended up being a massive financial drain with little to show for it.",
    "Reason 21: National Youth Service (NYS) Scandal: Ruto was associated with the National Youth Service scandal, where billions of shillings were allegedly stolen through fraudulent payments. The scandal involved high-level government officials and raised questions about his oversight and accountability.",
    "Reason 22: Kenya Pipeline Company (KPC) Scandal: Ruto was linked to a scandal involving the Kenya Pipeline Company, where funds meant for the construction of pipelines were allegedly embezzled. This scandal highlighted his involvement in the mismanagement of public infrastructure projects.",
    "Reason 23: Health Ministry Scandal: During his tenure, the Ministry of Health was embroiled in a scandal where funds meant for healthcare were allegedly misappropriated. Ruto's involvement in this scandal further tarnished his reputation and raised concerns about his commitment to public health.",
    "Reason 24: Eurobond Scandal: Ruto was implicated in the Eurobond scandal, where billions of shillings raised through international bonds allegedly went missing. The scandal highlighted his role in the mismanagement of public debt and financial resources."
    "Reason 25: Sugar Importation Scandal: Ruto was linked to a scandal involving the importation of sugar, where duties were allegedly waived for politically connected individuals. This scandal highlighted his involvement in favoritism and the misuse of government powers for personal gain.",
    "Reason 26: Sugar Importation Scandal: Ruto was linked to a scandal involving the importation of sugar, where duties were allegedly waived for politically connected individuals. This scandal highlighted his involvement in favoritism and the misuse of government powers for personal gain.",
    "Reason 27: Fake Gold Scandal: Ruto was associated with a fake gold scandal, where high-level government officials were allegedly involved in a scheme to sell fake gold to international buyers. This scandal raised questions about his integrity and involvement in international fraud.",
    "Reason 28: Covid-19 Funds Scandal: During the Covid-19 pandemic, Ruto was implicated in the misappropriation of funds meant for the pandemic response. The scandal highlighted his involvement in the mismanagement of emergency funds and raised concerns about his commitment to public health and safety.",
    # Add more reasons here, up to 50 or more
]

def submit_reason(form_url, reason):
    data = {
        'entry.2083386595': 'William Ruto',
        'entry.238261122': reason,
        'dlut': '1732382257793',
        'fvv': '1',
        'partialResponse': '[null,null,"-7253853047925745288"]',
        'pageHistory': '0',
        'fbzx': '-7253853047925745288',
        'submissionTimestamp': str(int(time.time() * 1000))  # Use current timestamp
    }
    response = requests.post(form_url, data=data)
    if response.status_code == 200:
        print("Reason submitted successfully.")
    else:
        print(f"Failed to submit reason. Status code: {response.status_code}")
        time.sleep(7)  # Add a delay to avoid rate limiting

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()

def main():
    form_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeOXMDQ09jupP0RsqgQaer74C_Wi_BrFLJLj30HG-ZxAf3Bkw/formResponse'  # Replace with your actual form URL
    counter = 0
    total_duration = 72 * 60  # 72 hours in minutes
    interval = 10  #random int for minutes 1-10 che computer chooses
    num_submissions = total_duration // interval
    total_submissions = (total_duration * 60) // (10 * 60)  # Estimate total submissions


    for i in range(num_submissions):
        reason = reasons[i % len(reasons)]  # Cycle through the reasons list
        submit_reason(form_url, reason)
        counter += 1
        fun_message = random.choice(fun_messages)
        print(f"Reason {counter} submitted successfully. {fun_message}")
        print_progress_bar(counter, total_submissions, prefix='Progress:', suffix='Complete', length=100)

        time.sleep(interval * 60)  # Sleep for 10 minutes
        

if __name__ == "__main__":
    main()


##Logic if you want the computer to choose the amount of time to wait before sending another request
""""
def main():
    form_url = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse'  # Replace with your actual form URL
    total_duration = 72 * 60  # 72 hours in minutes
    start_time = time.time()

    while (time.time() - start_time) < (total_duration * 60):  # Convert total_duration to seconds
        reason = random.choice(reasons)  # Select a random reason from the list
        submit_reason(form_url, reason)
        wait_time = random.randint(5, 15)  # Random wait time between 5 to 15 minutes
        print(f"Waiting for {wait_time} minutes before the next submission.")
        time.sleep(wait_time * 60)  # Sleep for the random wait time in seconds

if __name__ == "__main__":
    main()
"""
