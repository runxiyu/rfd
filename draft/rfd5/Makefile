git: update
	git add .
	git commit
	git push
update: rfd5.txt

rfd5.txt: rfd5.xml
	xml2rfc --text rfd5.xml
	sed -i -e '/\f/{n;s/^...../RFD RFDN/}' rfd5.txt
	ed rfd5.txt < Edfile
rfd5.xml: rfd5.md
	sed '0,/title =/{s/ ."$$/"/}' rfd5.md | mmark > rfd5.xml
