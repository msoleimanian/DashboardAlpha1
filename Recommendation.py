
def RecommendationConstructor():


    import streamlit as st
    import time
    import numpy as np
    import pandas as pd
    import time
    import plotly.express as px
    from streamlit_option_menu import option_menu




    def printCostumTitleAndContenth3(title, context):
        return f"""
            <div class="jumbotron">
            <h3>{title}</h3>
            <h6>{context}</h6>
            </div>
            <div class="container">
            </div>
            """

    def printCustomTitleAndContentrisk(title, context, color):
        return f"""
            <div class="jumbotron" ;background-color: "{color}";>
                <h3 color="{color};">{title}</h3>
                <h4>{context}</h4>
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


    def animated_linear_progress_bar(label, value, color='green'):
        progress_html = f"""
            <svg width="300" height="30" style="background-color: #f1f1f1; border-radius: 5px;">
                <rect id="progress-rect" width="0%" height="100%" fill="{color}">
                    <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
                </rect>
                <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
            </svg>
    
            <script>
                const progressRect = document.getElementById('progress-rect');
                progressRect.setAttribute('width', '{value}%');
            </script>
        """
        st.markdown(progress_html, unsafe_allow_html=True)

    # Example usage with animated linear progress bar

    def animated_circular_progress_bar(label, value, max_value, color='red', max_size=150):
        normalized_value = min(value / max_value, 1.0)  # Normalize value to be between 0 and 1
        progress_html = f"""
            <div id="progress-container" style="width: {max_size}px; height: {max_size}px; position: relative; border-radius: 50%; overflow: hidden;">
                <div id="progress-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
                <div id="animated-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: {color}; font-size: 11px; font-weight: bold;">{label}<br>{value} </div>
            </div>
    
            <script src="https://cdnjs.cloudflare.com/ajax/libs/progressbar.js/1.0.1/progressbar.min.js"></script>
            <script>
                const container = document.getElementById('progress-container');
                const bar = new ProgressBar.Circle(container, {{
                    strokeWidth: 13,
                    easing: 'easeInOut',
                    duration: 2000,
                    color: '{color}',
                    trailColor: '#e0e0e0',
                    trailWidth: 10,
                    svgStyle: null
                }});
    
                bar.animate({normalized_value});
            </script>
        """
        return progress_html

    def animated_linear_progress_bar_with_metric(metric_value, label, value, color='green', width=200, height=20):
        progress_html = f"""
            <div style="display: flex; align-items: center; text-align: left;">
                <div style="font-size: 14px; font-weight: bold; margin-right: 10px;">{metric_value}</div>
                <div style="position: relative; width: {width}px;">
                    <svg width="{width}" height="{height}" style="background-color: #f1f1f1; border-radius: 5px;">
                        <rect id="progress-rect" x="0" y="0" width="0%" height="100%" fill="{color}">
                            <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
                        </rect>
                        <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
                    </svg>
                </div>
            </div>
    
            <script>
                const progressRect = document.getElementById('progress-rect');
                progressRect.setAttribute('width', '{value}%');
            </script>
        """
        st.markdown(progress_html, unsafe_allow_html=True)

    # HTML and CSS for animated line
    animated_line_html = """
    <style>
        @keyframes drawLine {
            to {
                stroke-dashoffset: 0;
            }
        }
    
        .animated-line {
            width: 100%;
            height: 12px;
            background-color: black;
            position: relative;
            overflow: hidden;
        }
    
        .line-path {
            stroke-dasharray: 1000;
            stroke-dashoffset: 1000;
            animation: drawLine 2s forwards;
            stroke: #3498db;
            stroke-width: 2px;
        }
    </style>
    
    <div class="animated-line">
        <svg width="100%" height="100%">
            <line class="line-path" x1="0" y1="1" x2="100%" y2="1"/>
        </svg>
    </div>
    """

    # Display the animated line using HTML

    selectfarm = option_menu(None, ["Pak choy", "Rice", "Aqua"],
                          menu_icon="forward", default_index=0, orientation="horizontal",
                          styles={
                              "container": {"padding": "0!important", "background-color": "#fafafa"},
                              "icon": {"color": "orange", "font-size": "15px"},
                              "nav-link": {"font-size": "15px", "text-align": "right", "margin": "0px",
                                           "--hover-color": "#eee", },
                              "nav-link-selected": {"background-color": "green"},
                          }
                          )

    if selectfarm == "Rice":
        st.markdown(printCostumTitleAndContenth1("Nutrient recovery recommendation", ""), unsafe_allow_html=True)
        optionSeason = st.selectbox(
            "Select the Season...",
            ("1", "2"),
            index=0,
            placeholder="Select the farm...",
        )

        optionPlot = st.selectbox(
            "Select the Plot...",
            ("1", "3", "4", "5"),
            index=0,
            placeholder="Select the farm...",
        )

        optionDay = st.selectbox(
            "Select the Day...",
            ("30", "60"),
            index=0,
            placeholder="Select the farm...",
        )



        df = pd.read_csv('Dataset/Rice/N.csv')

        # Function to compare nutrient levels for two given seasons and plots
        def compare_nutrient_levels(season1, day1, plot1, season2, day2 , plot2):
            # Filter rows for the given season and plot
            benchmark = df[(df['Season'] == season1) & (df['Day'] == day1) & (df['Plot'] == plot1)]

            # Filter rows for the comparison season and plot
            selected = df[(df['Season'] == season2) & (df['Plot'] == plot2) & (df['Day'] == day2)]

            # Display the comparison
            if not benchmark.empty and not selected.empty:
                print("############")
                print(benchmark['N'].mean() - selected['N'].mean())
                comparison = pd.concat([benchmark, selected], keys=['Current', 'Comparison'])


                import random
                # seed random number generator
                # generate some integers
                values = random.randint(25,31)
                print(values)
                percentage = round(((((37 - values) / 37)) * 100),2)
                risk = ""
                color = ""
                if percentage<20:
                    risk = "No Risk"
                    color = "green"
                elif (percentage<=25):
                    risk = "Low Risk"
                    color = "orange"
                else:
                    risk = "High Risk"
                    color = "red"
                col1, col2 = st.columns(2)
                with col1:
                    html_content = f"""
                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                            <h3 style="color:#333333;">Yield Report</h3>
                                            <p style="color:{color};">Predicted Average Weight Grain for Season{optionSeason} at D90: {values} gram (% {percentage} lower than the best, Best weight grain is 37 gram.)</p>
                                        </div>
                                    """
                    st.markdown(html_content, unsafe_allow_html=True)

                with col2:
                    html_content = f"""
    <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                        <h3 style="color:#333333;">Yield Risk Predicted:</h3>
                        <p style="color:{color};">{risk}</p>
                    </div>
                """

                    st.markdown(html_content, unsafe_allow_html=True)
                return benchmark , selected
            else:
                print('No data found for the specified season and plot combination.')


        # Example: Compare nutrient levels for Season 1, Day 30, Plot 1 with Season 2, Plot 5
        benchmark, sel = compare_nutrient_levels(season2=int(optionSeason), day1=int(optionDay) , day2=int(optionDay), plot2=int(optionPlot), season1=2, plot1=5)
        html = f"""
        
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                    <h3 style="color:#333333;">Suggestions</h3>
                    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                <tr>
                    <th style="border: 2px solid #000; padding: 10px;"></th>
                    <th style="border: 2px solid #000; padding: 10px;">N</th>
                    <th style="border: 2px solid #000; padding: 10px;">K</th>
                    <th style="border: 2px solid #000; padding: 10px;">P</th>
                    <th style="border: 2px solid #000; padding: 10px;">Mg</th>
                    <th style="border: 2px solid #000; padding: 10px;">Ca</th>    
            <tr>
            <td style='border: 2px solid #000; padding: 10px;'>Best Performance(Season2 Plot2)</td>
            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['N'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['K'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['P'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Mg'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Ca'].mean().round(2)}</td>
            
            </tr>
            
            <tr>
            <td style='border: 2px solid #000; padding: 10px;'>Current Season{optionSeason} Plot{optionPlot}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{sel['N'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{sel['K'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{sel['P'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{sel['Mg'].mean().round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{sel['Ca'].mean().round(2)}</td>
            
            </tr>
            
            
            <tr><td style='border: 2px solid #000; padding: 10px;'>Intervention plan</td>
            <td style='border: 2px solid #000; padding: 10px;'>{(sel['N'].mean() - benchmark['N'].mean()).round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{(sel['K'].mean() - benchmark['K'].mean()).round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{(sel['P'].mean() - benchmark['P'].mean()).round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{(sel['Mg'].mean() - benchmark['Mg'].mean()).round(2)}</td>
            <td style='border: 2px solid #000; padding: 10px;'>{(sel['Ca'].mean() - benchmark['Ca'].mean()).round(2)}</td>
            </tr>
            </table>
            </div>
        """
        st.write("")
        st.markdown(html, unsafe_allow_html=True)

        html_content_with_border = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                <h3 style="color:#333333;">Yield Report</h3>
                <p style="color:green;">Predicted Average Weight Grain for Season{optionSeason} at D90: 33 gram after Aplly the Intervention plan (% 4 lower than the best, Best weight grain is 37 gram.)</p>
                <table style="border-collapse: collapse; width: 100%;">
                </div>
                <h3>Crop Traits</h3>
                <table style="border-collapse: collapse; width: 100%;">
    <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
        <th style="border: 1px solid #dddddd; padding: 8px;">Season</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Plot Number</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Plant Height</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">No. of Tiller</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">No. of Panicle</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">No. of Spikelet</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">No. of Filled Grain</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">No. Of Unfilled Grain</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Weight Grain (1000 grains)</th>
    </tr>
    <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
        <td style="border: 1px solid #dddddd; padding: 8px;">{optionSeason}</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">{optionPlot}</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">98.51</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">6</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">5</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">42</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">195</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">154</td>
        <td style="border: 1px solid #dddddd; padding: 8px;">33</td>
    </tr>
</table>
            </div>
        """
        st.write("")
        col1, col2, col3 = st.columns(3)
        if col2.button("Apply Intervention plan"):
            st.markdown(html_content_with_border, unsafe_allow_html=True)



    if selectfarm =="Aqua":
        st.header('')
        all_data = pd.read_csv('Dataset/Aqua/feed.csv')
        html = f"""

                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">Suggestions</h3>
                                <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                            <tr>
                                <th style="border: 2px solid #000; padding: 10px;"></th>
                                <th style="border: 2px solid #000; padding: 10px;">pH</th>
                                <th style="border: 2px solid #000; padding: 10px;">Ammonia</th>
                                <th style="border: 2px solid #000; padding: 10px;">DO</th>
                                <th style="border: 2px solid #000; padding: 10px;">Salinity</th>
                            <tr>
                            <td style='border: 2px solid #000; padding: 10px;'>Benchmark</td>
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
                            <td style='border: 2px solid #000; padding: 10px;'>{round(7.5 - float(all_data['pH'][0]), 2)}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{round(0.2 - float(all_data['Ammonia'][0]), 2)}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{round(7 - float(all_data['DO'][0]), 2)}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{round(33 - float(all_data['Salinity'][0]), 2)}</td>
                            </tr>
                            </table>
                            </div>
                        """

        st.write("")
        st.markdown(html, unsafe_allow_html=True)
        st.write("")
        col11, col22 = st.columns(2)
        with col11:
            html_content = f"""
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                    <h3 style="color:#333333;">Yield Report</h3>
                                                    <p style="color:green;">Predicted Average Weight for Fish: 2.4 gram (% 9 lower than the best, )</p>
                                                </div>
                                            """
            st.markdown(html_content, unsafe_allow_html=True)

        with col22:
            html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">Yield Risk Predicted:</h3>
                                <p style="color:green ;">No Risk</p>
                            </div>
                        """
            st.markdown(html_content, unsafe_allow_html=True)

        html_content_with_border = f"""
                            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">Yield Report</h3>
                                <p style="color:green;">Predicted Average Weight Fish is 2.4KG after Aplly the Intervention plan (% 4 lower than the best.)</p>
                                <table style="border-collapse: collapse; width: 100%;">
                                </div>
                                <h3>Crop Traits</h3>
                                <table style="border-collapse: collapse; width: 100%;">
            <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <th style="border: 1px solid #dddddd; padding: 8px;">Weight (KG)</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Length (CM)</th>
            </tr>
            <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <th style="border: 1px solid #dddddd; padding: 8px;">2.4</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">23</th>
            </tr>
                            </div>
                        """

        col1, col2, col3 = st.columns(3)


        if col2.button("Apply Intervention plan"):
            st.markdown(html_content_with_border, unsafe_allow_html=True)


    if selectfarm =="Pak choy":
        col1, col2, col3 = st.columns(3)
        with col1:
            pot = st.selectbox('Select the Pot', ('Pot 1', 'Pot 2'))
        generation = 'Generation 3'
        col11, col22 = st.columns(2)
        data = {'Generation 3':{'Pot 1': 670,  'Pot 2': 690}}
        percentage = round(((((1100 - data[generation][pot]) / 1100)) * 100), 2)
        risk = ""
        color = ""
        if percentage < 20:
            risk = "No Risk"
            color = "green"
        elif (percentage <= 25):
            risk = "Low Risk"
            color = "orange"
        else:
            risk = "High Risk"
            color = "red"

        with col11:
            html_content = f"""
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                    <h3 style="color:#333333;">Yield Report</h3>
                                                    <p style="color:{color};">Predicted Average Weight for Generation{generation} at Week4: {data[generation][pot]} gram (% {percentage} lower than the best, Best weight grain is 37 gram.)</p>
                                                </div>
                                            """
            st.markdown(html_content, unsafe_allow_html=True)

        with col22:
            html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">Yield Risk Predicted:</h3>
                                <p style="color:{color};">{risk}</p>
                            </div>
                        """
            st.markdown(html_content, unsafe_allow_html=True)

        benchmark = {'Temperature' : 24, 'Salinity' :5 , 'TDS':12 , 'Orp' :22 ,'Sr':7, 'EC' : 13, 'pH':6}
        dataset = {
            'Generation 3': {
                'Pot 1': {"Temperature": 25.5, "Salinity": 35, "TDS": 400, "Orp": 200, "Sr": 10, "pH": 7.2 , 'EC' : 13 },
                'Pot 2': {"Temperature": 24.8, "Salinity": 34, "TDS": 390, "Orp": 210, "Sr": 12, "pH": 7.5 , 'EC' : 13}
            },
            'Generation 4': {
                'Pot 1': {"Temperature": 26.2, "Salinity": 36, "TDS": 410, "Orp": 195, "Sr": 9, "pH": 7.0 , 'EC' : 13},
                'Pot 2': {"Temperature": 25.7, "Salinity": 35.5, "TDS": 405, "Orp": 205, "Sr": 11, "pH": 7.3 , 'EC' : 13}
            }
        }
        html = f"""

                    <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                            <h3 style="color:#333333;">Suggestions</h3>
                            <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                        <tr>
                            <th style="border: 2px solid #000; padding: 10px;"></th>
                            <th style="border: 2px solid #000; padding: 10px;">Temperature</th>
                            <th style="border: 2px solid #000; padding: 10px;">Salinity</th>
                            <th style="border: 2px solid #000; padding: 10px;">TDS</th>
                            <th style="border: 2px solid #000; padding: 10px;">Orp</th>
                            <th style="border: 2px solid #000; padding: 10px;">Sr</th>    
                            <th style="border: 2px solid #000; padding: 10px;">EC</th>    
                            <th style="border: 2px solid #000; padding: 10px;">pH</th>    
                    <tr>
                    <td style='border: 2px solid #000; padding: 10px;'>Benchmark</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Temperature']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Salinity']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['TDS']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Orp']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Sr']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['EC']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['pH']}</td>

                    </tr>

                    <tr>
                    <td style='border: 2px solid #000; padding: 10px;'>Current {generation} and {pot}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Temperature']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Salinity']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['TDS']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Orp']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Sr']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['EC']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['pH']}</td>

                    </tr>


                    <tr><td style='border: 2px solid #000; padding: 10px;'>Intervention plan</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(benchmark['Temperature'] - dataset[generation][pot]['Temperature'] , 2)}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Salinity'] - dataset[generation][pot]['Salinity']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['TDS'] - dataset[generation][pot]['TDS']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Orp'] - dataset[generation][pot]['Orp']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Sr'] - dataset[generation][pot]['Sr']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['EC'] - dataset[generation][pot]['EC']}</td>
                    <td style='border: 2px solid #000; padding: 10px;'>{round(benchmark['pH'] - dataset[generation][pot]['pH'],2)}</td>
                    </tr>
                    </table>
                    </div>
                """
        st.write("")
        st.markdown(html, unsafe_allow_html=True)
        st.write('')
        html_content_with_border = f"""
                    <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                        <h3 style="color:#333333;">Yield Report</h3>
                        <p style="color:green;">Predicted Average Weight Grain for {generation} at week 4: 1011 gram after Aplly the Intervention plan (% 4 lower than the best, Best weight grain is 1100 gram.)</p>
                        <table style="border-collapse: collapse; width: 100%;">
                        </div>
                        <h3>Crop Traits</h3>
                        <table style="border-collapse: collapse; width: 100%;">
    <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
        <th style="border: 1px solid #dddddd; padding: 8px;">Generation</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Pot number</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Plant Height(mm)</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Leaves Count(mm)</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Longest Leaf(mm)</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">Estimated Harvest Weight(gram)</th>
    </tr>
    <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
        <th style="border: 1px solid #dddddd; padding: 8px;">{generation}</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">{pot}</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">283</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">12</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">184</th>
        <th style="border: 1px solid #dddddd; padding: 8px;">1011</th>
    </tr>
                    </div>
                """
        col1, col2, col3 = st.columns(3)
        if col2.button("Apply Intervention plan"):
            st.markdown(html_content_with_border, unsafe_allow_html=True)