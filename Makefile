JS     := $(wildcard *.js)
#JS_OBJ := $(JS:%=%.o)
JCC     = closure-compiler
MAKES   = bk sencore
SHARED  = reset.css monitor.css monitor.js.o Makefile

all: bk.html sencore.html

index.html: bk.html
	ln -s $^ $@

bk.html: index.html.m4 bk_headers.html.m4 bk_data.js.o $(SHARED)
	m4 -D__TYPE__=bk $< > $@

sencore.html: index.html.m4 sencore_headers.html.m4 sencore_data.js.o $(SHARED)
	m4 -D__TYPE__=sencore $< > $@

%.js.o: %.js
	$(JCC) --js $^ --js_output_file $@

clean:
	rm -f index.html $(JS_OBJ)
