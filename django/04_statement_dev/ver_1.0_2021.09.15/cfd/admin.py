from django.contrib import admin

from cfd.models import Statement, Deposit, Withdrawal, Notesdb, Buy_calc, Quarter, Pipmargin

admin.site.register(Statement)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Notesdb)
admin.site.register(Buy_calc)
admin.site.register(Quarter)
admin.site.register(Pipmargin)