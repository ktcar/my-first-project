from price.models import Items
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "priceindector.settings")

Items.objects.all()