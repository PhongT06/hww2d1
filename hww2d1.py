# #1
# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }

# restaurant_menu["Beverages"] = {"Coke": 2.95, "Sweet_Tea": 2.95}
# restaurant_menu["Main Course"].update({"Steak": 17.99})
# restaurant_menu["Starters"].pop("Bruschetta")
# print(restaurant_menu)


#2###############################################
# def display_menu():
#     print("\nMenu:")
#     print("1. Book a room")
#     print("2. Check-out a customer")
#     print("3. Display room status")
#     print("4. Quit")

# def book_room(rooms):
#     room_number = input("What room number would you like to book?: ")
#     if room_number in rooms:
#         if rooms[room_number]["status"] == "available":
#             customer_name = input("Enter customer name: ")
#             rooms[room_number]["status"] = "booked"
#             rooms[room_number]["customer"] = customer_name
#             print(f"Room {room_number} booked for {customer_name}.")
#         else:
#             print("Room is already booked. Choose another one.")
#     else:
#         print("Invalid room number! Please try rooms 101 through 105!")

# def check_out(rooms):
#     room_number = input("Enter room number to check-out: ")
#     if room_number in rooms:
#         if rooms[room_number]["status"] == "booked":
#             customer_name = rooms[room_number]["customer"]
#             rooms[room_number]["status"] = "available"
#             rooms[room_number]["customer"] = ""
#             print(f"{customer_name} checked out of room {room_number}.")
#         else:
#             print("Room is already available.")
#     else:
#         print("Invalid room number!")

# def display_room_status(rooms):
#     print("\nRoom Status:")
#     for room_number, details in rooms.items():
#         print(f"Room {room_number}: {details['status']} - {details['customer']}")

# def main():
#     hotel_rooms = {
#         "101": {"status": "available", "customer": ""},
#         "102": {"status": "booked", "customer": "John Doe"},
#         "103": {"status": "booked", "customer": "Jane Doe"},
#         "104": {"status": "available", "customer": ""},
#         "105": {"status": "available", "customer": ""}
#     }
#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-4): ")
#         if choice == "1":
#             book_room(hotel_rooms)
#         elif choice == "2":
#             check_out(hotel_rooms)
#         elif choice == "3":
#             display_room_status(hotel_rooms)
#         elif choice == "4":
#             print("Thank you for choosing Hotel Califonia!")
#             break
#         else:
#             print("Invalid choice! Please choose a number between 1 and 4.")
# main()

#2.2######################################

# products = {
#     "1": {"name": "Laptop", "category": "Electronics", "price": 800},
#     "2": {"name": "Shirt", "category": "Clothing", "price": 20}
# }

# def search_product(products, keyword):
#     matching_products = []
#     for product_id, product_details in products.items():
#         if keyword.lower() in product_details['name'].lower():
#             matching_products.append((product_id, product_details))
#     return matching_products

# def display_matching_products(matching_products):
#     if not matching_products:
#         print("No matching products found.")
#     else:
#         print("Matching Products:")
#         for product_id, product_details in matching_products:
#             print(f"ID: {product_id}, Name: {product_details['name']}, Category: {product_details['category']}, Price: ${product_details['price']}")

# products = {
#     "1": {"name": "Laptop", "category": "Electronics", "price": 800},
#     "2": {"name": "Shirt", "category": "Clothing", "price": 20}
# }
# keyword = input("Enter the name of the product to search: ")
# matching_products = search_product(products, keyword)
# display_matching_products(matching_products)

#3#################################

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# def open_ticket(tickets):
#     ticket_id = input("Enter ticket ID: ")
#     if ticket_id in tickets:
#         print("Ticket ID already exists!")
#         return
#     customer_name = input("Enter customer name: ")
#     issue_description = input("Enter issue description: ")
#     status = "open"
#     tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": status}
#     print("Ticket opened successfully!")

# def update_ticket_status(tickets):
#     ticket_id = input("Enter ticket ID: ")
#     if ticket_id not in tickets:
#         print("Ticket ID not found!")
#         return
#     new_status = input("Enter new status (open/closed): ")
#     if new_status not in ["open", "closed"]:
#         print("Invalid status!")
#         return
#     tickets[ticket_id]["Status"] = new_status
#     print(f"Ticket {ticket_id} status updated to {new_status}.")

# def display_tickets(tickets):
#     print("\nAll Tickets:")
#     for ticket_id, ticket_details in tickets.items():
#         print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}, Status: {ticket_details['Status']}")

# def filter_tickets_by_status(tickets, status):
#     filtered_tickets = {ticket_id: ticket_details for ticket_id, ticket_details in tickets.items() if ticket_details["Status"] == status}
#     if not filtered_tickets:
#         print(f"No tickets with status '{status}' found.")
#     else:
#         print(f"\nTickets with status '{status}':")
#         for ticket_id, ticket_details in filtered_tickets.items():
#             print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}")

# def main():
#     service_tickets = {
#         "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#         "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
#     }

#     while True:
#         print("\nMenu:")
#         print("1. Open a new ticket")
#         print("2. Update ticket status")
#         print("3. Display all tickets")
#         print("4. Filter tickets by status")
#         print("5. Quit")

#         choice = input("Enter your choice (1-5): ")
#         if choice == "1":
#             open_ticket(service_tickets)
#         elif choice == "2":
#             update_ticket_status(service_tickets)
#         elif choice == "3":
#             display_tickets(service_tickets)
#         elif choice == "4":
#             status = input("Enter status to filter (open/closed): ")
#             filter_tickets_by_status(service_tickets, status)
#         elif choice == "5":
#             print("Thank you for using the ticket tracking system!")
#             break
#         else:
#             print("Invalid choice! Please choose a number between 1 and 5.")

# main()


#4###################################

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales = copy.deepcopy(weekly_sales)
copied_sales["Week 2"]["Electronics"] = 18000

print("Original Sales Data:")
print(weekly_sales)
print("\nUpdated Sales Data:")
print(copied_sales)


