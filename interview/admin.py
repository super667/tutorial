from django.contrib import admin
from jobs.models import Resume
from django.utils.safestring import mark_safe
from interview import candidate_field as cf

# Register your models here.
from interview.models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    
    list_display = (
        'username', 'city', 'bachelor_school','get_resume', 'first_score', 'first_result', 'first_interviewer_user', 'second_score',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',)

    list_filter = ('city','first_result','second_result','hr_result','first_interviewer_user','second_interviewer_user','hr_interviewer_user')

    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    ### 列表页排序字段
    ordering = ('hr_result','second_result','first_result',)

    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names and obj.first_interviewer_user == request.user:   # type: ignore
            return cf.default_fieldsets_first

        if 'interviewer' in group_names and obj.second_interviewer_user == request.user:  # type: ignore
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    
    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names



    def get_resume(self, obj):
        if not obj.phone:
            return ""

        resumes = Resume.objects.filter(phone=obj.phone)
        if resumes and len(resumes) > 0:
            return mark_safe(u'<a href="/resume/%s"target ="_blank">%s</a' % (resumes[0].id, "查看简历"))
        return ""

    get_resume.short_description = '查看简历'
    get_resume.allow_tags = True
        

admin.site.register(Candidate, CandidateAdmin)