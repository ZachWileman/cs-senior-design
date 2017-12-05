from django.shortcuts import render
from django.views import View

from notifications.models import Notification

class HomeView(View):
    """
    Class used to display the home page; which should display the Notifications for each of the devices on the network.
    """

    def get(self, request):
        """
        This will display to the user the homepage/notifications. Should look something like this:

        devices = [
            {'dest_address': 'MM:MM:MM:SS:SS:SS',
            'notifications': [
                {'date_created': 'some date', 'attack': 'SYN Flood Attack', 'threat_level': 'Severe', 'source_address': '190.123.123.123'},
                {'date_created': 'another date', 'attack': 'Christmas Tree Attack', 'threat_level': 'Moderate', 'source_address': None}]
            },
        ]
        """
        # Grab the collection of notifications from the database
        all_notifications = Notification.objects.all()

        return render(request, 'home/home.html', {'notifications': all_notifications})
