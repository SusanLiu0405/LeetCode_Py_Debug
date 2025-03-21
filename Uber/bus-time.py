def time_to_minutes(time_str):
    """Convert a time string (HH:MM) to total minutes."""
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def bus_time(plan, slot):
    """Find the minutes since the last bus departed."""
    current_time = time_to_minutes(slot)
    last_departed = -1  # Initialize as -1 to indicate no bus has departed yet

    # Convert each time in the plan to minutes
    for bus_time_str in plan:
        bus_time = time_to_minutes(bus_time_str)
        if bus_time < current_time:
            last_departed = bus_time
        else:
            break  # Stop checking as buses are sorted in ascending order

    # If no bus has departed yet
    if last_departed == -1:
        return 0

    # Return the difference in minutes since the last departed bus
    return current_time - last_departed

# Example Input
plan = ["12:30", "14:00", "19:55"]
slot = "12:00"  # Traveler arrives too early

# Output the result
print(bus_time(plan, "12:00"))
print(bus_time(plan, "13:00"))
