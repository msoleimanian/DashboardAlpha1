import streamlit as st

# Your dataframe
dataframe = {'Po1': 'red', 'Pot2': 'blue', 'Pot3': 'green', 'Pot4': 'yellow', 'Pot5': 'orange',
             'Pot6': 'purple', 'Pot7': 'cyan', 'Pot8': 'pink', 'Pot9': 'brown', 'Pot10': 'gray',
             'Pot11': 'magenta', 'Pot12': 'teal', 'Pot13': 'olive', 'Pot14': 'navy', 'Pot15': 'lime',
             'Pot16': 'maroon', 'Pot17': 'aqua', 'Pot18': 'fuchsia', 'Pot19': 'silver', 'Pot20': 'black',
             'Pot21': 'red', 'Pot22': 'blue', 'Pot23': 'green', 'Pot24': 'yellow', 'Pot25': 'orange',
             'Pot26': 'purple', 'Pot27': 'cyan', 'Pot28': 'pink', 'Pot29': 'brown', 'Pot30': 'gray',
             'Pot31': 'magenta', 'Pot32': 'teal', 'Pot33': 'olive', 'Pot34': 'navy', 'Pot35': 'lime',
             'Pot36': 'maroon', 'Pot37': 'aqua', 'Pot38': 'fuchsia', 'Pot39': 'silver', 'Pot40': 'black'}

# Streamlit app layout
st.title('Button Grid with Streamlit')

# Define CSS styles
css_styles = """
    <style>
        .button-container {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 10px;
            border: 2px solid #ddd; /* Border around the button container */
            padding: 10px; /* Add some padding for better appearance */
        }
        .button {
            width: 100%;
            height: 70px;
            background-color: #eee;
            color: #333;
            font-size: 16px;
            font-weight: bold;
            border: 2px solid #ddd;
            border-radius: 55px;
            cursor: pointer;
        }
    </style>
"""

# Display CSS styles
st.markdown(css_styles, unsafe_allow_html=True)

# Create button grid
button_container = "<div class='button-container'>"
for key, value in dataframe.items():
    # Use Streamlit's button widget with a callback to display text on click
    button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}'
                       onclick='st.write(\"{key} clicked!\")'>{key}</button>"""
button_container += "</div>"

# Display button grid
st.markdown(button_container, unsafe_allow_html=True)
# _____-------_______-------_______-------______-------_______---



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

cardCreator('mohse' , 123 )