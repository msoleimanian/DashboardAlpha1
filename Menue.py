import streamlit as st
from streamlit_option_menu import option_menu
import HistoricalAnalyzeMenu as historical
import DigitalTwinMenu as digitialtwin
import Home as home

def menuconstructor():
    # 1. as sidebar menu
    st.set_page_config(layout="wide")
    with st.sidebar:
        select = option_menu("AgroPulse TwinHub", ["Home","Historical Analyze", 'Digital Twin'],
            icons=['bank','easel-fill', 'info-square-fill'], menu_icon="database-up")

    if select == "Historical Analyze":
        historical.constructoemain()

    if select == "Digital Twin":
        digitialtwin.constructoemain()

    if select == 'Home':
        home.homepageconstructor()


if __name__ == '__main__':
    menuconstructor()
