from datetime import datetime, timedelta

def add_time(start, duration, start_day=None):
  output_format = "%-I:%M %p"

  # Create base date
  if start_day != None:
    output_format += ', %A'
    d = datetime.strptime("2020 06 " + start_day.lower() + " 1 " + start, "%Y %m %A %U %I:%M %p")
  else:
    d = datetime.strptime(start, "%I:%M %p")

  # Add diff to date
  hour, minute = duration.split(':')
  diff = timedelta(hours=int(hour), minutes=int(minute))
  d2   = d + diff

  # Format output
  diff = d2.replace(hour = 0, minute = 0, second = 0, microsecond = 0) \
          - d.replace(hour = 0, minute = 0, second = 0, microsecond = 0)

  output = d2.strftime(output_format)

  if diff.days == 1:
    output += ' (next day)'
  elif diff.days > 1:
    output += ' (' + str(diff.days) + ' days later)'

  return output