JS     := $(wildcard *.js)
#JS_OBJ := $(JS:%=%.o)
JCC     = closure-compiler
MAKES   = bk sencore
SHARED  = reset.css monitor.css monitor.js.o Makefile

all: bk.html sencore.html

bk.html: bk.html.m4 bk_data.js.o $(SHARED)
	m4 $< > $@

sencore.html: sencore.html.m4 sencore_data.js.o $(SHARED)
	m4 $< > $@

%.js.o: %.js
	$(JCC) --js $^ --js_output_file $@

clean:
	rm -f index.html $(JS_OBJ)
