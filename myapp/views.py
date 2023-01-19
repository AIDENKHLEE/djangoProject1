from django.shortcuts import render
from myapp import support_functions
# from myapp.models import Currency
from django.template.loader import get_template
from bs4 import BeautifulSoup
from django.shortcuts import render
from myapp.models import User, Attribute


# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data["time_of_day"] = time
    return render(request,"home.html", context=data)

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
    return render(request,"maintenance.html",context=data)

def match(request):
    template = get_template('home.html')
    html = template.render({'key': 'value'})
    soup = BeautifulSoup(html, 'html.parser')

    dropdown = soup.find(id = "partner_attribute")
    selected_option = dropdown.find("option", selected=True)
    match_attribute = selected_option["value"]

    data=dict()
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
    data=dict()
    a_list = ["honesty", 'intelligent']
    data['attributes'] = a_list
    return render(request, 'home.html',data)