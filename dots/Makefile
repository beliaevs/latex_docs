OUTPDF=diagrams_test.pdf division.pdf test.pdf WhiteAttachmentObjects.pdf 

all: $(OUTPDF)

%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm $(OUTPDF)