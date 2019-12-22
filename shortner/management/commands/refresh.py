from django.core.management.base import BaseCommand, CommandError
from shortner.models import WirrURL

class Command(BaseCommand):
    help = 'refresh the shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('item', type=int)

    def handle(self, *args, **options):
 #  raise CommandError('Poll "%s" does not exist' % poll_id)
       return WirrURL.objects.refresh_shortcodes(item=options['item'])

