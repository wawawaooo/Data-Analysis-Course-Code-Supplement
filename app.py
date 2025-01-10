from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import style

# Load the cleaned data
wrangling_df = pd.read_csv("wrangling_df.csv")
wrangling_df["date"] = pd.to_datetime(wrangling_df["date"], errors="coerce")

# Initialize the Dash application
app = Dash(__name__)

# Define the application layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Introduction", children=[
            html.Div([
                html.H2("Introduction", style=style.style_h2_center),
                html.Img(
                    src="https://www.reuters.com/resizer/yq0ENP6iGU2VM8nO6j0279d1q-o=/1080x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/PVNYAVZBTBJUDF4GGQILRZVV5I.jpg",
                    style=style.style_center_img
                ),
                html.P(
                    "    This is our analysis of national COVID-19 vaccination trends in the United States. In this project, we delve into the vaccination progress and explore key insights regarding the administration of COVID-19 vaccines during the period from 2021 to 2022."
                ),
                html.P(
                    "    Over the past four years, billions of people worldwide have been affected by the unique global catastrophe known as the COVID-19 pandemic, which has had a major impact on the world. Vaccination has played a key role in mitigating its impact. Our analysis focuses on tracking the proportion of people who complete the full three-dose vaccination (3-dose) regimen and the proportion of people who receive a booster shot. We hope to use the dataset and information to assess and illustrate vaccination patterns in the U.S. and the resulting impact, while responding to public attitudes and trust in vaccination."
                ),
                html.P(
                    "    Through interactive visualizations and insightful data exploration, we aim to provide a comprehensive understanding of vaccination in the United States. By examining data across age groups, we can identify patterns and trends that illuminate the effectiveness and adoption of the COVID-19 vaccine. We believe that understanding the progress and patterns of COVID-19 vaccination is critical for policymakers, healthcare professionals, and the general public. By analyzing the data, we can gain insight into the effectiveness of vaccination campaigns, identify potential areas for improvement, and assess the public health impact of vaccination efforts."
                ),
                html.H2("Research Questions", style=style.style_h2_center),
                html.Ul([
                    html.Li("We first integrated our data sources, with a dataset containing different age groups of the population and their vaccination completion data, and we grouped all data by age. We focused on comparing the proportion of people who completed the entire vaccination series (three doses) in each age group. Age groupings: <2, 2-4, 5-11, 12-17, 18-24, 25-49, 50-64, 65+"),
                    html.Li("Secondly, we wanted to analyze the relationship between average vaccination rates and age groups. With this data, we wanted to find out which age group responded most positively to the vaccine."),
                    html.Li("Finally, we wanted to analyze the relationship between Administered Daily and Series Complete Daily. This data will tell us whether the number of people completing the vaccination series changes as the daily dose of COVID-19 vaccine is administered increases. This trend emphasizes the importance and public acceptance of the vaccine."),
                    html.P("We believe that these questions can show the relationship about the covid vaccination status and age group. Exactly which group responds most positively to the vaccine and which group needs the most protection from the vaccine. Also, it will reflect the demand and acceptance of the vaccine in the whole society.")
                ])
            ])
        ]),
        dcc.Tab(label="Series Complete Vaccination by Age Group", children=[
            html.Div([
                # Left and right layout:
                html.Div([
                    # Left side: chart and drop-down menu
                    html.Div([
                        html.H2("Vaccination Series Completion Analysis", style=style.style_h2_bold_28px),
                        dcc.Graph(id="plot1", style=style.style_graph_wh400),
                        html.Div([
                            # "Select Month for Plot 1" 
                            html.Div([
                                html.Label("Select Month for Plot 1:", style=style.style_fontsize_18),
                                html.Div([
                                    dcc.Dropdown(
                                        id="dropdown-month1",
                                        options=[{"label": month, "value": i + 1} for i, month in enumerate(
                                            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])],
                                        placeholder="Select Month",
                                        style=style.style_dropdown_width_60
                                    ),
                                    html.Div(
                                        "choose the Month/Year as you need, expect November and December 2022",
                                        style=style.style_dropdown_remark
                                    )
                                ], style=style.style_dropdown_flex_center)
                            ], style=style.style_margin_bottom_20),

                            # "Select Year for Plot 1" 
                            html.Div([
                                html.Label("Select Year for Plot 1:", style=style.style_fontsize_18_margintop10),
                                dcc.Dropdown(
                                    id="dropdown-year1",
                                    options=[{"label": str(year), "value": year} for year in [2021, 2022]],
                                    placeholder="Select Year"
                                )
                            ])
                        ], style=style.style_margin_top_20),

                        html.Div(
                            "Analysis based on desired month as you want(no data in NOV and DEC 2022)",
                            style=style.style_bold_18px_margintop20
                        ),
                    ], style=style.style_leftdiv_border),

                    # Text content
                    html.Div([
                        html.H3("Findings and Analysis", style=style.style_h3_bold_24_center),
                        html.Div([
                            html.H4("Investigation", style=style.style_h4_bold_22),
                            html.P(
                                "We first integrated our data sources, with a dataset containing different age groups of the population and their vaccination completion data, and we grouped all data by age "
                                "We focused on comparing the proportion of people who completed the entire vaccination series (three doses) in each age group. Age groupings: <2, 2-4, 5-11, 12-17, 18-24, 25-49, 50-64, 65+",
                                style=style.style_fontsize_20
                            ),
                            html.P(
                                "According to the chart we have drawn, the horizontal axis indicates the different age groups, and the vertical axis indicates the percentage of vaccination completion. "
                                "We can see that the highest vaccination completions are found among those over 65 years old, with over 80%. In contrast, the younger age groups have a relatively low vaccination completion rate."
                                "Also, the trend in Figure 2 clearly shows a positive correlation",
                                style=style.style_fontsize_20
                            ),
                            html.H4("Key Findings", style=style.style_h4_bold_22),
                            html.Ul([
                                html.Li("We believe that vaccination completion is generally highest among those over 65 years of age. This may be due to the higher awareness of the importance of health protection and the higher need for it among older adults."
                                        "Older adults tend to be more susceptible to serious diseases and are therefore more willing to get vaccinated to protect their health.", style=style.style_fontsize_18_li),
                                html.Li("Furthermore, vaccination completion rates increase with age. This may be due to the fact that older populations are more concerned about health issues and are more focused on preventive measures."
                                        "In addition, they may be more receptive to vaccination advice and access to vaccination services.", style=style.style_fontsize_18_li),
                                html.Li("However, we also noticed a relatively low level of vaccination completion among younger age groups. This may be related to their attitudes toward vaccines, access to vaccination information, and the availability of vaccination services."
                                        "The generally unstable lifestyle and social activities of young people and the fact that they do not care as much about vaccination may make access to vaccination services more difficult.", style=style.style_fontsize_18_li),
                            ]),
                            html.H4("Conclusion", style=style.style_h4_bold_22),
                            html.P(
                                "The results of these analyses allow us to recognize that when promoting vaccination, we should focus on younger age groups to increase their awareness and vaccination rates. I believe that in order to respond to societal attitudes toward vaccination, "
                                "relevant authorities should adopt different communication and education strategies, provide reliable and accurate vaccination information, and offer convenient and accessible vaccination services as a way to more comprehensively increase vaccination completion throughout society, "
                                "thereby effectively controlling the spread of epidemics and protecting public health.",
                                style=style.style_fontsize_20
                            )
                        ])
                    ], style=style.style_rightdiv)
                ], style=style.style_flex_wrap)
            ])
        ]),
        dcc.Tab(label="Average Vaccination by Age Group", children=[
            html.Div([
                html.Div([
                    # Charts and drop-down menus
                    html.Div([
                        html.H2("Average Vaccination Analysis", style=style.style_h2_bold_28px),
                        dcc.Graph(id="plot2", style=style.style_graph_wh400),
                        html.Div([
                            # Select Month for Plot 2
                            html.Div([
                                html.Label("Select Month for Plot 2:", style=style.style_fontsize_18),
                                html.Div([
                                    dcc.Dropdown(
                                        id="dropdown-month2",
                                        options=[{"label": month, "value": i + 1} for i, month in enumerate(
                                            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])],
                                        placeholder="Select Month",
                                        style=style.style_dropdown_width_60
                                    ),
                                    html.Div(
                                        "choose the Month/Year as you need, expect November and December 2022",
                                        style=style.style_dropdown_remark
                                    )
                                ], style=style.style_dropdown_flex_center)
                            ], style=style.style_margin_bottom_20),

                            # Select Year for Plot 2
                            html.Div([
                                html.Label("Select Year for Plot 2:", style=style.style_fontsize_18_margintop10),
                                dcc.Dropdown(
                                    id="dropdown-year2",
                                    options=[{"label": str(year), "value": year} for year in [2021, 2022]],
                                    placeholder="Select Year"
                                )
                            ])
                        ], style=style.style_margin_top_20),

                        # Additional text on the right
                        html.Div(
                            "Analysis based on desired month as you want (no data in NOV and DEC 2022)",
                            style=style.style_bold_18px_margintop20
                        ),
                    ], style=style.style_leftdiv_border),

                    # Right: Text content
                    html.Div([
                        html.H3("Average Vaccination by Age Group", style=style.style_h3_bold_24_center),
                        html.Div([
                            html.H4("Investigation", style=style.style_h4_bold_22),
                            html.P(
                                "The bar graph illustrating the correlation between age and average vaccination rates indicates that the highest percentage of vaccinations occur within the elderly population, specifically those aged 65 and above. "
                                "This trend is likely due to the severe impact COVID-19 has on this demographic, combined with the significant protective benefits offered by the vaccines. Conversely, the vaccination rate among children younger than four years old is notably low."
                                "This is generally attributed to the fact that the potential side effects of the vaccines often outweigh the risks associated with a COVID-19 infection in this age group.",
                                style=style.style_fontsize_20
                            ),
                            html.P(
                                "According to the chart we have drawn, the horizontal axis indicates the different age groups, and the vertical axis indicates the percentage of vaccination completion. "
                                "We can see that the highest vaccination completions are found among those over 65 years old, with over 80%. In contrast, the younger age groups have a relatively low vaccination completion rate."
                                "Also, the trend in Figure 2 clearly shows a positive correlation",
                                style=style.style_fontsize_20
                            ),
                            html.H4("Conclusion", style=style.style_h4_bold_22),
                            html.P(
                                "It's clear that the vaccination rate tends to increase with age, demonstrating a greater health consciousness among older individuals. In light of these observations,  "
                                "it is essential for the government to intensify its vaccination awareness campaigns targeted towards younger demographics, particularly the youth, in order to bolster their vaccination rates.",
                                style=style.style_fontsize_20
                            )
                        ])
                    ], style=style.style_rightdiv)
                ], style=style.style_flex_wrap)
            ])
        ]),

        dcc.Tab(label="Administered Daily vs Series Complete Daily", children=[
            html.Div([
                html.Div([
                    # Left side: chart and drop-down menu
                    html.Div([
                        html.H2("Administered Daily vs Series Complete Daily Analysis", style=style.style_h2_bold_28px),
                        dcc.Graph(id="plot3", style=style.style_graph_wh400),
                        html.Div([
                            # Select Month for Plot 3
                            html.Div([
                                html.Label("Select Month for Plot 3:", style=style.style_fontsize_18),
                                html.Div([
                                    dcc.Dropdown(
                                        id="dropdown-month3",
                                        options=[{"label": month, "value": i + 1} for i, month in enumerate(
                                            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])],
                                        placeholder="Select Month",
                                        style=style.style_dropdown_width_60
                                    ),
                                    html.Div(
                                        "choose the Month/Year as you need, expect November and December 2022",
                                        style=style.style_dropdown_remark
                                    )
                                ], style=style.style_dropdown_flex_center)
                            ], style=style.style_margin_bottom_20),

                            # Select Year for Plot 3
                            html.Div([
                                html.Label("Select Year for Plot 3:", style=style.style_fontsize_18_margintop10),
                                dcc.Dropdown(
                                    id="dropdown-year3",
                                    options=[{"label": str(year), "value": year} for year in [2021, 2022]],
                                    placeholder="Select Year"
                                )
                            ])
                        ], style=style.style_margin_top_20),

                        # Additional text on the right
                        html.Div(
                            "Analysis based on desired month as you want (no data in NOV and DEC 2022)",
                            style=style.style_bold_18px_margintop20
                        ),
                    ], style=style.style_leftdiv_border),

                    # Right side: text content
                    html.Div([
                        html.H3("Administered Daily vs Series Complete Daily", style=style.style_h3_bold_24_center),
                        html.Div([
                            html.H4("Investigation", style=style.style_h4_bold_22),
                            html.P(
                                "The global pandemic has disrupted lives on an unprecedented scale. The story of our fight against COVID-19 takes an important turn with the onset of vaccination. "
                                "Our visualization brings to light the critical relationship between the number of vaccine doses administered daily and the completion of the vaccine series.",
                                style=style.style_fontsize_20
                            ),
                            html.P(
                                "The scatter plot at the heart of our story displays the number of vaccine doses administered daily on the x-axis, against the daily count of completed vaccine series on the y-axis. "
                                "Each point represents a single day's data, mapping the relationship between these two variables.",
                                style=style.style_fontsize_20
                            ),
                            html.P(
                                "The trend captured by the dashed red line in the scatter plot suggests a positive correlation. As the number of vaccines administered daily increases, so does the completion rate of the vaccine series. "
                                "This is an encouraging trend as it indicates that as we are accelerating our vaccine distribution, individuals are also completing their vaccination schedules. "
                                "The inclusion of the linear regression line helps to underscore this positive correlation, while the absence of the standard error limits ensures the story remains focused on the overall trend, rather than deviations from the norm.",
                                style=style.style_fontsize_20
                            ),
                            html.H4("Conclusion", style=style.style_h4_bold_22),
                            html.P(
                                "As the daily administration of COVID-19 vaccine doses increases, there's a corresponding rise in the completion of vaccination series. "
                                "This trend underscores the importance of continuing to ramp up vaccine distribution efforts to control the spread of the virus.",
                                style=style.style_fontsize_20
                            )
                        ])
                    ], style=style.style_rightdiv)
                ], style=style.style_flex_wrap)
            ])
        ]),

        dcc.Tab(label="Summary Takeaways/About Page", children=[
            html.Div([
                html.H2("Summary Takeaways", style=style.style_h2_center),
                html.P([
                    html.B("1. Through our findings, we found a positive correlation between age group and vaccination completion. "),
                    "As age increases, the care for vaccines gradually increases, so that those over 65 years old are the group with the highest vaccination completion rate. This is most likely due to the fact that people over 65 years old belong to the vulnerable group, and because of the low immunization rate and high risk, they will rely more on the vaccine for their protection."
                ]),
                html.P([
                    html.B("2. However, at the same time, for the lower age groups (adolescents and new adults), vaccination completion is generally the lowest. "),
                    "This group does not have a high awareness of vaccination, which demonstrates the attitude of adolescents and young adults towards vaccination. The results of these analyses make us realize that when promoting vaccination, we should focus on younger groups to increase their awareness and vaccination rates."
                ]),
                html.P([
                    html.B("3. We also found that as the daily administration of COVID-19 vaccine doses increases, there's a corresponding rise in the completion of vaccination series. "),
                    "Therefore, we believe that the vaccine has a certain level of acceptance in the eyes of the public and that people generally believe that the vaccine can help them stay somewhat away from the disease."
                ]),
                html.H2("About Page", style=style.style_h2_center),
                html.P("Please feel free to browse the various interactive pages of our shiny app to explore the visualizations, statistics, and insights we have compiled. We hope this project will spark curiosity, promote data literacy, and contribute to a deeper understanding of COVID-19 vaccination trends across the United States. This project serves as an avenue for us to delve into the rich dataset and present our findings in an interactive and informative manner. Through this shiny app, we aim to provide a nuanced understanding of the vaccination landscape, empower individuals to make informed decisions, and contribute to the ongoing discourse surrounding the COVID-19 pandemic."),
                html.H2("Dataset Source", style=style.style_h2_center),
                html.P([
                    "We have selected two datasets from ",
                    html.A("https://data.gov/", href="https://data.gov/", target="_blank"),
                    " that are relevant to our idea."
                ]),
                html.A(
                    "COVID-19 Vaccination and Case Trends by Age Group, United States",
                    href="https://catalog.data.gov/dataset/covid-19-vaccination-and-case-trends-by-age-group-united-states-e81b4",
                    target="_blank"
                ),
                html.Br(),
                html.A(
                    "COVID-19 Vaccination Trends in the United States, National and Jurisdictional",
                    href="https://catalog.data.gov/dataset/covid-19-vaccination-trends-in-the-united-statesnational-80d4f",
                    target="_blank"
                ),
                html.H2("At the end", style=style.style_h2_center),
                html.P("Thank you for joining us on this data-driven journey, and we sincerely hope that this analysis will provide valuable insights into the progress of COVID-19 vaccination efforts.")
            ])
        ])
    ])
])

