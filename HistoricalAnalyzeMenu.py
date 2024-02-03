import streamlit as st
from streamlit_option_menu import option_menu
import Summary as summary
import Insights as insights
import Explore as explore

def constructoemain():
    selected = option_menu(None, ["Summary", "Insights", "Explore"],
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "Summary":
        summary.summaryConstructor()

    if selected == "Insights":
        insights.insightConstructor()

    if selected == "Explore":
        explore.exploreConstructor()