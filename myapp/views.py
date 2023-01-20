from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from myapp import support_functions
# from myapp.models import Currency
from django.template.loader import get_template
from bs4 import BeautifulSoup
from django.shortcuts import render
from myapp.models import User, Attribute, AccountHolder
import folium


# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data["time_of_day"] = time
    return render(request, "home.html", context=data)


# from django.http import HttpResponseRedirect
# from django.urls import reverse
def maintenance(request):
    data = dict()
    # try:
    #     choice = request.GET['selection']
    #     if choice == "currencies":
    #         support_functions.add_currencies(support_functions.get_currency_list())
    #         c_list = Currency.objects.all()
    #         print("Got c_list",len(c_list))
    #         data['currencies'] = c_list
    #         return HttpResponseRedirect(reverse('currencies'))
    # except:
    #     pass
    return render(request, "maintenance.html", context=data)


def match(request):
    template = get_template('home.html')
    html = template.render({'key': 'value'})
    soup = BeautifulSoup(html, 'html.parser')

    dropdown = soup.find(id="partner_attribute")
    selected_option = dropdown.find("option", selected=True)
    match_attribute = selected_option["value"]

    data = dict()
    try:
        rows = User.objects.filter(self_attribute=match_attribute)
        match_results = list(rows)
        first_result = match_results[0]
        second_result = match_results[-1]

        data['first_result'] = first_result
        data['second_result'] = second_result
    except:
        pass
    return render(request, "match.html", context=data)


def view_attributes(request):
    data = dict()
    a_list = Attribute.objects.all()
    data['attributes'] = a_list
    return render(request, 'home.html', context=data)


def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user, date_of_birth=dob)
        acct_holder.save()
        return render(request, "home.html", context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, "registration/register.html", context)


def map(request):
    data = dict()
    m = folium.Map()
    # activate the reset button
    try:
        request.GET['reset']
        print("resetting")
        data['number_of_cities'] = 0
        data['m'] = m._repr_html_
        return render(request, "map.html", context=data)
    except:
        pass
    # create the markers
    try:
        request.GET['city_list']
        number_of_cities = int(request.GET['number_of_cities'])
        visiting_cities = list()
        for i in range(number_of_cities):
            name = "city" + str(i + 1)
            city_name = request.GET[name]
            visiting_cities.append(city_name)
        m = support_functions.add_markers(m, visiting_cities)
        data['visiting_cities'] = visiting_cities
        print('here')
        m = m._repr_html_
        data['m'] = m
        return render(request, "map.html", data)
    except:
        pass
    # get city names and number of city code
    try:
        number_of_cities = int(request.GET["number_of_cities"])
        if number_of_cities > 0:
            names = list()
            for i in range(number_of_cities):
                names.append("city" + str(i + 1))
            data['names'] = names
            data['number_of_cities'] = number_of_cities
        m = m._repr_html_
        data['m'] = m
    except:
        data['number_of_cities'] = 0
        m = m._repr_html_
        data['m'] = m
    return render(request, "map.html", context=data)


def match(request):
    data = dict()
    try:
        match_attribute = request.GET['partner_attribute']
        m = User.objects.filter(self_attribute=match_attribute)
        data['first_result'] = m[0]
        data['second_result'] = m[1]
    except:
        pass
    return render(request, "match.html", data)
