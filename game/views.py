from django.shortcuts import render
from django.forms import ModelForm
from game.models import Game
import datetime
# Create your views here.
def new(request):
    class GameForm(ModelForm):
        class Meta:
            model = Game
            fields = ['title']


    form = GameForm()
    context = { 'gameForm': form.as_p() }

    if request.method == 'POST':

        game = GameForm(request.POST)

        if game.is_valid():
            game.save()
            context['game'] = game.data['title']

    return render(request, 'frontline/new-game.html', context)
