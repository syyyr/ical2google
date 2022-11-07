#!/bin/bash
xdg-open "$(python "$(dirname "${BASH_SOURCE[0]}")/ical2google.py" "$1")"
