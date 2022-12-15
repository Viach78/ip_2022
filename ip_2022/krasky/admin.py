from django.contrib import admin
from .models import Krasky_vnut
from .models import Krasky_nar
from .models import Krasky_aero
from .models import Krasky_rust

# Register your models here.

admin.site.register(Krasky_vnut)
admin.site.register(Krasky_nar)
admin.site.register(Krasky_aero)
admin.site.register(Krasky_rust)
