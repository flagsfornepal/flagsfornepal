from flags.models import Flag

for flag in Flag.objects.all():
    if flag.image:
        flag.make_thumbnail()
