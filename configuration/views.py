from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from live.models import Product
import math 
import csv
import datetime

#
#for uploading files
#from django.conf import settings
from django.core.files.storage import FileSystemStorage

### Functions ###
#################

# From string mm/dd/yyy to date YYY-MM-DD
def date_conv(date_str):
    if not date_str:
        date_str = '1/1/2999'
    return datetime.datetime.strptime(date_str, '%m/%d/%Y').date()

# Special panda output nan
def nan(value):
    if isinstance(value, str):
        return 0
    return value


# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        # Writing CSV file to the system
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        
        # Reading CSV file
        path = fs.path(name)
        with open(path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # By default is assumed that orders are no active
            Product.objects.all().update(active=0)

            # Go through each order
            for row in csv_reader:
                # # Getting profile ID
                # if not (Profile.objects.filter(item_code=row['ItemCode'])):
                #     profile = Profile(item_code=row['ItemCode'], item_cod_desc=row['ItemCodeDesc'])
                #     print(f"NEW Profile: {row['ItemCode']} {row['ItemCodeDesc']}")
                #     profile.save()
                # profile = Profile.objects.get(item_code=row['ItemCode'])

                if (Product.objects.filter(so_line=row['SO_line'])):
                    # Order is in DB
                    RMANumber = nan(row['RMANumber'])

                    print(f"REGISTERED: {row['SO_line']} {row['CustomerName']} {row['ItemCode']} {row['Exp DATE']} {row['Qty']}")
                    
                    Product.objects.filter(so_line=row['SO_line']).update(so_line=row['SO_line'], customer_no=row['CustomerNo'], sales_order_no=row['SalesOrderNo'], customer_name=row['CustomerName'], linekey=row['LineKey'], item_code=row['ItemCode'], item_cod_desc=row['ItemCodeDesc'], so_header=date_conv(row['SO Header']), prom_date=date_conv(row['PROM DATE']), clear_date=date_conv(row['UDF_MATERIALS_CLEAR_DATE']), exp_date_i=date_conv(row['EXP DATE']), exp_date_f=date_conv(row['Exp DATE']), qty=row['Qty'], qty_shipped=row['QuantityShipped'], unit_price=row['UnitPrice'], production_notes=row['Production Notes'], qty_on_hand=row['QtyOnHand'], rma_number=RMANumber, drop_ship=row['DropShip'], comments=row['Comments'], active=1)

                else:
                    # New order is going into the system
                    RMANumber = nan(row['RMANumber'])
                    
                    print(f"NEW: {row['SO_line']} {row['CustomerName']} {row['ItemCode']} {row['Exp DATE']} {row['Qty']}")
                    
                    order = Product(so_line=row['SO_line'], customer_no=row['CustomerNo'], sales_order_no=row['SalesOrderNo'], customer_name=row['CustomerName'], linekey=row['LineKey'], item_code=row['ItemCode'], item_cod_desc=row['ItemCodeDesc'], so_header=date_conv(row['SO Header']), prom_date=date_conv(row['PROM DATE']), clear_date=date_conv(row['UDF_MATERIALS_CLEAR_DATE']), exp_date_i=date_conv(row['EXP DATE']), exp_date_f=date_conv(row['Exp DATE']), qty=row['Qty'], qty_shipped=row['QuantityShipped'], unit_price=row['UnitPrice'], production_notes=row['Production Notes'], qty_on_hand=row['QtyOnHand'], rma_number=RMANumber, drop_ship=row['DropShip'], comments=row['Comments'])
                    
                    # status = Status.objects.get(name="NEW")
                    order.save()

                    # For the future. It will be used log table
                    #log = Log(product_id = order, status_id = status, date = datetime.datetime.today().strftime('%Y-%m-%d'))
                    #log.save()

    return render(request, 'configuration/index.html')