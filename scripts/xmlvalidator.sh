#!/usr/bin/env python3

find -type f -iname "*.xml" | \
while read xml_file_name
do
	if ! python3 xmlvalidator.py "$xml_file_name"
	then
		echo "Warnung: $xml_file_name hat die Prüfung durch csvlint nicht bestanden."
		exit 1
	fi
done

