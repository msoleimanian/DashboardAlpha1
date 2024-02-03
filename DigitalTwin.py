import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd

def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printWithTitleAndBoarder(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h4 style="color:#333333;">{title}</h4>
            <table>
                    <tr>
                        <th>Status</th>
                        <th>Score(10)</th>
                        <th>Risk Level</th>
                    </tr>
                    <tr>
                        <td style="color : red;">good</td>
                        <td style="color : red;">4</td>
                        <td style="color : red;">High Risk</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Predicted Crop Health Status</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : red;">bad</td>
                    </tr>
            </table>
        </div>
        """

def printWithTitleAndBoarderwithoutTable(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h4 style="color:#333333;">{title}</h4>
            <table>
                    <tr>
                        <th>Status</th>
                        <th>Score(10)</th>
                    </tr>
                    <tr>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">5</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Plant Cycle</h4>
            <table>
                    <tr>
                        <th>Current Growth Time</th>
                        <th>Total Germination Time</th>
                    </tr>
                    <tr>
                        <td>2 week</td>
                        <td>4 week</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Current Crop Health Status</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : orange;">normal</td>
                    </tr>
            </table>
        </div>
        """

def printWithTitleAndBoarder1(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h3 style="color:#333333;">{title}</h3>
            <h5>{context}</h5>
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


def digitaltwinconstructor():

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

    if option2 == "Pak choy":






        import  pandas as pd
        df = pd.read_csv('Generation3_pot1.csv')
        col1 , col2 = st.columns(2)
        with col1:
            st.markdown(printWithTitleAndBoarderwithoutTable('Current Health Status Generation 3', 'Farm health Status: Good (7/10)', ) , unsafe_allow_html=True)
        with col2:
            st.markdown(printWithTitleAndBoarder('Predicted Health Status Generation 3 at week4', 'Farm health Status: Good - 7/10') , unsafe_allow_html=True)
        optionpot = st.selectbox('Select the pot:', (1, 2))
        # Your dataframe

        if optionpot == 1:
        # Replace 'Dataset/Pock choy /Generation3_pot1.csv' with the actual path to your CSV file
            file_path = 'Generation3_pot1.csv'

        if optionpot == 2 :
            file_path = 'Generation3_pot2.csv'
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Define a mapping for status to color
        status_color_mapping = {'good': 'green', 'normal': 'orange', 'bad': 'red'}

        # Create a dictionary with pot number as keys and color as values
        pot_color_dict = {}
        for index, row in df.iterrows():
            pot_number = row['subpotnumber']
            status = row['status'].lower()  # Convert to lowercase for case-insensitivity
            color = status_color_mapping.get(status,
                                             'unknown')  # Default to 'unknown' if status is not one of the specified values
            pot_color_dict[pot_number] = color

        print(pot_color_dict)


        dataframe = pot_color_dict
        # Streamlit app layout
        # Define CSS styles
        col1 , col2 = st.columns(2)
        with col1:

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
                        font-size: 10px;
                        font-weight: bold;
                        border: 2px solid #ddd;
                        border-radius: 55px;
                        cursor: pointer;
                    }
                </style>
            """
            # Display CSS styles
            st.markdown(css_styles, unsafe_allow_html=True)

            df = pd.read_csv('Generation3_pot1.csv')
            # Create button grid
            button_container = f"""<div style="border: 2px solid #333333; padding:10px; border-radius:5px;">     <p style='text-align: center'>Pot  {optionpot}</p>  <div class='button-container'>"""
            for key, value in dataframe.items():
                # Use Streamlit's button widget with a callback to display text on click
                button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}; color: white'
                                   onclick='st.write("{key} clicked!")'>{key}</button>"""
            button_container += "</div> </div>"

            # Display button grid
            st.markdown(button_container, unsafe_allow_html=True)

        with col2:
            df = pd.read_csv('Generation3_pot1.csv')
            subpot = st.selectbox('Select the SubPot Number', df['subpotnumber'].unique())
            filtered_df = df[df['subpotnumber'] == subpot]
            html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                <h2 style="color: {dataframe[subpot]}; ">Health Crop Status: {filtered_df['status'].values[0]}</h2>
                <h2>Current Crop Traits</h2>
                <table>
                    <tr>
                        <th>Leaf Count</th>
                        <th>Longest Leaf (mm)</th>
                        <th>Plant Height (mm)</th>
                    </tr>
                    <tr>
                        <td>{filtered_df['leafcount'].values[0]}</td>
                        <td>{filtered_df['longestleaf'].values[0]}</td>
                        <td>{filtered_df['plantheight'].values[0]}</td>
                    </tr>
                </table>
                <h2>Crop Traits at week4</h2>
                <table border='1'>
                    <tr>
                        <th>Leaf Count</th>
                        <th>Longest Leaf (mm)</th>
                        <th>Plant Height (mm)</th>
                    </tr>
                    <tr>
                        <td>{filtered_df['leafcount'].values[0] + 3 }</td>
                        <td>{filtered_df['longestleaf'].values[0]+ 22}</td>
                        <td>{filtered_df['plantheight'].values[0]+ 44}</td>
                    </tr>
                </table>
            </div>
            """
            st.markdown(html_content , unsafe_allow_html=True)

        def color_row(val):
            color = 'green' if val == df['plantheight'].max() else 'orange' if val > df['plantheight'].mean() else 'red'
            return f'background-color: {color}'
        st.write('')
        df = pd.read_csv('Generation3_pot1.csv')
        df1 = df.iloc[:20 , :]
        df2 = df.iloc[20: , :]

        # Load the CSV dat

        # Define a function to apply color based on plantheight


        # Apply the color function to the plantheight column

        # Display the styled dataframe
        with st.expander("More Information about Subplots"):
            # Put content inside the expander
            st.write("Here you can find additional information about each subplot.")
            col1, col2 = st.columns(2)
            with col1:
                df1 = df1.style.applymap(color_row, subset=['plantheight'])
                html_table = df1.to_html(index=False, classes='table-style', justify='center')

                # Display the HTML using st.markdown
                st.markdown(html_table, unsafe_allow_html=True)
            with col2:
                df2 = df2.style.applymap(color_row, subset=['plantheight'])
                html_table = df2.to_html(index=False, classes='table-style', justify='center')

                # Display the HTML using st.markdown
                st.markdown(html_table, unsafe_allow_html=True)

        st.write('')
        st.markdown(printWithTitleAndBoarder1('Simulation' , """Experiment with various nutrient levels and observe their impact on the week4 outcomes.""") , unsafe_allow_html=True)
        selectpot = st.selectbox('Select the pot:', ('Pot1', 'Pot2'))
        col1, col2 = st.columns(2)

        # Sliders in the first column
        temperature = col1.slider("Temperature (°C)", min_value=0, max_value=100, value=25, step=1)
        salinity = col1.slider("Salinity", min_value=0, max_value=50, value=25, step=1)
        tds = col1.slider("TDS (ppm)", min_value=0, max_value=1000, value=500, step=10)

        # Sliders in the second column
        orp = col2.slider("ORP (mV)", min_value=0, max_value=1000, value=500, step=10)
        sr = col2.slider("Sr", min_value=0, max_value=100, value=50, step=1)
        ec = col2.slider("EC (µS/cm)", min_value=0, max_value=100, value=50, step=1)
        ph = col2.slider("pH", min_value=0, max_value=14, value=7, step=1)


        col1 , col2 , col3 , col4, col5  = st.columns(5)
        import time
        col3.button('_______Apply_______')
        col1, col2 = st.columns(2)
        with col1:
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
                                font-size: 10px;
                                font-weight: bold;
                                border: 2px solid #ddd;
                                border-radius: 55px;
                                cursor: pointer;
                            }
                        </style>
                    """
            # Display CSS styles
            st.markdown(css_styles, unsafe_allow_html=True)

            df = pd.read_csv('Generation3_pot1.csv')
            # Create button grid
            button_container = f"""<div style="border: 2px solid #333333; padding:10px; border-radius:5px;">     <p style='text-align: center'>Pot  {optionpot}</p>  <div class='button-container'>"""
            for key, value in dataframe.items():
                # Use Streamlit's button widget with a callback to display text on click
                button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}; color: white'
                                           onclick='st.write("{key} clicked!")'>{key}</button>"""
            button_container += "</div> </div>"

            # Display button grid
            st.markdown(button_container, unsafe_allow_html=True)

        with col2:
            df = pd.read_csv('Generation3_pot1.csv')
            selectpot = st.selectbox('Select the SubPot Number', range(1, 41))
            subpot = f"SubPot{selectpot}"
            filtered_df = df[df['subpotnumber'] == subpot]
            html_content = f"""
                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                            <h2 style="color: {dataframe[subpot]}; ">Health Crop Status: {filtered_df['status'].values[0]}</h2>
                            <h2>Current Crop Traits</h2>
                            <table>
                                <tr>
                                    <th>Leaf Count</th>
                                    <th>Longest Leaf (mm)</th>
                                    <th>Plant Height (mm)</th>
                                </tr>
                                <tr>
                                    <td>{filtered_df['leafcount'].values[0]}</td>
                                    <td>{filtered_df['longestleaf'].values[0]}</td>
                                    <td>{filtered_df['plantheight'].values[0]}</td>
                                </tr>
                            </table>
                            <h2>Crop Traits at week4</h2>
                            <table border='1'>
                                <tr>
                                    <th>Leaf Count</th>
                                    <th>Longest Leaf (mm)</th>
                                    <th>Plant Height (mm)</th>
                                </tr>
                                <tr>
                                    <td>{filtered_df['leafcount'].values[0] + 3}</td>
                                    <td>{filtered_df['longestleaf'].values[0] + 22}</td>
                                    <td>{filtered_df['plantheight'].values[0] + 44}</td>
                                </tr>
                            </table>
                        </div>
                        """
            st.markdown(html_content, unsafe_allow_html=True)










