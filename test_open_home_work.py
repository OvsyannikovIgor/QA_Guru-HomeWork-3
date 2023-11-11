import time

from selene import have
from selene.support.shared import browser


def test_open_home_work():
    browser.open('https://github.com/OvsyannikovIgor/QA_Guru-HomeWork-3/pull/2')
    browser.element('.js-timeline-item').should(have.text("Merge branch 'main' into conflict"))
    time.sleep(7)
