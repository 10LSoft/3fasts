import fasthtml.common as view


def about_page():
    paragraphs = [
        'This is a simple example of a FastAPI application using fasthtml.',
        '''The 3Fast framework is designed to make it easy to build fast and
        efficient web applications.''',
        '''It provides a simple and intuitive API for building web applications
            using Python.''',
    ]

    return view.Html(
        view.Head(view.Title('About 3Fast Framework')),
        view.Body(
            view.H1('About 3Fast Framework'),
            *[view.P(p) for p in paragraphs],
        ),
    )
