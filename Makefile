JS     := $(wildcard *.js)
#JS_OBJ := $(JS:%=%.o)
JCC     = closure-compiler
MAKES   = bk sencore
SHARED  = reset.css tubular.css tubular.js.o Makefile
TARGETS = bk.html sencore.html

all: $(TARGETS)

index.html: bk.html
	ln -s $^ $@

bk.html: index.html.m4 bk_headers.html.m4 bk_data.js.o $(SHARED)
	m4 -D__TYPE__=bk $< > $@

sencore.html: index.html.m4 sencore_headers.html.m4 sencore_data.js.o $(SHARED)
	m4 -D__TYPE__=sencore $< > $@

%.js.o: %.js
	$(JCC) --js $^ --js_output_file $@

dist: all
	s3cmd put $(TARGETS) s3://tubular.atomized.org
	s3cmd setacl --acl-public s3://tubular.atomized.org/bk.html \
	    s3://tubular.atomized.org/sencore.html

clean:
	rm -f index.html $(JS_OBJ)
