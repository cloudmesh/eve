FILE=objects

all: 
	pandoc ../../README.rst -o readme.tex
	pandoc ../../../classes/docs/source/lesson/prg/rest.rst -o rest.tex
	pandoc ../../../classes/docs/source/lesson/prg/python_cmd5.rst -o python-cmd5.tex
	pdflatex  -shell-escape ${FILE}
#	bibtex ${FILE}
	pdflatex  -shell-escape ${FILE}
	pdflatex  -shell-escape ${FILE}

spec:
	cms schema spec2tex ../specification specification

man:
	cms schema hel > schema-man.tex

real-clean: clean
	rm -rf *.pdf

clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.tdo *.bcf

view:
	open ${FILE}.pdf

# all dependce tracking taking care of by Latexmk
fast:
	latexmk -pdf -latexoption=-shell-escape ${FILE}

watch:
	latexmk -pvc -view=pdf ${FILE} 

.PHONY: all clean view fast watch
