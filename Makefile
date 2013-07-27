SRCDIR = src
OUTDIR = target
JCC     = closure-compiler
MAKES   = bk sencore
SHARED  = $(wildcard $(SRCDIR)/css/*.css) $(wildcard $(SRCDIR/data))
TARGETS = $(MAKES:%=$(OUTDIR)/%.html) $(OUTDIR)/index.html
M4     := m4 -I$(SRCDIR) -I$(OUTDIR)

all: $(TARGETS)

$(OUTDIR)/index.html: $(OUTDIR)/bk.html
	ln -s $(notdir $^) $@

$(OUTDIR)/bk.html: $(SRCDIR)/bk.html.m4 $(SHARED) $(OUTDIR)/tubular.js.o $(OUTDIR)/bk_data.js.o
	$(M4) -D__TYPE__=bk $< > $@

$(OUTDIR)/sencore.html: $(SRCDIR)/sencore.html.m4 $(SHARED) $(OUTDIR)/tubular.js.o $(OUTDIR)/sencore_data.js.o
	$(M4) -D__TYPE__=sencore $< > $@

$(OUTDIR)/%.js.o: $(SRCDIR)/%.js
	$(JCC) --js $^ --js_output_file $@

dist: all
	s3cmd put $(TARGETS) s3://tubular.atomized.org
	s3cmd setacl --acl-public s3://tubular.atomized.org/bk.html \
	    s3://tubular.atomized.org/sencore.html

clean:
	rm -f target/*
