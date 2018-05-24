from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class MyPage(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        if self.player.charity1:
            image1 = "charity_game/a_pers.png"
        else:
            image1 = "charity_game/a_gen.png"
        if self.player.charity2:
            image2 = "charity_game/b_pers.png"
        else:
            image2 = "charity_game/b_gen.png"

        return {'image1': image1,
                'image2': image2}


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
