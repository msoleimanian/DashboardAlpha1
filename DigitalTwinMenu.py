import streamlit as st
from streamlit_option_menu import option_menu
import DigitalTwin as digitaltwin
import Monitoring as monitoring
import Recommendation as recommendation

def constructoemain():

    selected = option_menu(None, ["Virtual model", "Monitoring", "Recommendation"],
        menu_icon="cast", default_index=0, orientation="horizontal")
    if selected == "Virtual model":
        digitaltwin.digitaltwinconstructor()


    if selected == "Monitoring":
        monitoring.MonitoringConstructor()

    if selected == "Recommendation":
        recommendation.RecommendationConstructor()

