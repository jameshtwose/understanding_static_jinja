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

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" />
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>

<h1>{title_string}</h1>

"""
#%%
navbar_start_string="""
<section id="info-bar">
    <div class="nav-bar">
        <nav class="navbar navbar-expand-lg">
            <a class="navbar-brand" href="https://services.jms.rocks"><img src="https://services.jms.rocks/img/logo.png" /></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fa fa-bars"></i>
      </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="index.html">Home</a>
                    </li>
"""

navbar_end_string="""
                    </ul>
            </div>
        </nav>
    </div>
</section>
"""

#%%
file_name="index.html"
with open(file_name, "w") as f:
    with redirect_stdout(f):
        print(start_string)
        print("<ul>")
        for covid_file in sorted(glob("output_files/*")):
        
            print(f'<li><a href={covid_file}>{covid_file[13:-5]}</a></li>')

        print("</ul>")

        print(navbar_start_string)
        for covid_file in sorted(glob("output_files/*")):
            list_element = f"""<li class="nav-item">
                        <a class="nav-link" href="{covid_file}">{covid_file[13:-5]}</a>
                    </li>
                    """
            print(list_element)
        print(navbar_end_string)
        end_doc()

# %%
