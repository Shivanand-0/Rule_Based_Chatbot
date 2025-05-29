import re;     


faq_responses = {
        1: "We are open from 9 AM to 5 PM, Monday to Saturday.",    #"what are your working hours?"
        2: "We are located at gittikhadan,Nagpur.",     #where are you located?
        3: "Yes, we do accept walk-ins, but appointments are preferred.",   #do you accept walk-in appointments?
        4: "We offer cleaning, whitening, braces, implants, and regular check-ups.",  #what services do you offer?
        5:"You can call us at +91 9911223344 or email us at dental@gmail.com.",  #how can i contact you?
        6:"Yes, we have a pediatric dentist who specializes in treating children."  #Do you treat kids?
    }
 
def chat_processor(command):
    if re.search(r"\bhello\b|\bhii\b|\bhelp\b|\bgood morning\b|\bhey\b|\bwelcome back\b", command):
        return "Hello! how can i help you?"
    elif (re.search(r"(\bwhat\b)",command) and re.search(r"(\bworking hours\b|\bworking time\b|\bhours\b|\btime\b||\bclinic time\b|)",command)):
        return faq_responses[1]
    elif re.search(r"(\bwhat\b|\bwhere\b|)",command) and re.search(r"(\blocated\b|\blocation\b|\boffice\b|\bclinic\b|\bhospital\b)",command):
        return faq_responses[2]
    elif re.search(r"(\bwalk-in appointments\b|\bappointments\b)",command):
        return faq_responses[3]
    elif re.search(r"(\bwhat\b)",command) and re.search(r"(\bservices do you offer\b|\bservices offer\b|\bservices\b)",command):
        return faq_responses[4]
    elif re.search(r"(\bhow\b|\bwhat\b)",command) and re.search(r"(\bcontact\b)",command):
        return faq_responses[5]
    elif re.search(r"(\btreat kids\b)",command):
        return faq_responses[6]
    else:
        return "Sorry, I don’t know that yet."



while 1:
    command= input('you: ' )
    if re.search(r"\bbye\b|\bexit\b|\bterminate\b|\bquit\b", command):
        print("Bot: Good Bye!")
        break;
    response= chat_processor(command.lower());
    print("Bot: ",response)