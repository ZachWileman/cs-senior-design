from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import NotificationForm


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

        form = NotificationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<p>Successfully added form.</p>')

        else:
            return HttpResponse('<p>An error has occured with the POST data sent; the form wasn\'t able to validate \
                                 the form data.</p>')
