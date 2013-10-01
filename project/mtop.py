# go through every mongo studio, create studio, galleries and images
from django.core.management.base import BaseCommand, CommandError
from example.polls.models import Poll

class Command(BaseCommand):
  args = '<poll_id poll_id ...>'
  help = 'Closes the specified poll for voting'

  def handle(self, *args, **options):
    for poll_id in args:
      try:
        poll = Poll.objects.get(pk=int(poll_id))
      except Poll.DoesNotExist:
        raise CommandError('Poll "%s" does not exist' % poll_id)

      poll.opened = False
      poll.save()

      self.stdout.write('Successfully closed poll "%s"\n' % poll_id)