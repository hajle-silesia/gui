from application_window import ApplicationWindow
from tab_bar import TabBar
from tab import Tab, Container
from leaf import Title
from config import config


application_window = ApplicationWindow(config['application_window'])

tab_bar = TabBar(application_window, config['tab_bar'])
recipe = Tab(tab_bar, config['recipe'])

user_settings = Container(recipe, config['user_settings'])
miscs = Container(recipe, config['miscs'])
fermentables = Container(recipe, config['fermentables'])
parameters = Container(recipe, config['parameters'])
mash_steps = Container(recipe, config['mash_steps'])
hops = Container(recipe, config['hops'])

Title(user_settings)
Title(miscs)
Title(fermentables)
Title(parameters)
Title(mash_steps)
Title(hops)

application_window.position()

application_window.mainloop()
