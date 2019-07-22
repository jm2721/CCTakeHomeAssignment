from django.shortcuts import render
from django.http import HttpResponse 
from .models import Vendor, Product

def index(request):
    context = {}
    try:
        barcode = request.POST['barcode']

        if not validateBarcode(barcode):
            context['error_message'] = "Invalid barcode"
            return render(request, 'barcodeScanner/index.html', context)

        context['scanned_barcode'] = barcode
        
        if len(barcode) == 13 and barcode[0] == '0':
            barcode = barcode[1:]
       
        vId = str(getVendorId(barcode))
        pluCode = str(getPLU(barcode))
        weight = str(getWeight(barcode))
        
        vendors = Vendor.objects.filter(vendorId=vId)
        products = Product.objects.filter(plu=pluCode)
        # We're assuming only one vendor and product gets returned because these are both primary key fields.
        if len(vendors) != 0:
            vendor = vendors[0]
        else:
            vendor = "Could not find vendor in database!"

        if len(products) != 0:
            product = products[0]
        else:
            product = "Could not find product in database!"
            
        context['vendor'] = vendor
        context['product'] = product
        context['vendor_id'] = vId 
        context['plu'] = pluCode
        context['weight'] = weight 
    except (KeyError):
        context['error_message'] = "No data was passed in"
    
    return render(request, 'barcodeScanner/index.html', context)

def validateBarcode(barcode):
    if len(barcode) == 13 and barcode[0] != '0':
        return False
    return True

def getVendorId(barcode):
    return barcode[0:3]

def getPLU(barcode):
    return barcode[3:6]

def getWeight(barcode):
    # Put the decimal point
    weight = barcode[7:11]
    return weight[0:-2] + '.' + weight[-2:]

