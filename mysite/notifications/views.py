from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import NotificationForm
from settings.models import Attack


class SubmitNotificationView(View):
    """
    This view is meant for submitting notifications to then store in the database
    as well as display on the home page in the notifications.
    """
    def get(self, request):
        return render(request, 'notifications/submit_form.html', {'form': NotificationForm})

    def post(self, request):
        """
        Validate the form data the sniffing program sent in & save to the database.
        """

        # Grab the attacks that are currently being detected
        attacks = Attack.objects.filter(detection=True).values_list('name', flat=True)

        # Adds the POST data to the NotificationForm for validation testing
        form = NotificationForm(request.POST)

        # Checks if the form is valid
        if form.is_valid():
            notification = form.save(commit=False)

            # Checks if the Notification being sent in involves an Attack that is currently
            # being detected; if not, the Notification is essentially discarded.
            if notification.attack in attacks:
                notification.save()
                return HttpResponse('<p>Successfully added form.</p>')
            else:
                return HttpResponse('<p>Failed to save form; the attack: "{}" is currently set to not be detected.</p>'.format(notification.attack))

        # If the form wasn't able to validate the POST request at all
        else:
            return HttpResponse('<p>An error has occured with the POST data sent; the form wasn\'t able to validate \
                                 the form data.</p>')
