update: pragmatics.txt pragmatics.7 pragmatics.pdf pragmatics.ps pragmatics.html
	git add .
	git commit
	git push

pragmatics.pdf: pragmatics.ps
	ps2pdf pragmatics.ps
pragmatics.ps: pragmatics.txt
	paps pragmatics.txt --top-margin=21 --bottom-margin=21 > pragmatics.ps
pragmatics.7: pragmatics.md
	mmark --man pragmatics.md > pragmatics.7
	ed pragmatics.7 < Edman
pragmatics.txt pragmatics.html: pragmatics.xml
	xml2rfc --text --html pragmatics.xml
	sed -i -e '/\f/{n;s/^.\{5\}/RFD 1/}' pragmatics.txt
	ed pragmatics.txt < Edfile
pragmatics.xml: pragmatics.md
	sed '0,/title =/{s/ ."$$/"/}' pragmatics.md | mmark > pragmatics.xml

