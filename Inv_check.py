web_inv = {
    112365: 3,
    112654: 0,
    112398: 6 ,
    112547: 0,
    112578: 25,
    112336: 12,
}

store_inv = {
    114587: 1,
    112578: 1,
    112547: 2,
    112336: 1,
    114558: 3,
    115789: 0,
    118798: 1,
    112654: 5,
    115478: 2,
    114574: 0,
    112398: 1,
    117895: 1,
    114789: 2,
    117895: 1,
    114785: 1,
    112365: 3,
    116454: 0,
    117895: 2,
    116789: 1,
    
}

def check_inv(web_inv, store_inv):
    for web_sku in web_inv:
        for store_sku in store_inv:
            if web_sku == store_sku:
                if web_inv[web_sku] != store_inv[store_sku]:
                    print(f"Sku #", web_sku, " was corrected from an inventory of ", web_inv[web_sku], "to an inventory of ", store_inv[store_sku])
                    web_inv[web_sku] = store_inv[store_sku]
                    


check_inv(web_inv, store_inv)