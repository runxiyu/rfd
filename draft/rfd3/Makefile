git: update
	git add .
	git commit
	git push
update: rfd3.txt

rfd3.txt: rfd3.xml
	xml2rfc --text rfd3.xml
	sed -i -e '/\f/{n;s/^...../RFD RFDN/}' rfd3.txt
	ed rfd3.txt < Edfile
rfd3.xml: rfd3.md
	sed '0,/title =/{s/ ."$$/"/}' rfd3.md | mmark > rfd3.xml
