import streamlit as st
import requests
import pyrebase

fb = "https://electionapp-ab201-default-rtdb.asia-southeast1.firebasedatabase.app/AgentsDetails.json"

st.set_page_config(
    page_title="Agents Details",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('Please Fill In The Form as an Agent')
full_name = st.text_input('Enter your Full Name')

telephone=st.text_input('Enter your mobile number')
id_number=st.text_input('Enter your National ID No.')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.image(uploaded_file)


def uploading(id_number,uploaded_file):
    firebaseConfig = {
    'apiKey': "AIzaSyDHSZ0a5InIgBrKPadwZm81YWYwrB658xo",
    'authDomain': "electionapp-ab201.firebaseapp.com",
    'databaseURL': "https://electionapp-ab201-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "electionapp-ab201",
    'storageBucket': "electionapp-ab201.appspot.com",
    'messagingSenderId': "15977905127",
    'appId': "1:15977905127:web:c6dfce37dde0336c211b42",
    'measurementId': "G-330053BT4Q",
    'serviceAccount':'serviceAccount.json'
    };
    firebase=pyrebase.initialize_app(firebaseConfig)
    storage=firebase.storage()
    img = storage.child(f'{id_number}.jpg').put(uploaded_file)
    return img







btn = st.button('Submit')
if btn:
    AgentData = {'FullName':full_name,'TelephoneNo':telephone,'IdNumber':id_number}
    send = requests.post(fb,json=AgentData)
    uploading(id_number,uploaded_file)
    if (send):
        print(send)
    else:
        pass



