import time
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from ...script  import test_scheduler
from pytz import timezone

class Command(BaseCommand):
    help = 'Testing scheduler'

    #def add_arguments(self, parser):
        #parser.add_argument('date_start_object', nargs='+', type=str)
        #parser.add_argument('date_end_object', nargs='+', type=str)

    def handle(self, *args, **options):
        
        test_scheduler()