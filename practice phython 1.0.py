event_name= input("what was the name of the venue? ")

cost = float(input("What is the bill? "))

service_charge = float(input("How much did u tip  in % ? ").strip().replace("%", ""))
service_charge = (service_charge / 100) * cost 
group_size = int(input("how many people where u with on the bill? ")) 

grand_total= float(cost) + float(service_charge)
total_per_person = float(grand_total) // float(group_size)


print("welcome to PayUp")
print()
print(f"here's the break down for dinner at: {event_name}")
print()
print(type((f"cost: ${cost}")))
print(type(f"service charge: ${service_charge}"))
print(f"group size: {group_size}")
print(type(f"grand total:${grand_total:.2f}"))
 
print()
print((f"each person must PayUp: ${total_per_person:.2f}"))
print(type((f"each person must PayUp: ${total_per_person:.2f}")))