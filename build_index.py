#%%
from glob import glob
from contextlib import redirect_stdout

from index_html_helpers import start_doc, end_doc

#%%
title_string="Covid Data"
start_string = f"""<!DOCTYPE html>
<html>

<head>
    <title> {title_string}
    </title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>

<h1>{title_string}</h1>

"""

#%%
file_name="index.html"
with open(file_name, "w") as f:
    with redirect_stdout(f):
        print(start_string)
        print("<ul>")
        for covid_file in sorted(glob("output_files/*")):
        
            print(f'<li><a href={covid_file}>{covid_file}</a></li>')

        print("</ul>")

        end_doc()

# %%
