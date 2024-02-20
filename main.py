import streamlit as st
import pandas as pd
import numpy as np
import pickle
from transformers import pipeline


st.markdown(
    """
    <html>
        <head>
        </head>
        <body>
            <h1><center><span style="color: #673ee6">Welcom in👋</span><span >Hotel Rating 🏡</span></center></h1>
            <br>
            <br>
        </body>
    </html>
    """,
    unsafe_allow_html=True
)


st.write('-------')
st.markdown(
    """
    <html>
        <head>
        </head>
        <body>
            <h1><center><span style="color: #9c4949">Please fill out all fields</span></center></h1>
            <br>
            <br>
        </body>
    </html>
    """,
    unsafe_allow_html=True
)

Date_Month=st.number_input("please enter your Month ", min_value=0, max_value=12,value=0)

Date_Day=st.number_input("please enter your Day ", min_value=0, max_value=31,value=0) 

Hotel_Name=st.text_input('please Enter Hotel name',value='None')

Reviewer_Nationality=st.text_input('please Enter your  Nationality',value='None')

Hotel_city=st.text_input('please Enter Hotel City',value='None')


Trip_type= st.selectbox("Select an Trip type:",["Leisure trip", "Business trip"])

Booking_typs= st.selectbox("Select an Booking_typs:", ['Solo traveler', 'Couple','Group', 'Family with young children','Family with older children', 'Travelers with friends', 'With a pet'])

Room_Booking_types =st.text_input('please Enter Room Booking types',value='None')

Num_ofNights_user=st.number_input("please enter Number of Nights", min_value=0,value=0) 

Negative  = st.text_input("Enter your Negative message:",value='None')

Positive  = st.text_input("Enter your Positive  message:",value='None')

def get_Review_Total_Positive_Word_Counts( Anay_maasage ):
    tex = str(Anay_maasage)
    massage = tex.strip().split(' ')
    return len(massage)



Review_Total_Positive_Word_Counts = get_Review_Total_Positive_Word_Counts(Positive)

Review_Total_Positive_Word_Counts = get_Review_Total_Positive_Word_Counts(Negative)



st.write('------')
data_pass_to_model = []
Data=[]



if True:
    if Date_Month !=0:
        data_pass_to_model.append(Date_Month)


    if Date_Day != 0 :
        data_pass_to_model.append(Date_Day)

    if Hotel_Name != 'None':
        data_pass_to_model.append(Hotel_Name)
        Data.append(Hotel_Name)
        Hotel_Name=Hotel_Name

    if Reviewer_Nationality != 'None':
        data_pass_to_model.append(Reviewer_Nationality)

# hotel city 
    if Hotel_city != 'None':
        data_pass_to_model.append(Hotel_city)
        Data.append(Hotel_city)
        Hotel_city=Hotel_city

    if Trip_type == 'Leisure trip' or Trip_type == 'Business trip':
        data_pass_to_model.append(Trip_type)
        Data.append(Trip_type)
        Trip_type=Trip_type

    if Booking_typs == 'Solo traveler'  or Booking_typs == 'Couple' or Booking_typs == 'Group' or Booking_typs == 'Family with young children' or Booking_typs == 'Family with older children' or Booking_typs == 'Travelers with friends' or Booking_typs == 'With a pet':
        data_pass_to_model.append(Room_Booking_types)
        Data.append(Booking_typs)
        Booking_typs=Booking_typs


    if Room_Booking_types != 'None':
        data_pass_to_model.append(Room_Booking_types)
        Data.append(Room_Booking_types)
        Room_Booking_types=Room_Booking_types
    
    if Num_ofNights_user !=0:
        data_pass_to_model.append(Num_ofNights_user)


    if Negative !="None":
        data_pass_to_model.append(Negative)

    if Positive !="None":
        data_pass_to_model.append(Positive)


Review_Total_Negative_Word_Counts=get_Review_Total_Positive_Word_Counts(Negative)
Review_Total_Positive_Word_Counts=get_Review_Total_Positive_Word_Counts(Positive)
data_pass_to_model.append(Review_Total_Negative_Word_Counts)
data_pass_to_model.append(Review_Total_Positive_Word_Counts)





column_in_model=[Date_Month, Date_Day, Hotel_Name, Reviewer_Nationality, Review_Total_Negative_Word_Counts,
Review_Total_Positive_Word_Counts, Hotel_city, Trip_type, Booking_typs, Room_Booking_types, Num_ofNights_user,
'truncatedsvd00', 'truncatedsvd11', 'truncatedsvd22', 'truncatedsvd0', 'truncatedsvd1','truncatedsvd2']

