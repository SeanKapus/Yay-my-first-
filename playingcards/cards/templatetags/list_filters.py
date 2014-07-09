import random
from django import template

register = template.Library()

@register.filter
def suit(list, suit_type):
    return [item for item in list if item.get_suit_display() == suit_type]

@register.filter
def rank(list, rank):

    return [item for item in list if item.rank == rank]

@register.filter
def shuffle(cards):
    cards = list(cards)
    random.shuffle(cards)
    return cards

@register.filter
def deal(list, amount):
    return list[:amount]