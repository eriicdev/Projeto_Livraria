from django.shortcuts import redirect
from django.views import View


class HomeView(View):
    def get(self, request):
        return redirect("http://localhost:8080/")
