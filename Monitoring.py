import streamlit as st
import pandas as pd
import urllib.request
import requests
import threading
import json
import random
import plotly.express as px
import time
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import requests
import json
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def animated_gauge_progress_bar(value, title , rmin , rmax):
    if 1 <= value <= 10:
        bar_color = "red"
    else:
        bar_color = "#4CAF50"  # Default color for other values



    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{'type': 'indicator'}]]
    )
    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 50, 'position': 'top'},
        gauge=dict(
            axis=dict(range=[rmin, rmax]),
            bar=dict(color='black'),  # Set color dynamically
            bgcolor="white",
            borderwidth=2,
            bordercolor="gray",
            steps=[dict(range=[0, 100], color="lightgray")]
        ),
        title=dict(text=title, font=dict(size=20)),  # Set title directly within the trace
    ))

    fig.update_layout(
        height=200,
        margin=dict(l=15, r=15, b=15, t=60),
    )

    return fig


def guageCreator(vlaue , title, rmin , rmax):

        # Streamlit app
        chart_placeholder = st.empty()
        vla = round(vlaue)
        if vla <= 1 :
            animated_chart = animated_gauge_progress_bar(vlaue, title, rmin, rmax)
            chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
        # Update the progress value with an animation
        else:
            for value in range(0, vla, 1):
                time.sleep(0.06)
                animated_chart = animated_gauge_progress_bar(value, title, rmin, rmax)
                chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
                st.empty()  # Clear the previous chart to create animation effect

