from django.contrib import admin
from .models import Board, Task


# ---- new ----
admin.site.register(Board)
admin.site.register(Task)
# ---- end new ----