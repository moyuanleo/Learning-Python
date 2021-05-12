dic_country={'China':'Beijing','America':'Washington','Norway':'Oslo',
'Japan':'Tokyo','Germany':'Berlin','Canada':'Ottawa','France':'Paris',
'Thailand':'Bangkok'}
country=input()
country=country.capitalize()
if country in dic_country:
    capital=dic_country.get(country)
    print(capital)
else:
    print("未查询到该国家名！")