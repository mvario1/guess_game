from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minguess, Constants.maxguess)
        self.player.toguess = toguess

class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']

    def before_next_page(self):
        diff = abs(self.player.toguess - self.player.guess)
        self.player.payoff = Constants.endowment - diff

class Results(Page):
    def vars_for_template(self):
        return {'diff':  abs(self.player.toguess - self.player.guess)}

page_sequence = [
    Intro,
    Decision,
    Results
]
