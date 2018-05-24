from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'charity_game'
    players_per_group = None
    num_rounds = 1
    minguess = 0
    maxguess = 100


import random


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.charity1 = random.choice([True, False])
            p.charity2 = random.choice([True, False])
            p.endowment = random.randint(Constants.minguess, Constants.maxguess)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    charity1 = models.BooleanField()
    charity2 = models.BooleanField()
    decision = models.StringField(widget=widgets.RadioSelect, choices=['SickKids Foundation',
                                                                       'WellChild Foundation'])
    endowment = models.IntegerField(min=Constants.minguess,
                                    max=Constants.maxguess)
