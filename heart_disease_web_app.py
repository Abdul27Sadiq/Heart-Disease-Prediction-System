import numpy as np
import pickle
import streamlit as st

# Loading the saved Model
loaded_model = pickle.load(open(r'C:\Users\abdul\Downloads\machine\core\code/trained_model_sav','rb'))

# Creating a function for Prediction

def heart_prediction(input_data):

    # Change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
      return 'The person is not suffering from Heart Disease'
    else:
       return 'The person is suffering from Heart Disease'

def main():
    
    # Give a Title
    st.title('Heart Disease Prediction Web App')
    
    # Getting the input from the user
    age = st.text_input("what is the Age")
    sex = st.text_input("Male or Female")
    cp = st.text_input("what is cp")
    trestbps = st.text_input("what is trestbps")
    chol = st.text_input("what is chol")
    fbs = st.text_input("what is fbs")
    restecg = st.text_input("what is restecg")
    thalach = st.text_input("what is thalach")
    exang = st.text_input("what is exang")
    oldpeak = st.text_input("what is oldpeak")
    slope = st.text_input("what is slope")
    ca = st.text_input("what is ca")
    thal = st.text_input("what is thal")
    
    # Code for Prediction
    heart = ''
    
    # Creating a button for Prediction
    if st.button('Heart Test Result'):
        
         # Convert all inputs to float
        input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),
                      float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
        
          # Make prediction
        heart = heart_prediction(input_data)
        
        st.success(heart)
      
if __name__ == '__main__':
         main()