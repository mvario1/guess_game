from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'guess_game'
    players_per_group = None
    num_rounds = 1
    endowment = 100
    minguess = 0
    maxguess = 100
    marco_constant = 'Marco'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.IntegerField(min=Constants.minguess,
                                max=Constants.maxguess)
    toguess = models.IntegerField(min=Constants.minguess,
                                max=Constants.maxguess)