# Callback function: draw the first chart
@app.callback(
    Output("plot1", "figure"),
    [Input("dropdown-month1", "value"),
     Input("dropdown-year1", "value")]
)
def update_plot1(month, year):
    if month and year:
        filtered_df = wrangling_df[
            (wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)
        ]
        if not filtered_df.empty:
            grouped_df = filtered_df.groupby("AgeGroupVacc")["Series_Complete_Pop_pct_agegroup"].mean().reset_index()
            fig = px.scatter(
                grouped_df,
                x="AgeGroupVacc",
                y="Series_Complete_Pop_pct_agegroup",
                title="Series Complete Vaccination by Age Group",
                labels={
                    "AgeGroupVacc": "Age Group",  # X-axis label
                    "Series_Complete_Pop_pct_agegroup": "Series Complete Pop pct agegroup"  # Y-axis label
                }
            )
            fig.update_layout(title={'x': 0.5})  
            return fig

    fig = px.scatter(
        title="Series Complete Vaccination by Age Group",
    )
    fig.update_layout(title={'x': 0.5})
    return fig

# Callback function: draw the second chart
@app.callback(
    Output("plot2", "figure"),
    [Input("dropdown-month2", "value"),
     Input("dropdown-year2", "value")]
)
def update_plot2(month, year):
    if month and year:
        filtered_df = wrangling_df[
            (wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)
        ]
        if not filtered_df.empty:
            grouped_df = filtered_df.groupby("AgeGroupVacc")["Administered_Dose1_pct_agegroup"].mean().reset_index()
            fig = px.bar(
                grouped_df,
                x="AgeGroupVacc",
                y="Administered_Dose1_pct_agegroup",
                title="Average Vaccination by Age Group",
                labels={
                    "AgeGroupVacc": "Age Group",  # X-axis label
                    "Administered_Dose1_pct_agegroup": "Average Vaccination"  # Y-axis label
                }
            )
            fig.update_layout(title={'x': 0.5})
            return fig

    fig = px.bar(
        title="Average Vaccination by Age Group",
    )
    fig.update_layout(title={'x': 0.5})
    return fig

# Callback function: draw the third chart
@app.callback(
    Output("plot3", "figure"),
    [Input("dropdown-month3", "value"),
     Input("dropdown-year3", "value")]
)
def update_plot3(month, year):
    if month and year:
        filtered_df = wrangling_df[
            (wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)
        ]
        if not filtered_df.empty:
            fig = px.scatter(
                filtered_df,
                x="Administered_Daily",
                y="Series_Complete_Daily",
                title="Administered Daily vs Series Complete Daily",
                labels={
                    "Administered_Daily": "Administered Daily",
                    "Series_Complete_Daily": "Series Complete Daily"
                }
            )
            fig.update_layout(title={'x': 0.5})
            return fig

    fig = px.scatter(title="Administered Daily vs Series Complete Daily")
    fig.update_layout(title={'x': 0.5})
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)





