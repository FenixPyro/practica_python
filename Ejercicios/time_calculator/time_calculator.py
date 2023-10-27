def add_time(start, duration, current_day=None):
    start_time, start_txt = start.split()
    duration_hour, duration_minutes = map(int, duration.split(":"))
    start_hour, start_minutes = map(int, start_time.split(":"))
    if start_txt == "PM":
      start_hour += 12
    total_minutes = (start_hour * 60 + start_minutes + duration_hour * 60 + duration_minutes)
    new_hour = total_minutes // 60 % 24
    new_minutes = total_minutes % 60
    new_text = "AM" if new_hour < 12 else "PM"
    new_hour %= 12
    if new_hour == 0:
      new_hour = 12
    days_later = total_minutes // 1440
    if current_day:
      current_day = current_day.capitalize()
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_day_index = days_of_week.index(current_day)
      new_day_index = (start_day_index + days_later) % 7
      new_day = days_of_week[new_day_index]
      result = f"{new_hour}:{new_minutes:02} {new_text}, {new_day}"
    else:
        result = f"{new_hour}:{new_minutes:02} {new_text}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    return result