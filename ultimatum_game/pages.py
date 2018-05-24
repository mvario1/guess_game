from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
   # timeout_seconds = 10

   form_model = 'player'
   form_fields = ['odd_negative']

   def odd_negative_error_message(self, value):
       print('value is', value)
       if value != 10:
           return 'Wrong answer'


class Decision1(Page):

    def is_displayed(self):
        return self.player.role() == 'sender'

    form_model = 'group'
    form_fields = ['dg_decision']

class ResultsWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        pass

class Decision2(Page):
    def is_displayed(self):
        return self.player.role() == 'receiver'


    form_model = 'group'
    form_fields = ['response']


class ResultsWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        sender = self.group.get_player_by_role('sender')
        receiver = self.group.get_player_by_role('receiver')
        return {'sender_payoff':sender.payoff, 'receiver_payoff':receiver.payoff}


page_sequence = [
    Intro,
    Decision1,
    ResultsWaitPage1,
    Decision2,
    ResultsWaitPage2,
    Results
]
