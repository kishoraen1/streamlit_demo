import streamlit as st 
import joblib 

st.title("Iris Flower classification")

#using the model already created before
reloaded_model = joblib.load('iris_joblib')


# sliders for input features 
sepal_length = st.slider("Sepal Length ", 4.3,7.9)
sepal_width = st.slider("Sepal width ", 2.0,4.4)
petal_length = st.slider("Petal Length ", 1.0,6.9)
petal_width = st.slider("Petal Width ", 0.1,2.5)


#predict the output category
y_pred = reloaded_model.predict([[sepal_length,sepal_width,petal_length,petal_width]])


if st.button('Predict'):
    st.title(y_pred[0])
