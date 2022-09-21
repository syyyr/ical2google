import icalendar as ical
import urllib.parse
import sys
import pprint

def encode_string(url_str):
    return urllib.parse.quote_plus(url_str)


if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <file-name>')
    exit(1)

file_name = sys.argv[1]

try:
    text_file = open(file_name, "r")
except FileNotFoundError:
    print(f"File '{file_name}' doesn't exist")
    exit(1)


data = text_file.read()
calendar = ical.Calendar.from_ical(data)

url = 'https://calendar.google.com/calendar/u/0/r/eventedit?'

for e in calendar.walk():
    if isinstance(e, ical.Event):
        event = e
        break
else:
    print('The ics file contained no events')
    exit(1)

query = f'text={encode_string(event.get("SUMMARY"))}'

if event.has_key('LOCATION'):
    query = f'{query}&location={encode_string(event.get("LOCATION"))}'

if event.has_key('DESCRIPTION'):
    query = f'{query}&details={encode_string(event.get("DESCRIPTION"))}'

if event.has_key('DTSTART'):
    start = event.get('DTSTART')
    end = event.get('DTEND')
    query = f'${query}&dates={encode_string(start.to_ical())}/{encode_string(end.to_ical())}'

url = f'{url}{query}'
print(url)