def get_field_data(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    print(field_data[len(field_data)-1]['created_at'])
    # Extracting values for the specified field
    values = [field_data[1][f'field{field_number}']]
    time = field_data[len(field_data)-1]['created_at']
    return values


def get_field_datas(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    time=[]
    val=[]
    df = pd.DataFrame()
    for data in field_data:
        time.append(data['created_at'])
        val.append(data[f'field{field_number}'])

    df['time'] = time
    df['value'] = val
    print(field_data)
    # Extracting values for the specified field
    return df

def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """
def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """

def getPakChoyData(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": nutreint,
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    print("$$$$$$$$$$$$$$$$$$$")
    print(data)
    time = []
    val = []
    dataframe = pd.DataFrame()

    for d in data['data']:
        val.append(d['value'])
        time.append(d['readingAt'])

    dataframe['time'] = time
    dataframe['value'] = val
    print("$$$$$$$$$$$$$$$$$$$")
    return dataframe


def get_field_data(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    print(field_data[len(field_data)-1]['created_at'])
    # Extracting values for the specified field
    values = [field_data[1][f'field{field_number}']]
    time = field_data[len(field_data)-1]['created_at']
    return values


def get_field_datas(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    time=[]
    val=[]
    df = pd.DataFrame()
    for data in field_data:
        time.append(data['created_at'])
        val.append(data[f'field{field_number}'])

    df['time'] = time
    df['value'] = val
    print(field_data)
    # Extracting values for the specified field
    return df

def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """

def getPakChoyData(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": nutreint,
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    time = []
    val = []
    dataframe = pd.DataFrame()

    for d in data['data']:
        val.append(d['value'])
        time.append(d['readingAt'])

    dataframe['time'] = time
    dataframe['value'] = val
    print("$$$$$$$$$$$$$$$$")
    print(dataframe)
    print("$$$$$$$$$$$$$$$$")
    return dataframe


def getPakChoyDatas(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": "Temperature",
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    return data

def cardCreator(title , value):

    html_code = """
    <html>
        <style>
            .status-card {
                background-color: #c1f0c1; /* Light green color */
                padding: 20px;
                border-radius: 50%; /* Make it circular */
                width: 200px; /* Set a fixed width for the circular card */
                height: 200px; /* Set a fixed height for the circular card */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
        </style>"""

    html_code =  html_code + f"""<div class='status-card'>
            <h5>{title}</h5>
            <p> {value} </p>
        </div>
        </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def textwithboarder(title, text):
    html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">{title}</h3>
                                <p>{text}</p>
                            </div>"""
    # Show the Guage of the Nutrients levels
    st.markdown(html_content, unsafe_allow_html=True)

def MonitoringConstructor():
    option2 = option_menu(None, ["Pak choy", "Rice", "Aqua"],
                                  menu_icon="forward", default_index=0, orientation="horizontal",
                                  styles={
                                      "container": {"padding": "0!important", "background-color": "#fafafa"},
                                      "icon": {"color": "orange", "font-size": "15px"},
                                      "nav-link": {"font-size": "15px", "text-align": "right", "margin": "0px",
                                                   "--hover-color": "#eee", },
                                      "nav-link-selected": {"background-color": "green"},
                                  }
                                  )
    if option2 == "Aqua":
        fieldname = {'Field 1': 'Temperature', 'Field 2': 'pH', 'Field 3': 'Ammonia', 'Field 4': 'DO',
                     'Field 5': 'Salinity'}
        all_data = {fieldname[f'Field {i}']: get_field_data(i) for i in range(1, 6)}
        html = f"""

                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                        <h3 style="color:#333333;">Daily Suggestions</h3>
                        <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                    <tr>
                        <th style="border: 2px solid #000; padding: 10px;"></th>
                        <th style="border: 2px solid #000; padding: 10px;">pH</th>
                        <th style="border: 2px solid #000; padding: 10px;">Ammonia</th>
                        <th style="border: 2px solid #000; padding: 10px;">DO</th>
                        <th style="border: 2px solid #000; padding: 10px;">Salinity</th>
                    <tr>
                    <td style='border: 2px solid #000; padding: 10px;'>BenchMark</td>
                    <td style='border: 2px solid #000; padding: 10px;'>7.5</td>
                    <td style='border: 2px solid #000; padding: 10px;'>0.2</td>
                    <td style='border: 2px solid #000; padding: 10px;'>7</td>
                    <td style='border: 2px solid #000; padding: 10px;'>33</td>
                    </tr>
                    <tr>
                    <td style='border: 2px solid #000; padding: 10px;'>Current</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{float(all_data['pH'][0])}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{float(all_data['Ammonia'][0])}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{float(all_data['DO'][0])}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{float(all_data['Salinity'][0])}</td>
                    </tr>
                    <tr><td style='border: 2px solid #000; padding: 10px;'>Intervention plan</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(7.5- float(all_data['pH'][0]),2)}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(0.2- float(all_data['Ammonia'][0]),2)}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(7- float(all_data['DO'][0]), 2)}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(33- float(all_data['Salinity'][0]),2)}</td>
                    </tr>
                    </table>
                    </div>
                """

        st.write("")
        st.markdown(html, unsafe_allow_html=True)
        st.write("")


        # Cards
        aquadataset = pd.read_csv('Dataset/Aqua/AquaSammury.csv')
        # title for the Traits
        st.markdown(textwithboarder('Real-time Traits', f"""View the latest data from Aqua Fish traits and explore the forecast for the upcoming traits. (latest data {aquadataset.iloc[len(aquadataset) - 1]['Date']})""" ))
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            cardCreator('LENGTH (cm)', aquadataset.iloc[len(aquadataset) - 1]['LENGTH (cm)'])
        with col2:
            cardCreator('WEIGHT (kg)', aquadataset.iloc[len(aquadataset) - 1]['WEIGHT (kg)'])
        with col3:
            cardCreator('Future LENGTH (cm)', 66 )
        with col4:
            cardCreator('Future WEIGHT (kg)', 2.10)
        st.write('')

        # Read Data from Aqua API
        fieldname = {'Field 1' : 'Temperature' ,'Field 2' : 'pH', 'Field 3' : 'Ammonia','Field 4' : 'DO', 'Field 5':'Salinity'}
        all_data = {fieldname[f'Field {i}']: get_field_data(i) for i in range(1, 6)}
        URL = f'https://api.thingspeak.com/channels/1649792/fields/1.json?api_key='
        KEY = 'YOUR_API_KEY'
        NEW_URL = URL + KEY

        # Check the Time
        get_data = requests.get(NEW_URL).json()
        field_data = get_data['feeds']
        html_content = f"""
                                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                            <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                            <p>Track real-time nutrient levels for Aqua. {field_data[len(field_data) - 1]['created_at']}</p>
                                                        </div>
                                                    """
        # Show the Guage of the Nutrients levels
        st.markdown(html_content , unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            guageCreator(float(all_data['pH'][0]), 'pH', 1, 14)
        with col2:
            guageCreator(float(all_data['Temperature'][0]), 'Temperature', 10, 55 )
        with col3:
            guageCreator(float(all_data['Ammonia'][0]), 'Ammonia', 0, 0.12)
        with col4:
            guageCreator(float(all_data['DO'][0]), 'DO', 0, 20)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            guageCreator(float(all_data['Salinity'][0]), 'Salinity', 0, 40)




    if option2 == "Pak choy":
        data = getPakChoyData('waterPh')

        import plotly.graph_objects as go

        fig_ph = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "pH"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterEc')
        fig_ec = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "EC"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSr')
        fig_sr = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Sr"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterOrp')
        fig_orp = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Orp"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTds')
        fig_tds = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "TDS"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSalinity')
        fig_Salinity = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Salinity"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTemperature')
        fig_Temperature = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Temperature"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))


        html_content = f"""
                                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                            <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                            <p>You can see the level of the nutrients at {data["data"][0]["readingAt"]}</p>
                                                        </div>
                                                    """
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.plotly_chart(fig_ph, use_container_width=True, height=500)
        with col2:
            st.plotly_chart(fig_ec, use_container_width=True, height=500)
        with col3:
            st.plotly_chart(fig_sr, use_container_width=True, height=500)
        with col4:
            st.plotly_chart(fig_orp, use_container_width=True, height=500)
        with col5:
            st.plotly_chart(fig_tds, use_container_width=True, height=500)
        with col6:
            st.plotly_chart(fig_Salinity, use_container_width=True, height=500)
        with col7:
            st.plotly_chart(fig_Temperature, use_container_width=True, height=500)

        options = st.selectbox(
            'Select the option',
            ('Temperature', 'pH', 'Sr', 'Orp', 'Tds', 'Salinity'))
        df = getPakChoyDatas(options)
        print(df)

    if option2 == 'Rice':
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        import time

        # Function to create an animated gauge-style progress bar using Plotly
        def animated_gauge_progress_bar(value, title):
            if 1 <= value <= 10:
                bar_color = "red"
            else:
                bar_color = "#4CAF50"  # Default color for other values

            fig = make_subplots(
                rows=1, cols=1,
                specs=[[{'type': 'indicator'}]]
            )

            fig.add_trace(go.Indicator(
                mode="number+gauge+delta",
                value=value,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': 50, 'position': 'top'},
                gauge=dict(
                    axis=dict(range=[0, 100]),
                    bar=dict(color=bar_color),  # Set color dynamically
                    bgcolor="white",
                    borderwidth=2,
                    bordercolor="gray",
                    steps=[dict(range=[0, 100], color="lightgray")]
                ),
                title=dict(text=title, font=dict(size=20)),  # Set title directly within the trace
            ))

            fig.update_layout(
                height=200,
                margin=dict(l=10, r=10, b=10, t=30),
            )

            return fig

        # Streamlit app
        st.title("Animated Gauge-style Progress Bar with Plotly")

        progress_value = st.slider("Select progress value", 0, 100, 50)
        title = "pH"

        chart_placeholder = st.empty()

        vla = 23
        # Update the progress value with an animation
        for value in range(0, vla, 1):
            time.sleep(0.06)
            animated_chart = animated_gauge_progress_bar(value, title)
            chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
            st.empty()  # Clear the previous chart to create animation effect




