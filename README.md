# ical2google
Import ics files into Google Calendar.

## Motivation
Facebook is able to export events either to your email (which never worked for me), or as an `.ics` file. I don't use a
desktop calendar application, I only use *Google Calendar*, so simply opening the `.ics` didn't work for me. *ical2google*
tries to solve this issue.

## Usage
*ical2google* takes a path to an *.ics* file, parses it, and then outputs a URL that takes you to the "Create Event"
screen in Google Calendar. There you can simply click "Save". You can also make changes to the event before saving.
```
ical2google <ics-file-name>
```
The repository includes two helper files:
- `ical2google_browser_helper.bash`, that runs the script and opens the output with xdg-open. This will hopefully open a
  browser window with the URL. The helper looks for the Python script inside its directory.
- `ical2google.desktop`, a .desktop file, that runs the browser helper. The path to the helper script **be sure to change
  it!**

`ical2google.desktop` should be put inside `~/.local/share/applications`. **Make sure to point the path to
`ical2google.desktop` to the helper (`ical2google_browser_helper.bash`).** After that, you should use this command:
```bash
xdg-mime default ical2google.desktop text/calendar
```
to register *ical2google* as the handler for `.ics` files. *Note: your DE might use something else than xdg-open (e.g.
exo-open), so be sure to use whatever your setup uses*.
Then you should be able to open `.ics` files in *Google Calendar* via your browser.

## Dependencies
Inside `requirements.txt`. But basically, it's just the `icalendar` Python module.

## Caveats
- Currently only supports some of the event info (links are to the iCalendar RFC):
  - summary via [`SUMMARY`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.12)
  - description via [`DESCRIPTION`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.5)
  - location via [`LOCATION`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.1.7)
  - start/end date via [`DTSTART`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.2.4)
  and [`DTEND`](https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.2.2)
- Only parses the first event of the *.ics* file
