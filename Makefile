TARGET := target
DATA := tubular/data
TEMPLATES := $(DATA)/templates
PYV := 2.7
PY := bin/python
CSS := $(wildcard $(TEMPLATES)/*.css)
CSS_TARGETS := $(CSS:$(TEMPLATES)/%=$(TARGET)/%)

all: $(PY) css adapters tubes monitors monitorid

$(PY):
	virtualenv-$(PYV) --no-site-packages .

tubes: $(TARGET)/tube $(DATA)/bk_data.json $(DATA)/sencore_data.json $(DATA)/monitor_data.json $(TEMPLATES)/tube_page.html tubular/make_tubes.py
	./bin/mktubes --target=$(TARGET)/tube

target/tube/%.html: $(TARGET)/tube $(DATA)/bk_data.json $(DATA)/sencore_data.json $(DATA)/monitor_data.json $(TEMPLATES)/tube_page.html tubular/make_tubes.py css
	./bin/mktubes --target=$(TARGET)/tube $*

monitors: $(TARGET)/monitor $(DATA)/monitor_data.json $(TEMPLATES)/monitor.html $(TEMPLATES)/monitor_page.html
	./bin/mkmonitors --target=$(TARGET)/monitor

monitorid: $(TARGET)/monitor/identify.html

$(TARGET)/monitor/identify.html: $(TARGET)/monitor $(DATA)/monitor_data.json $(TEMPLATES)/monitor_id_page.html $(TEMPLATES)/monitor.html tubular/make_monitorid.py
	./bin/mkmonitorid --target=$(TARGET)

$(TARGET):
	mkdir -p $@

$(TARGET)/tube:
	mkdir -p $@

$(TARGET)/monitor: $(TARGET)
	mkdir -p $@

css: $(CSS_TARGETS)
$(CSS_TARGETS): $(TARGET)/%: $(TEMPLATES)/% $(TARGET)
	cp $< $@

test:
	@echo $(ADAPTER_TARGETS)

adapters: $(TARGET)/adapters
$(TARGET)/adapters: $(DATA)/adapters
	cp -R $< $@

clean:
	rm -rf $(TARGET)
