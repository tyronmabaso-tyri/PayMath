event_name = input("what was the name of the venue? ")

cost = float(input("What is the bill? "))

service_charge = input("How much did u tip in % ? ")
service_charge = service_charge.strip().replace("%", "")
service_charge = float(service_charge)
service_charge = (service_charge / 100) * cost
group_size = int(input("how many people where u with on the bill? "))

grand_total = float(cost) + float(service_charge)

split_type = input("do u wanna split evenly or unevenly? (type 'even' or 'uneven') ")

print("welcome to PayUp")
print()
print(f"here's the break down for dinner at: {event_name}")
print()
print(f"cost: ${cost:.2f}")
print(f"service charge: ${service_charge:.2f}")
print(f"group size: {group_size}")
print(f"grand total:${grand_total:.2f}")
print()

if split_type == "uneven":
    total_check = 0
    for person in range(1, group_size + 1):
        share = float(input(f"how much of the grand total does person {person} owe? $"))
        print(f"person {person} must PayUp: ${share:.2f}")
        total_check = total_check + share
    print()
    print(f"total collected: ${total_check:.2f}")
else:
    total_per_person = grand_total / group_size
    print(f"each person must PayUp: ${total_per_person:.2f}")