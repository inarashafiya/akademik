pdf:
	pandoc --pdf-engine=xelatex -o hasil/akademik-praxis-academy.pdf --toc --from markdown --template eisvogel --listings --top-level-division=chapter isi/*
