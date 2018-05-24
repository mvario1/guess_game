from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'political_game'
    players_per_group = None
    num_rounds = 1

import random

class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.radical = random.choice([True, False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    radical = models.BooleanField()
    parties = models.StringField(widget=widgets.RadioSelect)
    political_views = models.IntegerField(choices=list(range(11)), widget=widgets.RadioSelectHorizontal)