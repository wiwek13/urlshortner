import random
import string
from django.conf import settings
SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)



# from shortner.models import WirrURL
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Wclass = instance.__class__
    qs = Wclass.objects.filter(shortcode=new_code).exists()
    if qs:
        return create_shortcode(size=size)

    return new_code