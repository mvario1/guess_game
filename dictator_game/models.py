from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_game'
    players_per_group = 2
    num_rounds = 1
    Endowment = 100
    minguess = 0
    maxguess = 100

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dg_decision = models.IntegerField(min=Constants.minguess,
                                      max=Constants.maxguess,
                                      verbose_name = 'How much money would you like to give?',
                                      doc='dicators decision')

    def set_payoffs(self):
        dictator = self.get_player_by_role('dictator')
        receiver = self.get_player_by_role('receiver')
        dictator.payoff = Constants.Endowment - self.dg_decision
        receiver.payoff = self.dg_decision


class Player(BasePlayer):
    def role(self):
        if self.id_in_group==1:
            return 'dictator'
        else:
            return 'receiver'


