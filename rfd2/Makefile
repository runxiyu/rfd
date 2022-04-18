update: rfd2.txt rfd2.7
	git add .
	git commit
	git push

rfd2.7: rfd2.md
	mmark --man rfd2.md > rfd2.7
rfd2.txt: rfd2.xml
	xml2rfc --text rfd2.xml
	sed -i -e '/\f/{n;s/^...../RFD RFDN/}' rfd2.txt
	ed rfd2.txt < Edfile
rfd2.xml: rfd2.md
	sed '0,/title =/{s/ ."$$/"/}' rfd2.md | mmark > rfd2.xml
