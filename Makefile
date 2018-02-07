SPHINX=sphinx-build
SOURCE=tech/source/
OUTPUT=tech/build/

all: build

clean:
	@echo "Removing ${OUTPUT}"
	@rm -r ${OUTPUT}

build:
	@echo "Rebuilding HTML documentation"
	@${SPHINX} -b html ${SOURCE} ${OUTPUT}

.PHONY: clean build
