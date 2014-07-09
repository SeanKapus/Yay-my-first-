from StdSuites import data
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.utils import timesince
from cards.forms import EmailUserCreationForm
from cards.models import Card, WarGame
from playingcards import settings


def home(request):
    data = {
        'cards': Card.objects.all()
    }
    return render(request, 'cards.html', data)


# def Club-card(request):
#     data = {
#         'cards': Card.objects.all()
#     }
#     return render(request, 'club_cards.html', data)


def card_filters(request):
    data = {
        'cards': Card.objects.all()
    }
    return render(request, 'card_filters.html', data)

@login_required
def profile(request):
    war_games = WarGame.objects.filter(player=request.user)
    total_games = WarGame.objects.filter(player=request.user).count()
    if total_games == 10:
        user = request.user
        user.email_user('you finished ten games')

    return render(request, 'profile.html', {"war_games":war_games})


def faq(request):
    return render(request, 'faq.html')


def blackjack(request):
    cards = Card.objects.order_by('?')
    user_cards = Card.objects.order_by('?')[:2]
    dealer_cards= Card.objects.order_by('?')[2:4]
    data = {
        'user_cards': user_cards,
        'dealer_cards': dealer_cards
    }
    return render(request, 'blackjack.html', data)


def poker(request):
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, "poker.html", data)


def hearts(request):
    data = {'cards': Card.objects.filter(suit=3)}

    return render(request, 'hearts.html', data)


def not_face(request):
    data = {'cards': Card.objects.exclude(rank=['jack', 'queen', 'king'])}

    return render(request, 'not_face.html', data)

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {} {} {}'.format(user.first_name, user.last_name, user.date_joined)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site since you joined on {}</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


# def profile(request):
#     if not request.user.is_authenticated():
#         return redirect("login")
#
#     return render(request, 'profile.html', {})
# @login_required replaces request user

# @login_required
# def profile(request):
#     return render(request, 'profile.html', {})



@login_required()
def war(request):
    cards = list(Card.objects.order_by('?'))
    user_card = cards[0]
    dealer_card = cards[1]

    result = user_card.get_war_result(dealer_card)
    WarGame.objects.create(result=result, player=request.user)

    return render(request, 'war.html', {
        'user_cards': [user_card],
        'dealer_cards': [dealer_card],
        'result': result
    })


