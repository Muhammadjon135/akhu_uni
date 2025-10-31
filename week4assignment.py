print("\nHOTEL BOOKING ANALYTICS")
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


def define_the_level_factor(level):
    if level == "Under Capacity":
        num = 0.5
    elif level == "Fair Occupancy":
        num = 1.0
    elif level == "Good Occupancy":
        num = 1.2
    elif level == "Excellent Occupancy":
        num = 1.5
    else:
        num = 1.8
    return num


def calculate_booking_rate(hotel_years, baseline_rooms, booked_rooms):
    expected_bookings = 1000 + (hotel_years * 100)
    room_capacity = expected_bookings - baseline_rooms
    return (booked_rooms - baseline_rooms) / room_capacity * 100


def determine_occupancy_level(booking_percent):
    if booking_percent < 50:
        capacity_status = "Under Capacity"
    elif 50 <= booking_percent < 60:
        capacity_status = "Fair Occupancy"
    elif 60 <= booking_percent < 70:
        capacity_status = "Good Occupancy"
    elif 70 <= booking_percent < 85:
        capacity_status = "Excellent Occupancy"
    else:
        capacity_status = "Full Capacity"
    return capacity_status


def calculate_net_income(revenue, nights, level_factor):
    base_income = revenue * 0.05 + nights * 2
    return round(base_income * level_factor, 1)


def needs_discount_offer(operating_days, total_nights, avg_booking):
    if operating_days >= 6 and avg_booking < 50:
        return True
    if total_nights < 100 and avg_booking < 60:
        return True
    if operating_days >= 4 and avg_booking < 40:
        return True
    return False


def generate_booking_analysis(guest_name, room_type, nights, season, hotel_years, baseline_rooms, booked_rooms, operating_days):
    room_revenue = calculate_room_revenue(room_type, nights, season)
    booking_rate = calculate_booking_rate(hotel_years, baseline_rooms, booked_rooms)
    level = determine_occupancy_level(booking_rate)
    level_factor = define_the_level_factor(level)
    net_income = calculate_net_income(room_revenue, nights, level_factor)
    is_discount = needs_discount_offer(operating_days, nights, booking_rate)
    print("="*40)
    print(f"Booking Analysis for: {guest_name}")
    print("-"*40)
    print(f"Room Type: {room_type}")
    print(f"Nights Booked: {nights}")
    print(f"Season: {season}")
    print(f"Room Revenue: ${room_revenue}")
    print("Booking Analysis:")
    print(f"  Experience: {hotel_years} years, Baseline: {baseline_rooms}, Booked Rooms: {booked_rooms}")
    print(f"  Booking Rate: {booking_rate:.1f}%")
    print(f"  Occupancy Level: {level}")
    print(f"Net Income: ${net_income}")
    print(f"Operating Days: {operating_days}\nDiscount Offer Needed: {'Yes' if is_discount else 'No'}\n")


generate_booking_analysis("Harrison", "suite", 45, "peak", 3, 800, 1150, 3)
generate_booking_analysis("Madison", "deluxe", 60, "regular", 5, 900, 1300, 5)
generate_booking_analysis("Logan", "standard", 30, "low", 8, 850, 950, 7)
