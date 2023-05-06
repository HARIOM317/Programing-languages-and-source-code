import phonenumbers
from phonenumbers import timezone, geocoder, carrier
MobileNumber = input("Enter Mobile Number (With + Country Code) :  ")
Number = phonenumbers.parse(MobileNumber)
Zone = timezone.time_zones_for_number(Number)
car = carrier.name_for_number(Number, "en")
Reg = geocoder.description_for_number(Number, "en")

print("Phone Number:  ", Number)
print("Time Zone:  ", Zone)
print("Carrier:  ", car)
print("Registration:  ", Reg)
