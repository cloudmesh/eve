FILE=objects

all: 
	pandoc ../README.rst -o readme.tex
	pandoc ../../classes/docs/source/lesson/prg/rest.rst -o rest.tex
	pandoc ../../classes/docs/source/lesson/prg/python_cmd5.rst -o python-cmd5.tex
	pdflatex  -shell-escape ${FILE}
#	bibtex ${FILE}
	pdflatex  -shell-escape ${FILE}
	pdflatex  -shell-escape ${FILE}

watch:
	pandoc ../README.rst -o readme.tex
	pandoc ../../classes/docs/source/lesson/prg/rest.rst -o rest.tex
	pandoc ../../classes/docs/source/lesson/prg/python_cmd5.rst -o python-cmd5.tex
	latexmk -pvc -pdf -pdflatex="pdflatex -shell-escape" ${FILE}


man:
	cms schema help > schema-man.tex
	#cms schema help > schema-man.txt
	#echo '\\begin{verbatim}' > schema-man.tex
	#cat schema-man.txt >> schema-man.tex
	#echo '\\end{verbatim}' >> schema-man.tex

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
	latexmk -shell-escape -pvc -view=pdf ${FILE} 

.PHONY: all clean view fast watch
