#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "$0 <firefox-profile-path>"
fi

key="${1%/}/key4.db"
if [[ ! -f "$key" ]]; then
    echo "Cannot find key file, exiting"
    exit 1
fi 

logins="${1%/}/logins.json"
if [[ ! -f "$logins" ]]; then
    echo "Cannot find logins file, exiting"
    exit 1
fi

prefs="${1%/}/prefs.js"
if [[ ! -f "$prefs" ]]; then
    echo "Cannot find prefs file, exiting"
    exit 1
fi

timestamp=$(date +%Y-%m-%d_%H%M)

/bin/tar cJf "firefox-settings-$timestamp.tar.xz" -C "$1" key4.db logins.json prefs.js
