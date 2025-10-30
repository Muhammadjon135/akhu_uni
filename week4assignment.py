def calculate_room_revenue(room_type, nights_booked, season):
    if room_type == "suite":
        if season == "low":
            total_revenue = nights_booked*150
        elif season == "regular":
            total_revenue = nights_booked*225
        else:
            total_revenue = nights_booked*350
    elif room_type == "deluxe":
        if season == "low":
            total_revenue = nights_booked*100
        elif season == "regular":
            total_revenue = nights_booked*160
        else:
            total_revenue = nights_booked*240
    else:
        if season == "low":
            total_revenue = nights_booked*60
        elif season == "regular":
            total_revenue = nights_booked*95
        else:
            total_revenue = nights_booked*140
    return total_revenue
print(calculate_room_revenue("deluxe", 2, "low"))
