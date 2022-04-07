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
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400&display=swap" rel="stylesheet">
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

def start_doc_index(title_string="Covid Data"):
    print(f"""<!DOCTYPE html>
        <html>

        <head>
            <title> {title_string}
            </title>

            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" />
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script> -->
            
            <script src="https://getbootstrap.com/docs/5.0/dist/js/bootstrap.bundle.min.js"></script>

            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="style.css">
        </head>

        <body>

        """)

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

def navbar_start():
    print("""
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
    """)

def navbar_end():
    print("""
                        </ul>
                </div>
            </nav>
        </div>
    </section>
    """)

def dropdown_example():
    print("""
    <!-- Example single danger button -->
    <div class="btn-group">
    <button type="button" class="btn btn-danger dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Action
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">Separated link</a></li>
    </ul>
    </div>
    """)

def dropdown_begin():
    print("""
    <div class="btn-group">
    <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Files
    </button>
    <ul class="dropdown-menu">

    """)