from django.contrib import admin

# Register your models here.

from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')


admin.site.register(Job, JobAdmin)