(sed 's/FILENAME/'"$FILENAME"'/g' << EOF
update: FILENAME.txt FILENAME.7 FILENAME.html
	git add .
	git commit
	git push

FILENAME.7: FILENAME.md
	mmark --man FILENAME.md > FILENAME.7
FILENAME.txt FILENAME.html: FILENAME.xml
	xml2rfc --text --html FILENAME.xml
	sed -i -e '/\f/{n;s/^./RFD 1/}' FILENAME.txt
	ed FILENAME.txt < Edfile
FILENAME.xml: FILENAME.md
	sed '0,/title =/{s/ ."\$\$/"/}' FILENAME.md | mmark > FILENAME.xml
EOF
)
