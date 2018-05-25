from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):

    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = 'player'
    form_fields = ['donation']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        total_payoffs = [p.participant.payoff for p in self.group.get_players()]
        series = [{
            'name': 'Payoffs',
            'type': 'column',
            'data': [g.totaldonation for g in self.group.in_all_rounds()]
            # 'data': [p.payoff for p in self.group.get_players()],
        }
        ]
        return {'series': series,
                "total_payoffs":total_payoffs}

    # def vars_for_template(self):
    #     total_donation = sum([p.donation for p in self.group.get_players()])
    #     return {"t": total_donation
    #             }


page_sequence = [
    Intro,
    MyPage,
    ResultsWaitPage,
    Results
]
