# NUMBER-TRACE-USING-PYTHON
INSTALL PIP :

<li>pip install requests
<li>pip install phonenumbers
<li>pip install pycountry
<li>pip install folium
<li>pip install geocoder
<li>pip install timezone-converter
<li>pip install carrier

# ETC

<h1> STEP 1 - MANUAL NUMBER </h1>

NUMBER DETAILS MANUALLY CHOSSE !:
```
if a==1:
        number_details1()
```
FUNCTION : 
```
def number_details1():
    import phonenumbers
    import folium
    from mynumber import number
    from phonenumbers import geocoder,timezone,carrier
    

    key ='b72366878ec4414381ce6defa1dec069'
    samnumber = phonenumbers.parse(number)
    print(samnumber)
    yourlocation = geocoder.description_for_number(samnumber,"en")
    print("Country Name : ",yourlocation)

    time= timezone.time_zones_for_number(samnumber)
    print("Zone :", time)

    #get service provider

    service_provider = phonenumbers.parse(number)
    print("Operator : ",carrier.name_for_number(service_provider,"en"))

    from opencage.geocoder import OpenCageGeocode
    geocoder = OpenCageGeocode(key)

    query=str(yourlocation)
    result=geocoder.geocode(query)
    #print(result)

    lat=result[0]['geometry']['lat']
    lng=result[0]['geometry']['lng']
    print(lat,lng)

    mymap= folium.Map(location=[lat,lng],zoom_start=9)

    folium.Marker([lat,lng],popup=yourlocation).add_to((mymap))

    ##save map on html file
    mymap.save("mylocation.html")
 ```

 ---
<h1> STEP 2 - NUMBER FROM USER </h1>
 
 Function CALL : 
 ```
 elif a==2:
        number_details2()
```
Function :
```
def number_details2():
    
    #track secound
    class Location_Tracker:
        def __init__(self, App):
            self.window = App
            self.window.title("Phone number Tracker")
            self.window.geometry("500x400")
            self.window.configure(bg="#3f5efb")
            self.window.resizable(False, False)
    
            #___________Application menu_____________
            Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
            self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
            self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
            self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
    
            #___________Place widgets on the window______
            self.phone_number.place(x=170, y=120)
            self.track_button.place(x=200, y=200)
            self.country_label.place(x=100, y=280)
    
            #__________Linking button with countries ________
            self.track_button.bind("<Button-1>", self.Track_location)
            #255757294146
        
        def Track_location(self,event):
            phone_number = self.phone_number.get()
            country = "Country is Unknown"
            if phone_number:
                tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
                print(tracked)
                if tracked:
                        if hasattr(tracked, "official_name"):
                            country = tracked.official_name
                        else:
                            country = tracked.name
            self.country_label.configure(text=country)
    
    
    
    PhoneTracker = Tk()
    MyApp = Location_Tracker(PhoneTracker)
    PhoneTracker.mainloop()
```

---
<h1> STEP 3 - IP ADDRESS TRACK</h1>

Function CALL : 
```
elif a==3:
        ip_info()
```
MAIN FUNCTION :
```
def ip_info():
   

    ## single ip request
    response = requests.get("http://ip-api.com/json/24.48.0.1").json()
    #
    print(response['lat'])
    print(response['lon'])

    # batch ip request

    response = requests.post("http://ip-api.com/batch", json=[
    {"query": "103.120.203.180"},
    ]).json()

    for ip_info in response:
        for k,v in ip_info.items():
            print(k,v)
        print("\n")
```

<H1> 3 Type of tracing HERE.