VERSION=draft
FILE=objects

all: 
	# pandoc ../README.rst -o readme.tex
	# pandoc ../../classes/docs/source/lesson/prg/rest.rst -o includes/rest.tex
	# pandoc ../../classes/docs/source/lesson/prg/python_cmd5.rst -o includes/python-cmd5.tex
	pdflatex  -shell-escape ${FILE}
#	bibtex ${FILE}
	pdflatex  -shell-escape ${FILE}
	pdflatex  -shell-escape ${FILE}
	cp objects.pdf NIST.SP.1500-8-${VERSION}.pdf

define generate_uml
	cd images/uml; java -jar plantuml.jar -Tsvg $(1).uml
	cd images/uml; cairosvg $(1).svg -o $(1).pdf
endef

define generate_dot
	cd images/dot; dot -Tpdf -o $(1).pdf  $(1).dot 
endef

dot:
	$(call generate_dot,account)
	$(call generate_uml,boot)
	$(call generate_uml,account)
	$(call generate_uml,virtualcluster)

t1:
	suml --png --font-family "Comic Sans MS" --scruffy -i f.uml > test.png; e test.png 

watch:
	latexmk -pvc -pdf -pdflatex="pdflatex -shell-escape" ${FILE}

s:
	suml --png --scruffy --sequence  > tmp/sequence1-scruffy.png


man:
	cms schema help > schema-man.tex
	#cms schema help > schema-man.txt
	#echo '\\begin{verbatim}' > schema-man.tex
	#cat schema-man.txt >> schema-man.tex
	#echo '\\end{verbatim}' >> schema-man.tex

real-clean: clean
	rm -rf *.pdf

clean:
	rm -rf rm objects-pics.pdf
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.tdo *.bcf
	rm -rf _minted-objects

view:
	open ${FILE}.pdf

# all dependce tracking taking care of by Latexmk
fast:
	latexmk -pdf -latexoption=-shell-escape ${FILE}

# watch:
#	latexmk -shell-escape -pvc -view=pdf ${FILE} 

.PHONY: all clean view fast watch
