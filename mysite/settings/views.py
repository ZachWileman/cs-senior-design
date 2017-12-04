from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Attack

from .forms import AttackForm


class SettingsView(View):

    def get(self, request):
        return render(request, 'settings/settings_page.html', {'attacks': Attack.objects.all()})

    def post(self, request):
        # Grabs all of the attack names
        attacks_names = []
        attacks = Attack.objects.all()
        for attack in attacks:
            attacks_names.append(attack.name)

        for attack in attacks_names:
            # Grab the current attack from the database for later use
            current_attack = Attack.objects.get(name=attack)

            # Check to see what the attack's detection was set to
            detection = request.POST.get(attack, 0)

            # Update the detection value in the database for each Attack
            if detection == 'on':
                current_attack.detection = True
            else:
                current_attack.detection = False

            # Save the updated version of each attack's detection to the database
            current_attack.save()

        return self.get(request)


class SubmitAttackView(View):

    def get(self, request):
        return render(request, 'notifications/submit_form.html', {'form': AttackForm})

    def post(self, request):
        form = AttackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<p>Successfully added form.</p>')

        else:
            return HttpResponse('<p>An error has occured with the POST data sent; the form wasn\'t able to validate \
                                 the form data.</p>')
