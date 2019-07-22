from barcodeScanner.models import Vendor, Product

# To use this method open a Django shell (so all dependencies are present)
# and run this method.
def generateDummyData():
    for p in Product.objects.all():
        p.delete()
    for v in Vendor.objects.all():
        v.delete()
    
    products = """
            Ground Beef:493:4.99:1.02|
            Ground Pork:456:6.99:2.02|
            Wagyu Beef:468:10.89:0.5|
            Ribeye Steak:357:8.99:1.0
        """
    vendors = """
            Hutterian Farm:123|
            Icebox Flats Farm:345|
            Made Up Farm:678
        """
    
    for product in products.split('|'):
        fields = product.split(':')
        p = Product.objects.create(name=fields[0], plu=fields[1], price=fields[2], weight=fields[3])
    
    for vendor in vendors.split('|'):
        fields = vendor.split(':')
        v = Vendor.objects.create(name=fields[0], vendorId=fields[1])
