git: update
	git add .
	git commit
	git push
update: rfd4.txt

rfd4.txt: rfd4.xml
	xml2rfc --text rfd4.xml
	sed -i -e '/\f/{n;s/^...../RFD 4/}' rfd4.txt
	ed rfd4.txt < Edfile
rfd4.xml: rfd4.md
	sed '0,/title =/{s/ ."$$/"/}' rfd4.md | mmark > rfd4.xml
