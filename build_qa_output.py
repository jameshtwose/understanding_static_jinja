#%%
# import datetime
import pandas as pd
import seaborn as sns
from contextlib import redirect_stdout
import plotly.graph_objects as go
import plotly.express as px

from index_html_helpers import navbar_end, navbar_start, start_doc, end_doc

#%%
df = (pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
    .assign(date=lambda d: pd.to_datetime(d["date"]))
)
#%%
def covid_death_date_range_df(data, date_begin="2020-02-24", date_end="2020-03-24"):
    columns_list = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 
                    'total_deaths', 'new_deaths']
    return data.loc[data["date"].between(left=date_begin, right=date_end), columns_list]

#%%
user_begin="2020-02-24"
user_end="2020-03-24"
covid_df = covid_death_date_range_df(data=df, 
date_begin=user_begin, 
date_end=user_end)

#%%
cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)
#%%
def plot_line_plot(data):

    fig = px.line(
        data_frame=data[data["location"].isin(["Portugal", "Netherlands", "Finland"])],
        x='date',
        y="total_cases",
        color="location",
        markers=True
    )
    # fig
    # fig.update_traces(line_color='#743de0')

    fig.update_layout(title="Covid total cases in various countries",
                        xaxis_title='Date',
                        yaxis_title="Total Cases",
                        paper_bgcolor='rgb(34, 34, 34)',
                            plot_bgcolor='rgb(34, 34, 34)',
                            template="plotly_dark",
                        )
    return fig


# plot_line_plot(data=covid_df).to_html()

#%%
file_name_data_range_dict = {"output_files/covid_data_1.html": ("2020-02-24", "2020-03-24"),
                            "output_files/covid_data_2.html": ("2020-03-24", "2020-04-24"),
                            "output_files/covid_data_3.html": ("2020-04-24", "2020-05-24"),
                            "output_files/covid_data_4.html": ("2020-05-24", "2020-06-24"),
}

for file_name in file_name_data_range_dict:
    user_begin = file_name_data_range_dict[file_name][0]
    user_end = file_name_data_range_dict[file_name][1]
    with open(file_name, "w") as f:
        with redirect_stdout(f):
            start_doc(style_link="../style.css")
            print("<section id='mainbody'>")
            print(f"<h3>Covid Death Data - date range: {user_begin} - {user_end}</h3>")
            covid_df = covid_death_date_range_df(data=df, date_begin=user_begin, date_end=user_end)
            print(plot_line_plot(data=covid_df).to_html())
            print(covid_df.head(5).style.background_gradient(cmap, 
                            subset=['new_cases'], 
                            axis=1, 
                            vmin=0, 
                            vmax=100
                            )
                            .to_html())
            print(covid_df
            [["location", "total_cases", "total_deaths"]]
            .groupby("location")
            .describe()
            # .style.background_gradient(cmap, 
            #     subset=['mean'], 
            #     axis=1, 
            #     vmin=0, 
            #     vmax=100
            #     )
                .to_html())
            print("</section>")
            navbar_start(home_link="../index.html")
            navbar_end()

            end_doc()

# %%
