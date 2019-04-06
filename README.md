# Collection of scripts
Contains scripts for various file operations, reading data from sensor and ansible scripts.

## Scripts

### convert-movike-mkv
Converts video files to mkv files, then setting the same timestamps as the original file before deleting it.

### delete_duplicate_movies
Delete movie files with identical names, except for extension. Use programs like fSlint instead!

### firefox-backup
Saves **only** firefox passwods, nothing more from the profile folder

### link-files-to-single-directory
Link all files in a file tree into a single folder, with basic name coalition handling

### merge_convert_avi
Merge multiple avi files into a single avi file using avimerge, with the option to convert it to mkv.

### temperature-read
Simple script for fetching information from a DS18B20 Temperature Sensor, verifying if the data is correct by CRC
and store the temperature if it's valid. The storage is done to a supplied csv file. The values stored in the csv file
is date, temperature and temperature error range.

## ansible
Roles for configuring both client and server for reverse ssh, useful to get access to a host behind a firewall.