import pandas as pd

html_string = """
    <html>
    <head><title>Latest PPRA Tenders</title></head>
    <body>
        <style>
        table {
            border-collapse: collapse;
            border: 1px solid silver;
        }
        table tr:nth-child(even) {
            background: #E0E0E0;
        }
        </style>
        %s
    </body>
    </html>
"""


def convertToHTML():
    df = pd.read_csv('books.csv')
    table_html = df.to_html(index=False, render_links=True,
                            justify="center", escape=False, border=4)
    with open('books.html', 'w') as f:
        f.write(html_string % (table_html))


convertToHTML()
