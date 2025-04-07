from apps.about import about_page
from fastapi import FastAPI
from fasthtml.common import FastHTML

app = FastAPI()
frontend = FastHTML()


# Mount the about frontend
@frontend.route('/about')
def about():
    return about_page()


app.mount('', frontend)
