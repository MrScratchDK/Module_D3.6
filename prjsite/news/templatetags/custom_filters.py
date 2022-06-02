# from django import template
#
#
# register = template.Library()
#
#
# @register.filter()
# def censor(text):
#    BAD_WORDS = ['немного']
#
#    for i in text.split():
#       if i.lower() in BAD_WORDS:
#          return f'{i[0].title()}{"*" + (len(i) - 1)}'
#    return f'{text}'