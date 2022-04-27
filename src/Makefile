# Autor: Martin Hlinský (xhlins01)
# Projekt: IVS #2 - Tvorba kalkulačky

.PHONY: all pack clean test doc run profile

all: run

pack: doc
	mkdir -p ../../xhlins01_xdudov02_xkundr07_xnekul04/repo
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04/install
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04/doc
	cp -a ../. ../../xhlins01_xdudov02_xkundr07_xnekul04/repo


clean:
	rm -rf ../../xhlins01_xdudov02_xkundr07_xnekul04/

test: mathlibtests.py
	python3 $^

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc && cd ../doc && doxygen ../src/$^


run: gui.py
	python3 $^

profile: profiling.py
	python3 $^