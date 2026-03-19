from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .dynamodb import table

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        table.put_item(
            Item={
                "email": data['email'],
                "name": data['name'],
                "password": data['password']
            }
        )
        return redirect("login")

    return render(request, "register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        response = table.get_item(Key={"email": data['email']})
        user = response.get("Item")

        if user and user["password"] == data["password"]:
            return redirect("dashboard")

    return render(request, "login.html", {"form": form})


def dashboard(request):
    return render(request, "dashboard.html")