#Tareget Encoder
with open('target_encoder.pkl', 'rb') as file:
    TargetEncoder= pickle.load(file)
file.close()

print(Hotel_Name,Hotel_Name,Hotel_city,Trip_type,Booking_typs,Room_Booking_types)

data1 = [{'Hotel_Name': Hotel_Name if Hotel_Name !=None else st.write("please Enter this fild"),
          'Reviewer_Nationality': Reviewer_Nationality if Reviewer_Nationality !=None else st.write("please Enter this fild"),
          'Hotel_city':Hotel_city if Hotel_city !=None else st.write("please Enter this fild"),
          'Trip_type': Trip_type,
          'Booking_typs': Booking_typs,
          'Room_Booking_types': Room_Booking_types if Room_Booking_types !=None else st.write("please Enter this fild")}]


df = pd.DataFrame(data1)
categorical_columns = ['Hotel_Name', 'Reviewer_Nationality', 'Hotel_city', 'Trip_type', 'Booking_typs', 'Room_Booking_types']

df_encoded1=None
if df['Hotel_Name'] is None or df['Reviewer_Nationality'] is None or df['Hotel_city'] is None or df['Room_Booking_types'] is None:
    st.error("Please fill in all required fields.")
else:
    df_encoded1=TargetEncoder.transform(df)
    df_encoded1 = list(df_encoded1.values[0])




encodeed_negative=None




if Negative != None:
    with open('saved_objects1.pkl', 'rb') as file:
        Negative_encoder= pickle.load(file)
    file.close()


    tfidf_vectorizer2_loaded = Negative_encoder['tfidf_vectorizer']
    svd2_loaded = Negative_encoder['svd']

    tttt=tfidf_vectorizer2_loaded.transform([Negative])
    xcxc=svd2_loaded.transform(tttt)
    encodeed_negative =list(xcxc[0])
else:
    st.error("please fill this field")

encodeed_Positive = None


if Positive != None:
    with open('saved_objects2.pkl', 'rb') as file:
        POS_encoder= pickle.load(file)
    file.close()


    tfidf_vectorizer2_loaded = POS_encoder['tfidf_vectorizer2']
    svd2_loaded = POS_encoder['svd2']

    tttt=tfidf_vectorizer2_loaded.transform([Positive])
    xcxc=svd2_loaded.transform(tttt)
    encodeed_Positive =list(xcxc[0])
else:
    st.error("please fill this field")


temp=[Review_Total_Negative_Word_Counts, Review_Total_Positive_Word_Counts]
temb1=[Date_Month, Date_Day ]
temp3=[Num_ofNights_user]
Data_Pass_to_Model1 = temb1 + df_encoded1[0:3] + temp + df_encoded1[3::] + temp3 + encodeed_negative + encodeed_Positive


print(Data_Pass_to_Model1)
st.markdown(
    """
    <html>
        <head>
        </head>
        <body>
            <h1><center><span style="color: #9c4949">This First Model</span></center></h1>
            <br>
            <br>
        </body>
    </html>
    """,
    unsafe_allow_html=True
)

if st.button("Click To Predict"):
    with open('model.pkl','rb')as file:
        model=pickle.load(file)
    file.close()
    pre_val = model.predict([Data_Pass_to_Model1])
    if pre_val[0] == 1:

        st.header(f"Model Predict This Hotel is Good 😍😍")
    if pre_val[0] == 0:

        st.header(f"Model Predict This Hotel is bad😓😓")


st.write('--------')
st.markdown(
    """
    <html>
        <head>
        </head>
        <body>
            <h1><center><span style="color: #9c4949">This sacond Model</span></center></h1>
            <br>
            <br>
        </body>
    </html>
    """,
    unsafe_allow_html=True
)

st.write(f"I recommend using this model.")

senanalysy= pipeline('sentiment-analysis')


if st.button("please click to pridict"):
    if Negative!=None and Positive !=None:
        pos= senanalysy(Positive)[0]['score']*100
        Neg = senanalysy(Negative)[0]['score']*100
        avg=(pos+Neg)/2
        print(avg)
        if avg >=50:
            st.header(f"Model Predict This Hotel is Good 😍😍")
        else:

            st.header(f"Model Predict This Hotel is bad😓😓")
