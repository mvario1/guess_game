from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'publicgood_game'
    players_per_group = 3
    num_rounds = 3
    minguess = 0
    maxguess = 100
    endowment = 100
    efficiency_factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    totaldonation = models.IntegerField()
    # totalpayoff = models.IntegerField()
    share = models.IntegerField()
    hohoho = models.IntegerField()

    def set_payoffs(self):
        self.totaldonation = sum([p.donation for p in self.get_players()])

        self.share = self.totaldonation * 2 / Constants.players_per_group

        for p in self.get_players():
            p.payoff = Constants.endowment - p.donation + self.share




class Player(BasePlayer):
    hahaha = models.StringField()
    donation = models.IntegerField(min=Constants.minguess,
                                   max=Constants.maxguess)
