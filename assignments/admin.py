from django.contrib import admin

from assignments.models import About, SocialLink

# użytkownik nie moze dodac nowego obiektu jesli istnieje juz jeden
# dlatego trzeba nadpisać metode has_add_permission
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        
        count = About.objects.all().count() # zwraca liczbe obiektow
        if count == 0:
            return True
        return False

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
