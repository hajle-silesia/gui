from tkinter import *

config = {'application_window': {'name': "Hajle Silesia Homebrewing System",
                                 'icon_path': "./img/icon.png"
                                 },
          'tab_bar': {'name': "Tab bar",
                      },
          'recipe': {'name': "Recipe",
                     },
          'user_settings': {'name': "User settings",
                            'row': 0,
                            'column': 0,
                            'columnspan': 3,
                            'sticky': EW + N,
                            },
          'miscs': {'name': "Miscs",
                    'row': 1,
                    'column': 0,
                    'sticky': NSEW,
                    },
          'fermentables': {'name': "Fermentables",
                           'row': 1,
                           'column': 1,
                           'sticky': NSEW,
                           },
          'parameters': {'name': "Parameters",
                         'row': 1,
                         'column': 2,
                         'sticky': NSEW,
                         },
          'mash_steps': {'name': "Mash steps",
                         'row': 2,
                         'column': 0,
                         'sticky': NSEW,
                         },
          'hops': {'name': "Hops",
                   'row': 2,
                   'column': 1,
                   'sticky': NSEW,
                   },
          }
