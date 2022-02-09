# ical2google
Import ics files into Google Calendar.

## Usage
*ical2google* takes a path to an *ics* file, parses it, and then outputs a URL that takes you to the "Create Event" screen in Google Calendar. There you can simply click "Save". You can also make changes to the event before saving.
```
ical2google <ics-file-name>
```

## Dependencies
Inside `requirements.txt`.

## Caveats
- Currently only supports some of the event info (with links to the iCalendar RFC):
  - summary via [`SUMMARY`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.12)
  - description via [`DESCRIPTION`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.5)
  - location via [`LOCATION`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.7)
  - start/end date via [`DTSTART`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.2.4)
  and [`DTEND`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.2.2)
- Only parses the first event of the *ics* file
