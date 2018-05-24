from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class MyPage(Page):
    form_model = 'player'
    form_fields = ['donation1', 'donation2']

    def vars_for_template(self):
        if self.player.charity1:
            image1 = "charity_game/a_pers.png"
        else:
            image1 = "charity_game/a_gen.png"
        if self.player.charity2:
            image2 = "charity_game/b_pers.png"
        else:
            image2 = "charity_game/b_gen.png"
        foundations = ['SickKids', 'WellChilds']
        return {'image1': image1,
                'image2': image2,
                "foundations":foundations}

    def donation1_max(self):
        return self.player.endowment

    def donation2_max(self):
        return self.player.endowment

    def error_message(self, values):
        print('value is', values)
        if values["donation1"] + values["donation2"] != self.player.endowment:
            return 'the total donation must add up to your total endowment'

    timeout_seconds = 5

    def before_next_page(self):
        if self.timeout_happened:
            self.player.donation1 = random.randint(Constants.minguess,
                                                   self.player.endowment)
            self.player.donation2 = self.player.endowment - self.player.donation1



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
