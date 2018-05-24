from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class MyPage(Page):

    def parties_choices(self):

        if self.player.radical:
            choices = ['pda', 'svp']
            random.shuffle(choices)
            return choices
        else:
            choices = ['bdp', 'evp']
            random.shuffle(choices)
            return choices

    form_model = 'player'
    form_fields = ['parties', 'political_views']

    def vars_for_template(self):
        if self.player.radical:
            return {'image1': "political_game/pda.png", 'image2': "political_game/svp.png"}
        else:
            return {'image1': "political_game/bdp.png", 'image2': "political_game/evp.png"}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
