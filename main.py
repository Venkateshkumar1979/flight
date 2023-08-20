import streamlit as st
from datetime import datetime,timedelta
import pickle
import numpy as np
st.title('Flight Price Prediction')

airline =	st.sidebar.selectbox('Airlines',[None,'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST','Indigo','Air_India'])
airline_dict={'AirAsia':0,'Indigo':1,'GO_FIRST':2,'SpiceJet':3,'Air_India':4,'Vistara':5}

source_city =st.sidebar.selectbox('Source City',[None,'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
source_dict={'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Kolkata':4,'Chennai':5}

departure_time = st.sidebar.selectbox('Departure Time',[None,'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night','Late_Night'])
departure={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}

stops = st.sidebar.selectbox('Stops',[None,'Zero','one','two_or_more'])
stops_dict={'Zero':0,'one':1,'two_or_more':2}

arrival_time =st.sidebar.selectbox('Arrival Time',[None,'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night','Late_Night'])
arrival={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}

destination_city =st.sidebar.selectbox('Destination City',[None,'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
desitination={'Delhi':0,'Hyderabad':1,'Mumbai':2,'Bangalore':3,'Chennai':4,'Kolkata':5}

Class =st.sidebar.selectbox('Class',[None,'Economy','Business'])
Class_dict={'Economy':0,'Business':1}

departure_date=st.sidebar.date_input('Departure Date',min_value=datetime.today(),max_value=datetime.today()+timedelta(50))

date_diff=datetime.strptime(str(departure_date),'%Y-%m-%d')-datetime.today()
days_left =int(date_diff.days+1)
#st.write(days_left)

data=[airline,source_city,departure_time,stops,arrival_time,destination_city,Class,days_left]
if None not in data and st.button('Predict'):
    features=[airline_dict[airline],source_dict[source_city],
              departure[departure_time],stops_dict[stops],
              arrival[arrival_time],desitination[destination_city],Class_dict[Class],days_left]
    model=pickle.load(open('flight_linear.pkl','rb'))
    predict=model.predict([features])[0]
    st.title(f'Your Flight Price is INR {(predict.round(2))}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    