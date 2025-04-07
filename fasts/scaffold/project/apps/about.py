from datetime import datetime

import fasthtml.common as view

from fasts.core.fastcss import css, render

# Define CSS styles for the about page
css(
    'body',
    background_color='#313131',
    font_family='Arial, sans-serif',
    display='flex',
    justify_content='center',
    width='100%',
    padding_top='5%'
)

css(
    '#about',
    display='flex',
    flex_direction='column',
    justify_content='center',
    min_width='400px',
    max_width='50%',
)
css('h1', color='#8C8C8C')
css('p', font_size='16px', line_height='1.5', color='#E6E6E6')
css(
    '#footer',
    font_size='12px',
    color='#8C8C8C',
    text_align='center',
    margin_top='20px'
)

about_css = render()


def about_page():
    paragraphs = [
        '''Você é uma daquelas pessoas que gostam da ideia de atuar em um
        projeto full stack em sua linguagem favorita, mas não conseguiu
        encontrar um desses projetos ainda?''',
        '''Python é a sua linguagem favorita e você gostaria de trabalhar com
        ela tanto no frontend quanto no backend de suas aplicações web?''',
        '''Acho que o 3Fast Framework pode ser pra você!''',
        '''Ele é um framework full stack, que utiliza o que chamamos de 3
        fasts, sendo FastAPI + FastHTML + FastCSS.''',
        '''Esta última lib foi criada por nós e minimamente estabelecida para
        impedir que precisemos escrever código CSS em algum momento,
        substituindo e mapeando os estilos por meio de chamadas a funções
        Python.''',
    ]

    return view.Html(
        view.Head(view.Title('3Fast Framework'), view.Style(about_css)),
        view.Body(
            view.Div(
                view.H1('3Fast Framework'),
                *[view.P(p) for p in paragraphs],
                view.P(
                    f'3Fast Framework - {datetime.now().year}',
                    id='footer'
                ),
                id='about',
            ),
        )
    )
