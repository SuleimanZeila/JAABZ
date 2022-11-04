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
    stored = storage.child(id_number+'.jpg').put(uploaded_file)
    return stored

uploading(232323232,'download.png')