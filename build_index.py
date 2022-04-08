#%%
from glob import glob
from contextlib import redirect_stdout

from index_html_helpers import start_doc, end_doc, navbar_start, navbar_end, dropdown_example, dropdown_begin

#%%
file_name="index.html"
with open(file_name, "w") as f:
    with redirect_stdout(f):
        title_string="Covid Data"
        start_doc(title_string = title_string)       
        print("<section id='mainbody'>")
        print(f"<h1>{title_string}</h1>")
        print("<ul>")
        # for covid_file in sorted(glob("output_files/*")):
        
        #     print(f'<li><a href={covid_file}>{covid_file[13:-5]}</a></li>')

        # print("</ul>")

        print(f"<h3>A landing page of a selection of covid data exports</h3>")

        print("</section>")

        navbar_start()
        
        dropdown_begin()
        for covid_file in sorted(glob("output_files/*")):
            list_element = f"""<li><a class="dropdown-item" href="{covid_file}">{covid_file[13:-5]}</a></li>"""
            print(list_element)
        print("""</ul>
    </div>""")

        # dropdown_example()
        
        navbar_end()
        end_doc()

# %%
