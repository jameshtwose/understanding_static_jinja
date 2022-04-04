def start_doc(title="Covid Data"):
    print(
        f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title> {title}
    </title>
    <link rel="preconnect" href="https://fonts.googleapis.com"> 
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
    </head>
    <body>
    <h2><a href="../index.html">Home</a></h2>
    """
    )

    # <h1> This is a first level heading </h1> (can be inside header)
    # <div class="myDiv">
    #   <h2>This is a heading in a div element</h2>
    #   <p>This is some text in a div element.</p>
    # </div>


def end_doc():
    print(
        """
    </body>
    </html>
    """
    )


def format_paragraph(statement: str) -> str:
    """Simple format for html paragraph
    Parameters
    ----------
    statement : str
        paragraph to be printed
    Returns
    -------
    str
        statement with paragraph tag
    """
    return "<p>" + str(statement) + "</p>"


def format_exception(statement: str) -> str:
    """Style paragraph with red color
    Parameters
    ----------
    statement : str
        exception to be printed
    Returns
    -------
    str
        statement with paragraph and exception tag
    """
    return '<p class="exception">' + str(statement) + "</p>"

