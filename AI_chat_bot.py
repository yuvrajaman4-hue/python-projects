#AI chat bot project-rule based chat assistant

import datetime
import time
presenthour =datetime.datetime.now().hour
name= input("welcome, Enter your name:")
if 5<= presenthour<=11:
    print("Good morning,", name)
elif 11<=presenthour<=17:
    print("Good Afternoon,",name)
elif 17<= presenthour<=21:
    print("Good Evening," , name)
else:
    print("Good night,",name)


print("hello! welcome to your personalized chatbot")
print("Ask me your questions, or type 'bye' to exit")
#chatbot memory creation ( using dictionary of responses)
responses={
    "hello":"Hi, How can i help you?",
    "how are you":"I am fine. hwo you doin",
    "Who are you":" I am your AI chat assistant",
    "motivate me":"its not wealth you seek , its all about becomimg the best",
    "I feel happy":"its great ! being happy is priceless, touch wood",
    "summarize functions":"Its an algorithm and, converts a given input to a certain output following the rules defined"

}
def getResponseofbot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return"I am still in learning phase, just hold on for a while"
while True:
    userInput= input("please ask your question:")
    reply=getResponseofbot(userInput)
    print("Bot response:", reply)
    if "bye" in userInput.lower():
        break

