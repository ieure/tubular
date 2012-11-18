JS     := $(wildcard *.js)
JS_OBJ := $(JS:%=%.o)
JCC     = closure-compiler

all: index.html

index.html: index.html.m4 reset.css monitor.css $(JS_OBJ) Makefile
	m4 $< > $@

%.js.o: %.js
	$(JCC) --js $^ --js_output_file $@

clean:
	rm -f index.html $(JS_OBJ)
