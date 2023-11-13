from nicegui import ui
from datetime import datetime
from nicegui.events import MouseEventArguments
ui.query('body').classes('bg-gradient-to-r from-blue-500 to-transparent ')

with ui.card().classes('column items-center gap-0'):
    date = ui.label().style('font-size: 2rem')
    time = ui.label()
    ui.timer(1.0, lambda: date.set_text(datetime.now().strftime('%d/%m/%Y')))
    ui.timer(0.1, lambda: time.set_text(datetime.now().strftime('%H:%M:%S')))
ui.image('thunderbolt.png').classes('h-96').props('fit=scale-down')

with ui.column().classes('absolute-center items center'):
    ui.label('bolt').classes('text-8xl')
    ui.input('User')
    ui.input('Password')
    ui.button('login')
    ui.button('New User')
    ui.link('forgot password', '')

ui.run()
