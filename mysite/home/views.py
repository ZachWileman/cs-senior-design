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
            {'mac_address': 'MM:MM:MM:SS:SS:SS',
            'notifications': [
                {'date_created': 'some date', 'description': 'this is the description'},
                {'date_created': 'another date', 'description': 'another one'}]
            },
            {'mac_address': 'AA:AA:AA:BB:BB:BB',
            'notifications': [
                {'date_created': '12345', 'description': 'this is the description'},
                {'date_created': '67891', 'description': 'another one'}]
            },
        ]

        """
        # Grab the collection of notifications from the database
        all_notifications = Notification.objects.all()

        devices = []

        # Create a list of devices using each of the mac addresses
        for notification in all_notifications:
            if notification.mac_address not in [device['mac_address'] for device in devices]:
                devices.append({'mac_address': notification.mac_address, 'notifications': []})

        # Add the notifications to their respective device
        for notification in all_notifications:
            for device in devices:
                if notification.mac_address == device['mac_address']:
                    device['notifications'].append({'description': notification.description, 'date_created': notification.date_created})

        # Sort the notifications under each device by date_created
        for device in devices:
            device['notifications'] = sorted(device['notifications'], key=lambda k: k['date_created'], reverse=True)

        return render(request, 'home/home.html', {'devices': devices})
