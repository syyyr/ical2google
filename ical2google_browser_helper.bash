#!/bin/bash
xdg-open "$(python "$(dirname $BASH_SOURCE)/ical2google.py" "$1")"
