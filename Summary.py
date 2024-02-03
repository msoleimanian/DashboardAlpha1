

def summaryConstructor():

    import streamlit as st
    import time
    import numpy as np
    import pandas as pd
    import time
    import Menue as m
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

    def printCostumTitleAndContenth2(title, context):
        return f"""
            <div class="jumbotron">
            <h2>{title}</h2>
            <h6>{context}</h6>
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


    # Function to scale the numbers in a column to a 0-10 range
    def scale_numbers(column_values):
        max_value = max(column_values)
        return [round((value / max_value) * 10, 2) for value in column_values]


    # Function to get color based on percentage difference from the best
    def get_color(percent_difference):
        if percent_difference == 0:
            return 'green'  # Light Red
        elif 0 < percent_difference <= 1.5:
            return '#b3ffb3'
        elif 1.5 < percent_difference <= 3:
            return 'orange'
        elif 3 < percent_difference <= 3.5:
            return '#ff6666'


    # Data
    seasons = ['Season 1', 'Season 2', 'Season 3']
    plot_numbers = {'Season 1': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                    'Season 2': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                    'Season 3': ['Plot1', 'Plot3', 'Plot4', 'Plot5']}

    columns = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'No. of Spikelet',
               'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

    column_score = ['Weight Grain (1000 grains)']
    AVGWeightGrain = [26.27,
                      24.26,
                      25.95,
                      23.25,
                      33.31,
                      31.01,
                      30.55,
                      33.46,
                      33.19,
                      31.43,
                      26.20,
                      24.23]

    # Create an empty list to store data
    data_rows = []

    # Populate the data list for data entry
    count = 0
    for season in seasons:
        for plot in plot_numbers[season]:
            row = {'Season': season, 'Plot Number': plot, 'AVG Weight Grain': AVGWeightGrain[count]}
            count = count + 1
            for col in column_score:
                row[col] = None  # Initialize with None for data entry
            data_rows.append(row)
    print(data_rows)
    # Create DataFrame for data entry
    data_entry = pd.DataFrame(data_rows)

    # Provide a 2D array to fill in the numbers
    numbers_to_fill = [
        [98.51, 6, 5, 42, 195, 154, 26.27],
        [98, 5, 5, 35, 122, 155, 24.26],
        [93.20, 5, 4, 27, 137, 46, 25.95],
        [93.99, 7, 5, 35, 150, 163, 23.25],

        [103.16, 5, 5, 38, 188, 271, 33.31],
        [98.75, 5, 5, 38, 803, 250, 31.01],
        [88.80, 4, 4, 30, 643, 343, 30.55],
        [92.07, 5, 5, 37, 662, 290, 33.46],

        [100.16, 5, 5, 41, 84, 16, 33.19],
        [96.95, 5, 4, 41, 84, 16, 31.43],
        [88.17, 3, 4, 30, 86, 14, 26.20],
        [93.98, 4, 4, 37, 82, 5, 24.23],
    ]

    # Fill up the DataFrame with the provided numbers
    for col_index, col_values in enumerate(zip(*numbers_to_fill)):
        for row_index, value in enumerate(col_values):
            data_entry.at[row_index, columns[col_index]] = value

    # Scale the numbers and sum each row
    scaled_data = data_entry.copy()
    print("#####123")
    print(scaled_data)
    for col in columns:
        scaled_values = scale_numbers(data_entry[col])
        scaled_data[col] = scaled_values

    scaled_data['Total Score'] = scaled_data[column_score].sum(axis=1)

    # Find the best and worst total scores
    max_total_score = scaled_data['Total Score'].max()
    min_total_score = scaled_data['Total Score'].min()

    # HTML styling with inline styles for black text color, thicker black border lines, and increased width
    html_code = f"""
    
        <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
    
        <h5> </h5>
        <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
            <tr>
                <th style="border: 2px solid #000; padding: 10px;">Season</th>
                <th style="border: 2px solid #000; padding: 10px;">Plot Number</th>
                <th style="border: 2px solid #000; padding: 10px;">Score</th>
                <th style="border: 2px solid #000; padding: 10px;">AVG Weight Grain</th>
            </tr>
            {"".join(
        f"<tr><td style='border: 2px solid #000; padding: 10px;'>{row['Season']}</td>"
        f"<td style='border: 2px solid #000; padding: 10px;'>{row['Plot Number']}</td>"
        f"<td style='border: 2px solid #000; padding: 10px; "
        f"background-color: {get_color((10 - row['Total Score']))};'>"
        f"{row['Total Score']}</td>"
        f"<td style='border: 2px solid #000; padding: 10px;'>{row['AVG Weight Grain']}</td></tr>"
    
        for _, row in scaled_data.iterrows()
    )}
        </table>
        </div>
    """

    # Display the HTML content




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


    # Continue with other code after the progress animation
    farmsdfst = pd.read_csv ('Dataset/FarmsStatus.csv')

    st.write("")
    st.write("")
    st.write("")


    if option2 == 'Rice':
        st.markdown(html_code, unsafe_allow_html=True)
        st.markdown(animated_line_html, unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth2("Best Performance",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Season2",""),unsafe_allow_html=True)


        col11 , col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 33  # Maximum weight in KG
            current_weight = 32.08  # Current weight in KG
            progress_html = animated_circular_progress_bar('AVG Weight Grain(1000 grains)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            col1, col2,col3 = st.columns(3)
            with col1:
                max_weight = 7  # Maximum weight in KG
                current_weight = 5  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Tiller', current_weight, max_weight, color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 5  # Maximum weight in KG
                current_weight = 4  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Panicle', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col3:
                max_weight = 42  # Maximum weight in KG
                current_weight = 36  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Spikelet', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)
            col4, col5, col6 = st.columns(3)
            with col4:
                max_weight = 803  # Maximum weight in KG
                current_weight = 574  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Filled Grain', current_weight, max_weight, color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col5:
                max_weight = 343  # Maximum weight in KG
                current_weight = 288  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. Of Unfilled Grain', current_weight, max_weight,
                                                               color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)


        st.markdown(printCostumTitleAndContenth3("Plot5 in Season2",
                                                 ""),
                    unsafe_allow_html=True)

        col11 , col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 33.46  # Maximum weight in KG
            current_weight = 33.46  # Current weight in KG
            progress_html = animated_circular_progress_bar('AVG Weight Grain(1000 grains)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Trait Value")
            col1, col2,col3 = st.columns(3)
            with col1:
                max_weight = 7  # Maximum weight in KG
                current_weight = 5  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Tiller', current_weight, max_weight, color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 5  # Maximum weight in KG
                current_weight = 5  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Panicle', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col3:
                max_weight = 42  # Maximum weight in KG
                current_weight = 37  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Spikelet', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)
            col4, col5, col6 = st.columns(3)
            with col4:
                max_weight = 803  # Maximum weight in KG
                current_weight = 662  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Filled Grain', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col5:
                max_weight = 343  # Maximum weight in KG
                current_weight = 290  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. Of Unfilled Grain', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

        st.write("")
        st.write("")






        st.markdown(animated_line_html, unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth2("Worst Performance",
                                                 ""),
                    unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth3("Season1",
                                                 ""),
                    unsafe_allow_html=True)


        col11 , col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 33  # Maximum weight in KG
            current_weight = 24.99  # Current weight in KG
            progress_html = animated_circular_progress_bar('AVG Weight Grain(1000 grains)', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Trait Value")
            col1, col2,col3 = st.columns(3)
            with col1:
                max_weight = 7  # Maximum weight in KG
                current_weight = 6  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Tiller', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 5  # Maximum weight in KG
                current_weight = 4  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Panicle', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col3:
                max_weight = 42  # Maximum weight in KG
                current_weight = 34  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Spikelet', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)
            col4, col5, col6 = st.columns(3)
            with col4:
                max_weight = 803  # Maximum weight in KG
                current_weight = 151  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Filled Grain', current_weight, max_weight, color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col5:
                max_weight = 343  # Maximum weight in KG
                current_weight = 130  # Current weight in KG
                progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                               color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)


        st.markdown(printCostumTitleAndContenth3("Plot5 in Season1",
                                                 ""),
                    unsafe_allow_html=True)

        col11 , col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 33.46  # Maximum weight in KG
            current_weight = 23.25  # Current weight in KG
            progress_html = animated_circular_progress_bar('AVG Weight Grain(1000 grains)', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("High Value Trait")
            col1, col2,col3 = st.columns(3)
            with col1:
                max_weight = 7  # Maximum weight in KG
                current_weight = 7  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Tiller', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 5  # Maximum weight in KG
                current_weight = 4  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Panicle', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col3:
                max_weight = 42  # Maximum weight in KG
                current_weight = 35  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Spikelet', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)
            col4, col5,col6 = st.columns(3)
            with col4:
                max_weight = 803  # Maximum weight in KG
                current_weight = 150  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Filled Grain', current_weight, max_weight, color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col5:
                max_weight = 343  # Maximum weight in KG
                current_weight = 163  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. Of Unfilled Grain', current_weight, max_weight,
                                                               color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

        df = pd.read_csv(f'Dataset/Rice/Season3.csv')
        st.markdown(animated_line_html, unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth2("Other Seasons",
                                                 ""),
                    unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth3("Season3",
                                                 ""),
                    unsafe_allow_html=True)


        col11 , col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 33  # Maximum weight in KG
            current_weight = df['Weight Grain (1000 grains)'].mean()  # Current weight in KG
            progress_html = animated_circular_progress_bar('AVG Weight Grain(1000 grains)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Trait Value")
            col1, col2,col3 = st.columns(3)
            with col1:
                max_weight = 7  # Maximum weight in KG
                current_weight = df['No. of Tiller'].mean()  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Tiller', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 5  # Maximum weight in KG
                current_weight = df['No. of Panicle'].mean()  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Panicle', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col3:
                max_weight = 42  # Maximum weight in KG
                current_weight = df['No. of Spikelet'].mean()  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Spikelet', current_weight, max_weight, color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)
            col4, col5, col6 = st.columns(3)
            with col4:
                max_weight = 803  # Maximum weight in KG
                current_weight = df['No. of Filled Grain'].mean()  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. of Filled Grain', current_weight, max_weight, color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col5:
                max_weight = 343  # Maximum weight in KG
                current_weight = df['No. Of Unfilled Grain'].mean()  # Current weight in KG
                progress_html = animated_circular_progress_bar('AVG No. Of Unfilled Grain', current_weight, max_weight,
                                                               color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)





    if option2 == 'Pak choy':
        # Create DataFrame
        df = pd.read_csv('Dataset/Pock choy /generation.csv')
        # Filter columns
        filtered_df = df[['generation', 'pot', 'leavescount', 'longestleaf', 'plantheight']]

        # Group by pot and subpot, calculate averages
        grouped_df = filtered_df.groupby(['generation', 'pot']).mean().reset_index()

        # Scale the values based on the height (score)
        max_score = 10
        height_scaling = max_score / grouped_df['plantheight'].max()
        grouped_df['score'] = grouped_df['plantheight'] * height_scaling

        # HTML code
        html_code_packchoy = f"""
            <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
                <h5> </h5>
                <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                    <tr>
                        <th style="border: 2px solid #000; padding: 10px;">Generation</th>
                        <th style="border: 2px solid #000; padding: 10px;">Pot Number</th>
                        <th style="border: 2px solid #000; padding: 10px;">Score</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG Plant Height</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG Longest leaf</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG leaves count</th>
                    </tr>
                    {''.join([f'<tr><td style="border: 2px solid #000; padding: 10px;">{row["generation"]}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px;">{row["pot"]}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px; background-color: {get_color(10 -min(row["score"], max_score))}">{min(row["score"], max_score):.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px;">{row["plantheight"]:.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px;">{row["longestleaf"]:.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px;">{row["leavescount"]:.2f}</td></tr>'
                              for index, row in grouped_df.iterrows()])}
                </table>
            </div>
        """

        # Streamlit app
        st.markdown(html_code_packchoy, unsafe_allow_html=True)
        st.write("")
        st.markdown(animated_line_html, unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth2("Best Performance",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Generation1", ""), unsafe_allow_html=True)

        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 214.25  # Maximum weight in KG
            current_weight = 128  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plant Height', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            col1, col2, col3 = st.columns(3)
            with col1:
                max_weight = 106.75  # Maximum weight in KG
                current_weight = 70  # Current weight in KG
                progress_html = animated_circular_progress_bar('Longest Leaf', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 9.70  # Maximum weight in KG
                current_weight = 7  # Current weight in KG
                progress_html = animated_circular_progress_bar('Leaf cout ', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)


        st.markdown(printCostumTitleAndContenth3("Pot1", ""), unsafe_allow_html=True)

        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 214.25  # Maximum weight in KG
            current_weight =  214.25  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plant Height', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            col1, col2, col3 = st.columns(3)
            with col1:
                max_weight = 106.75  # Maximum weight in KG
                current_weight = 106.75  # Current weight in KG
                progress_html = animated_circular_progress_bar('Longest Leaf', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 9.70  # Maximum weight in KG
                current_weight = 9.70  # Current weight in KG
                progress_html = animated_circular_progress_bar('Leaf cout ', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

        st.write("")
        st.write("")




        st.write("")
        st.markdown(animated_line_html, unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth2("Worst Performance",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Generation2", ""), unsafe_allow_html=True)

        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 214.25  # Maximum weight in KG
            current_weight = 82  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plant Height', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            col1, col2, col3 = st.columns(3)
            with col1:
                max_weight = 106.75  # Maximum weight in KG
                current_weight = 130  # Current weight in KG
                progress_html = animated_circular_progress_bar('Longest Leaf', current_weight, max_weight,
                                                               color='green',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 9.70  # Maximum weight in KG
                current_weight = 4  # Current weight in KG
                progress_html = animated_circular_progress_bar('Leaf cout ', current_weight, max_weight,
                                                               color='orange',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)


        st.markdown(printCostumTitleAndContenth3("Pot2", ""), unsafe_allow_html=True)

        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 214.25  # Maximum weight in KG
            current_weight =  1.88  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plant Height', current_weight, max_weight,
                                                           color='red',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            col1, col2, col3 = st.columns(3)
            with col1:
                max_weight = 106.75  # Maximum weight in KG
                current_weight = 3.75  # Current weight in KG
                progress_html = animated_circular_progress_bar('Longest Leaf', current_weight, max_weight,
                                                               color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

            with col2:
                max_weight = 9.70  # Maximum weight in KG
                current_weight = 0.62  # Current weight in KG
                progress_html = animated_circular_progress_bar('Leaf cout ', current_weight, max_weight,
                                                               color='red',
                                                               max_size=95)
                st.components.v1.html(progress_html, height=105)

        st.write("")
        st.write("")


    if option2 == "Aqua":
        data = {
            'DATE': ['4-Jul-23', '11-Jul-23', '18-Jul-23', '25-Jul-23', '1-Aug-23', '8-Aug-23', '15-Aug-23', '22-Aug-23',
                     '29-Aug-23', '5-Sep-23', '12-Sep-23', '19-Sep-23', '26-Sep-23'],
            'GAP OF DAYS': [7] * 13,
            'LENGTH (cm)': [55.6, 55.8, 56, 56.2, 56.5, 56.6, 56.7, 56.8, 57, 57.2, 57.4, 57.5, 57.8],
            'WEIGHT (kg)': [2.04, 1.76, 1.7, 1.64, 1.96, 1.98, 1.37, 1.82, 1.9, 2, 2.01, 1.9, 1.93],
            'GROWTH RATE LENGTH': ['0%', '0.36%', '0.36%', '0.36%', '0.54%', '0.18%', '0.18%', '0.18%', '0.35%', '0.35%',
                                   '0.35%', '0.17%', '0.52%'],
            'GROWTH RATE WEIGHT': ['0%', '-13.73%', '-16.67%', '-20.10%', '-4.90%', '-3.92%', '-32.84%', '-10.78%',
                                   '-7.84%', '-2.00%', '-1.49%', '-6.86%', '-5.88%']
        }

        df = pd.DataFrame(data)

        # Convert DATE column to datetime
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%y')

        # Convert percentage columns to numeric values
        df['GROWTH RATE LENGTH'] = pd.to_numeric(df['GROWTH RATE LENGTH'].str.rstrip('%'), errors='coerce') / 100
        df['GROWTH RATE WEIGHT'] = pd.to_numeric(df['GROWTH RATE WEIGHT'].str.rstrip('%'), errors='coerce') / 100

        # Add a new column for month-year in 'YYYY-MM' format
        df['Month-Year'] = df['DATE'].dt.to_period('M').dt.strftime('%Y-%m')

        # Group by month-year and calculate averages
        avg_df = df.groupby('Month-Year').agg({
            'LENGTH (cm)': 'mean',
            'WEIGHT (kg)': 'mean',
            'GROWTH RATE LENGTH': 'mean',
            'GROWTH RATE WEIGHT': 'mean'
        }).reset_index()

        # Assign scores based on average 'LENGTH (cm)'
        avg_df['Score'] = (avg_df['WEIGHT (kg)'] / avg_df['WEIGHT (kg)'].max()) * 10
    #################################
        # Sample data
        data = {
            'Month-Year': ['2023-07', '2023-08', '2023-09'],
            'LENGTH (cm)': [55.9000, 56.7200, 57.4750],
            'Score': [7.5, 9.5, 10.0]  # Example scores
        }

        df = avg_df

        # HTML code for the styled table without external CSS
        table_html = f""" 
            <table style="font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;">
                <tr style="background-color: #f2f2f2;">
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">Month-Year</th>
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">LENGTH (cm)</th>
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">WEIGHT (kg)</th>
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">Score</th>
                </tr>
        """

        # Adding rows dynamically based on DataFrame values
        for index, row in df.iterrows():
            row_html = f"<tr style='background-color: {get_color(10-row['Score'])}'>"
            row_html += f"<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>{row['Month-Year']}</td>"
            row_html += f"<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>{round(row['LENGTH (cm)'],2)}</td>"
            row_html += f"<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>{round(row['WEIGHT (kg)'],2)}</td>"
            row_html += f"<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>{round(row['Score'],2)}</td>"
            row_html += "</tr>"

            table_html += row_html

        # Closing the HTML table tag
        table_html += "</table>"

        # Display the HTML table
        st.markdown(table_html, unsafe_allow_html=True)

        ##################################
        df = pd.read_csv('Dataset/Aqua/feed.csv')
        dataframe = df['Temperature'].mean()

        # Streamlit app
        st.write("")
        st.markdown(animated_line_html, unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth2("Best Performance",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Generation Date: 2023-09", ""), unsafe_allow_html=True)
        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 1.96  # Maximum weight in KG
            current_weight = 1.96  # Current weight in KG
            progress_html = animated_circular_progress_bar('WEIGHT (kg)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            with col22:
                max_weight = 57.48	  # Maximum weight in KG
                current_weight = 57.48	 # Current weight in KG
                progress_html = animated_circular_progress_bar('LENGTH (kg)', current_weight, max_weight,
                                                               color='green',
                                                               max_size=200)
                st.components.v1.html(progress_html, height=210)




        st.write("")
        st.markdown(animated_line_html, unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth2("Worst Performance",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Generation Date: 2023-07", ""), unsafe_allow_html=True)
        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 1.96  # Maximum weight in KG
            current_weight = 1.78  # Current weight in KG
            progress_html = animated_circular_progress_bar('WEIGHT (kg)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            with col22:
                max_weight = 57.48  # Maximum weight in KG
                current_weight = 56.72  # Current weight in KG
                progress_html = animated_circular_progress_bar('LENGTH (kg)', current_weight, max_weight,
                                                               color='green',
                                                               max_size=200)
                st.components.v1.html(progress_html, height=210)



        st.write("")
        st.markdown(animated_line_html, unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth2("Others",
                                                 ""),
                    unsafe_allow_html=True)

        st.markdown(printCostumTitleAndContenth3("Generation Date: 2023-08", ""), unsafe_allow_html=True)
        col11, col22 = st.columns(2)
        with col11:
            st.write("High Value Trait")
            max_weight = 1.96  # Maximum weight in KG
            current_weight = 1.78  # Current weight in KG
            progress_html = animated_circular_progress_bar('WEIGHT (kg)', current_weight, max_weight,
                                                           color='green',
                                                           max_size=200)
            st.components.v1.html(progress_html, height=210)
        with col22:
            st.write("Other Traits Value")
            with col22:
                max_weight = 57.48  # Maximum weight in KG
                current_weight = 56.72  # Current weight in KG
                progress_html = animated_circular_progress_bar('LENGTH (kg)', current_weight, max_weight,
                                                               color='green',
                                                               max_size=200)
                st.components.v1.html(progress_html, height=210)


