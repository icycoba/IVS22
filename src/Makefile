# Autor: Martin Hlinský (xhlins01)
# Projekt: IVS #2 - Tvorba kalkulačky

.PHONY: all pack clean test doc run profile

all: run

pack: clean doc
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04/repo
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04/install
	mkdir ../../xhlins01_xdudov02_xkundr07_xnekul04/doc
	rsync -a --exclude='doc/' --exclude='install/' .. ../../xhlins01_xdudov02_xkundr07_xnekul04/repo
	rsync -a ../install ../../xhlins01_xdudov02_xkundr07_xnekul04/
	rsync -a ../doc ../../xhlins01_xdudov02_xkundr07_xnekul04/
	cd ../.. && zip -r xhlins01_xdudov02_xkundr07_xnekul04.zip xhlins01_xdudov02_xkundr07_xnekul04


clean:
	rm -rf ../../xhlins01_xdudov02_xkundr07_xnekul04
	rm -rf ../../xhlins01_xdudov02_xkundr07_xnekul04.zip
	rm -rf ./html
	rm -rf ./latex
	rm -rf ./__pycache__

test: mathlibtests.py
	python3 $^

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	cd ../doc && doxygen ../src/$^

run: gui.py
	python3 $^

profile: profiling.py
	python3 $^