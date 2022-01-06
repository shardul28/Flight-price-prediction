from pkg_resources import SOURCE_DIST
import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image


original_title = '<h1 style="color:White; font-size: 20px;">Created by Shardul Tambe</h1>'

st.title('Flight Price Prediction')
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpaperaccess.com/full/254381.jpg")
        ;background-size:     cover;
        background-repeat:   no-repeat;
        background-position: center center;
    }
   .sidebar .sidebar-content {
        background: url("https://wallpaperaccess.com/full/254381.jpg")

    }
    </style>
    """,
    unsafe_allow_html=True
)
#image = Image.open('bb.jpg')
#st.image(image, '')

# FUNCTION
def user_report():
    def monthToNum(shortMonth):
        return {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12}[shortMonth.lower()]
    #first categorical data Total_Stops has total 5 categories

#Additional_Info has total 9 categories

#Day has total 10 categories

#Month has total 4 categories

#Duration has total 338 categories
    algolist=['ExtraTreeRegressor','RandomForestRegressor','XGBRegressor','GradientBoostingRegressor','DecisionTreeRegressor']
    Algorithm = st.selectbox('Select Classifier',algolist)
    airlinelist=['IndiGo', 'Air India', 'SpiceJet', 'Jet Airways',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Multiple carriers Premium economy',
       'Trujet', 'Jet Airways Business']
    airline = st.selectbox('Select Airline',airlinelist)
    Total_Stopslist=[0,1, 2, 3, 4]
    Total_Stops = st.selectbox('Select Number of Stops',Total_Stopslist)

    Monthlist=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
    Duration=st.slider('Duration of the Flight',0,3000,1)
    Daylist=[]
    for i in range(1,31):
        Daylist.append(i)
    Day= st.selectbox('Select Day',Daylist)
    Month= st.selectbox('Select Month',Monthlist)
    Sourcelist=['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
    Source= st.selectbox('Select Source',Sourcelist)
    Destlist=['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
    Destination= st.selectbox('Select Destination',Destlist)
    Additional_Infolist=['No Info', 'In-flight meal not included',
       'No check-in baggage included', '1 Short layover',
       '1 Long layover', 'Change airports', 'Business class',
       'Red-eye flight', '2 Long layover']
    Additional_Info = st.selectbox('Additional Info',Additional_Infolist)
    additional_info=Additional_Info
    if(airline=='Jet Airways'):
        Air_Asia=0
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='IndiGo'):
            Air_Asia=0
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_Asia=0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_Asia=0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_Asia=0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
    elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_Asia=0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Air_Asia=0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Air_Asia=0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia=0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia=0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

    elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia=0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
    elif (airline=='Air Asia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Air_Asia=1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

    else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
    if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=0


    elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=0


    elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Bangalore=0


    elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Bangalore=0

    elif (Source == 'Bangalore'):
            s_Delhi = 0
            s_Bangalore=1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

    else:
            s_Delhi = 0
            s_Bangalore=0

            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
    if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0


    elif (Destination== 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0

    elif (Destination== 'Bangalore'):
            d_Cochin = 0
            d_Delhi = 1
            d_Bangalore=1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Bangalore=0

            d_Kolkata = 0

    elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Bangalore=0

            d_Hyderabad = 0
            d_Kolkata = 1

    else:
            d_Cochin = 0
            d_Delhi = 0
            d_Bangalore=0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
#######################################################
    if (additional_info=='No Info'):
             No_Info=1
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='In-flight meal_not_included'):
             No_Info=0
             In_flight_meal_not_included=1
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='No_check-in_baggage_included'):
             No_Info=0 
             In_flight_meal_not_included=0,
             No_check_in_baggage_included=1,
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='1_Short_layover'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=1
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0
    if (additional_info=='1_Long_layover'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=1
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='Change_airports'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=1
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='Business_class'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=1
             Red_eye_flight=0
             Two_Long_layover=0

    if (additional_info=='Red_eye_flight'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=1
             Two_Long_layover=0

    if (additional_info=='2_Long_layover'):
             No_Info=0
             In_flight_meal_not_included=0
             No_check_in_baggage_included=0
             One_Short_layover=0
             One_Long_layover=0
             Change_airports=0
             Business_class=0
             Red_eye_flight=0
             Two_Long_layover=1
             '''
     Total_stops,
            Day,
            Month,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi,
            No_Info,
            In_flight_meal_not_included,
            No_check-in_baggage_included,
            One_Short_layover,
            One_Long_layover,
            Change_airports,
            Business_class,
            Red_eye_flight,
            Two_Long_layover'''
    month=monthToNum(Month)
    user_report_data ={'Total_Stops':Total_Stops, 'Additional_Info':additional_info, 'Day':Day, 'Month':month, 'Duration':Duration,
       'Airline_Air Asia':Air_Asia, 'Airline_Air India':Air_India, 'Airline_GoAir':GoAir,
       'Airline_IndiGo':IndiGo, 'Airline_Jet Airways':Jet_Airways, 'Airline_Jet Airways Business':Jet_Airways_Business,
       'Airline_Multiple carriers':Multiple_carriers,
       'Airline_Multiple carriers Premium economy':Multiple_carriers_Premium_economy, 'Airline_SpiceJet':SpiceJet,
       'Airline_Trujet':Trujet, 'Airline_Vistara':Vistara, 'Airline_Vistara Premium economy':Vistara_Premium_economy,
       'Source_Banglore':s_Bangalore ,'Source_Chennai':s_Chennai, 'Source_Delhi':s_Delhi, 'Source_Kolkata':s_Kolkata,
       'Source_Mumbai':s_Mumbai, 'Destination_Banglore':d_Bangalore, 'Destination_Cochin':d_Cochin,
       'Destination_Delhi':d_Delhi, 'Destination_Hyderabad':d_Delhi, 'Destination_Kolkata':d_Kolkata,
       'Destination_New Delhi':d_Kolkata}
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data,Algorithm

user_data,alg = user_report()
original_title = '<h1 style="color:White; font-size: 30px;">Flight Data</h1>'
st.markdown(original_title, unsafe_allow_html=True)
st.write(user_data)

user_data['Additional_Info'] = user_data['Additional_Info'].map({
    'No Info':0,
    'In-flight meal not included':1,
    'No check-in baggage included':2,
    '1 Short layover':3,
    '1 Long layover':4,
    'Change airports':5,
    'Business class':6,
    'Red-eye flight':7,
    '2 Long layover':8
})
Algorithm=alg
if Algorithm=="ExtraTreeRegressor":
        model = pickle.load(open('ExtraTreeRegressormodel.sav', 'rb'))
        print()
elif Algorithm=="RandomForestRegressor":
        model = pickle.load(open('RandomForestRegressormodel.sav', 'rb'))

        print()
elif Algorithm=="XGBRegressor":
        model = pickle.load(open('XGBRegressormodel.sav', 'rb'))

        print()
elif Algorithm=="GradientBoostingRegressor":
        model = pickle.load(open('GradientBoostingRegressor.sav', 'rb'))
        print()
else:
        print()
        model = pickle.load(open('DecisionTreeRegressormodel.sav', 'rb'))
salary = model.predict(user_data)
st.subheader('Flight price range')
#0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).


#st.subheader('The mobile price range is'+str(np.round(salary[0], 2)))
st.subheader('The Flight price is approx. :'+str(np.round(salary[0], 2))
