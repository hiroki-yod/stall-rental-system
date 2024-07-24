from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class GroupListView(LoginRequiredMixin, View):
    template_name = "list.html"

    def get(self, request):
        user_groups = request.user.member_groups.all()
        context = {
            "groups": user_groups
        }
        return render(request, self.template_name, context)
