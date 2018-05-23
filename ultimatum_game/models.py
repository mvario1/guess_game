from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_game'
    players_per_group = 2
    num_rounds = 1
    endowment = 100
    minguess = 0
    maxguess = 100

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dg_decision = models.IntegerField(min=Constants.minguess,
                                      max=Constants.maxguess,
                                      verbose_name='How much money would you like to give?',
                                      doc='sender decision')


    response = models.IntegerField(choices=
                                 ((0,'Yes'),
                                  (1,'No')),
                                 widget=widgets.RadioSelectHorizontal,
                                 )



    def set_payoffs(self):
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        if self.response == 0:

            sender.payoff = Constants.endowment - self.dg_decision
            receiver.payoff = self.dg_decision
        else:
            sender.payoff = 0,
            receiver.payoff = 0




class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'receiver'
