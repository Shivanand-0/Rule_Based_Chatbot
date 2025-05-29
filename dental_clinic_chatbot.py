import re;     # imported re or regEx or reguler expression module to finds exact patterns in strings

# response of FAQ 
faq_responses = {
        1: "We are open from 9 AM to 5 PM, Monday to Saturday.",    #"what are your working hours?"
        2: "We are located at gittikhadan,Nagpur.",     #where are you located?
        3: "Yes, we do accept walk-ins, but appointments are preferred.",   #do you accept walk-in appointments?
        4: "We offer cleaning, whitening, braces, implants, and regular check-ups.",  #what services do you offer?
        5:"You can call us at +91 9911223344 or email us at dental@gmail.com.",  #how can i contact you?
        6:"Yes, we have a pediatric dentist who specializes in treating children."  #Do you treat kids?
    }
 
 # chat_processor function: matches pattern and response accordingly
def chat_processor(command):
    if re.search(r"\bhello\b|\bhii\b|\bhelp\b|\bgood morning\b|\bhey\b|\bwelcome back\b", command):      #greet
        return "Hello! how can i help you?"
    elif re.search(r"\bwhat\b", command) and re.search(r"\b(working hours|working time|hours|time|clinic time)\b", command):
        return faq_responses[1]
    elif re.search(r"\b(what|where)\b",command) and re.search(r"\b(located|location|office|clinic|hospital)\b",command):
        return faq_responses[2]
    elif re.search(r"\b(walk-in appointments|appointments)\b",command):
        return faq_responses[3]
    elif re.search(r"\bwhat\b",command) and re.search(r"\b(services do you offer|services offer|services)\b",command):
        return faq_responses[4]
    elif re.search(r"\b(how|what)\b",command) and re.search(r"\bcontact\b",command):
        return faq_responses[5]
    elif re.search(r"\btreat kids\b",command):
        return faq_responses[6]
    else:
        return "Sorry, I don't know that yet."    #not matching responce



while 1:
    command= input('you: ' )    #user input or command or question
    if re.search(r"\bbye\b|\bexit\b|\bterminate\b|\bquit\b", command):    
        print("Bot: Good Bye!")                                       #responce of termination 
        break;
    response= chat_processor(command.lower());   #handling responce for patient
    print("Bot: ",response)