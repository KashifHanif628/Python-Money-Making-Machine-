import streamlit as st  # this is install for UI purpose.
import random # it is install for random number generate between fetching the specific things.
import time  # its provide the time related all the facility
import requests  # it is very important. its help to api call data from the internet or any specific API.

st.title("💰 Money Making Machine 💰")

def generate_money():
    return random.randint(1, 1000)

st.subheader("💵 Instant Cash Generator 💵")
if st.button("💰 Generate Money 💰"): # if any user click on that button to generate the money then
    st.write("🔄 Counting Your Money...!") # this msg will show
    time.sleep(2) # here 2 seconds delay will show on the screen with the help of time.sleep module.
    amount = generate_money() # now amount will show after calling generate_money function into amount variable. 
    st.success(f"🎉 You made ${amount}! 💸") # we have passed here amount variabl to make the money.


def fetch_side_hustle(): # make a variabl to get the api data from side_hustle which we made in last class.
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles?apikey=123456')
        if response.status_code == 200: #status_code is already build in function which is coming from requests module. and we have put the value 200 as asume.
            hustles = response.json() #make a variabl of hustles and take the response from above which is show after try then show in the json formate.
            return hustles["side_hustle"] #square bracket used here to only show the hustle not with side_hustle and then hustle.
        else:
            return("🚀 Freelancing")
    except:
        return("⚠️ Something went wrong!")
    
st.subheader("🚀 Side Hustle Ideas 🚀") # create another heading
if st.button("🚀 Generate Hustle 🚀"): # add button for generate hustle
    idea = fetch_side_hustle() # make a variabl of idea and call the above function fetch_side_hustle to get hustle. 
    st.success(f"🔥 {idea}") # Added fire emoji for motivation


def fetch_money_Quotes():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?apikey=123456')
        if response.status_code == 200:
            quote = response.json()
            return quote["money_quote"]
        else:
            return("💡 Money is the root of all evil!")
    except:
        return("⚠️ Something went wrong")

st.subheader("💬 Money Making Motivation 💬") # create another heading
if st.button("💡 Get Inspired 💡"):
    quote = fetch_money_Quotes()
    st.info(f"💭 {quote}") # we can use here st.info, st.success or st.warning
