from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# MARK: HOME
@login_required
def home(request):
    if request.user.is_superuser:

        return render(
            request,
            "pages/home.html",
        )


# MARK: ABOUT
@login_required
def about(request):
    return render(request, "pages/about.html", {})
