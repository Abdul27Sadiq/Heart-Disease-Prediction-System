
import numpy as np
import pickle


# Loading the saved Model
loaded_model = pickle.load(open(r'C:\Users\abdul\Downloads\machine\core\code/trained_model_sav', 'rb'))

input_data = (49,1,1,130,266,0,1,171,0,0.6,2,0,2)

# Change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('The person is not suffering from Heart Disease')
else:
   print('The person is suffering from Heart Disease')
