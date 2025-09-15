total_packages = 0
total_items = 0
total_weight = 0
unused_capacity = 0
max_items_in_a_package = 0
heaviest_package_number = 0

current_package_weight = 0
current_package_items = 0

while True:
    try:
        weight = float(input("What is weight?"))
    except ValueError:
        print("Enter valid number")
        continue

    if weight == 0:
        if current_package_items > 0:
            total_packages += 1
            unused_capacity += 20 - current_package_weight
            if current_package_items > max_items_in_a_package:
                max_items_in_a_package = current_package_items
                heaviest_package_number = total_packages
        break

    if weight < 0 or weight > 10:
        print("Enter valid number")
        continue

    if current_package_items == 5 or current_package_weight + weight > 20:
        total_packages += 1
        unused_capacity += 20 - current_package_weight
        if current_package_items > max_items_in_a_package:
            max_items_in_a_package = current_package_items
            heaviest_package_number = total_packages

        current_package_items = 0
        current_package_weight = 0

    current_package_weight += weight
    current_package_items += 1
    total_items += 1
    total_weight += weight


print("Total packages is: {}".format(total_packages))
print("Total items is: {}".format(total_items))
print("Total weight is: {}".format(total_weight))
print("Unused packages is: {}".format(unused_capacity))
print("Maximum items is: {}".format(heaviest_package_number))
