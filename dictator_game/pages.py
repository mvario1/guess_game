from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['gender']


class Decision(Page):
    form_model = 'group'
    form_fields = ['dg_decision']

    def vars_for_template(self):
        receiver = self.group.get_player_by_role('receiver')
        return {'receiver_gender':receiver.get_gender_display()}

    def is_displayed(self):
        return self.player.role() == 'dictator'

class WP(WaitPage):
    body_text = 'please wait for Dictator'
    def after_all_players_arrive(self):
        self.group.set_payoffs()
        pass


class Results(Page):
    def vars_for_template(self):
        dictator = self.group.get_player_by_role('dictator')
        receiver = self.group.get_player_by_role('receiver')
        return {'dictator_payoff':dictator.payoff, 'receiver_payoff':receiver.payoff}


page_sequence = [
    Intro,
    WaitPage,
    Decision,
    WP,
    Results
]
