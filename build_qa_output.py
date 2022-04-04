#%%
# import datetime
import pandas as pd
from contextlib import redirect_stdout

from index_html_helpers import start_doc, end_doc

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
            start_doc()
            print(f"<h3>Covid Death Data - date range: {user_begin} - {user_end}</h3>")
            covid_df = covid_death_date_range_df(data=df, date_begin=user_begin, date_end=user_end)
            print(covid_df.to_html())

            end_doc()

# %%
