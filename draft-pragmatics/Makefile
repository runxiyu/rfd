update: pragmatics.txt pragmatics.7
	git add .
	git commit
	git push

pragmatics.7: pragmatics.md
	mmark --man pragmatics.md > pragmatics.7
pragmatics.txt: pragmatics.xml
	xml2rfc --text pragmatics.xml
	sed -i -e '/\f/{n;s/^.\{5\}/RFD 1/}' pragmatics.txt
	ed pragmatics.txt < Edfile
pragmatics.xml: pragmatics.md
	sed '0,/title =/{s/ ."$$/"/}' pragmatics.md | mmark > pragmatics.xml

