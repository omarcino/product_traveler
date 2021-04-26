from django.shortcuts import render
from live.models import Product
from django.db.models import Q
import re

# Append list items to a list
def append_lsts(lst_out, lst_in):
    for x in lst_in:
        lst_out.append(x)
    return lst_out

def index(request):
    # Profiles by GET method
    locations = request.GET
    profiles = []
    for l in locations:
        if l == 'qa':
            qa_lst = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5']
            profiles = append_lsts(profiles, qa_lst)
        elif l == 'fct':
            fct_lst = ['p1', 'p2', 'p3']
            profiles = append_lsts(profiles, fct_lst)
        elif l == 'burnin':
            burnin_lst = ['p2', 'p3', 'p4', 'p5']
            profiles = append_lsts(profiles, burnin_lst)
        elif l == 'production':
            production_lst = ['p3', 'p4']
            profiles = append_lsts(profiles, production_lst)
        elif l == 'onhold':
            onhold_lst = ['p98']
            profiles = append_lsts(profiles, onhold_lst)
        else:
            for i in range(100):
                x = i
                x = ('p' + str(x))
                profiles.append(x)

    profiles = list(set(profiles))
    print(profiles)

    profiles_selected = Product.objects.filter(profile__in=profiles).exclude(active=0)
    for p in profiles_selected:
        # customer_name = re.search('^[a-zA-Z0-9]+ .{4}', p.customer_name, flags=re.IGNORECASE)
        customer_name = re.search('^[a-zA-Z0-9]+ ', p.customer_name, flags=re.IGNORECASE)
        if customer_name:
            p.customer_name = customer_name.group()
        print(f"{p.sales_order_no} {p.customer_name} {p.item_code} {p.item_cod_desc} {p.exp_date_f} {p.qty} {p.comments}")

    # Selecting all orders that belongs to the profiles
    

    return render(request, 'live/index.html', {
        "ps": profiles_selected
    })