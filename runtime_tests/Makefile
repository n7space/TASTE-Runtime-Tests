MKDIR=mkdir -p
PYTEST=pytest
REPORT_DIR=reports
DOXYGEN_OUTPUT_DIR=doxygen

.PHONY: test all srs directories

all: directories srs test clean

directories: ${REPORT_DIR}

${REPORT_DIR}:
	${MKDIR} $@

srs:
	./generate_doc.sh
	echo $(shell find -name srs.xml) ${REPORT_DIR}/
	cp `find ${DOXYGEN_OUTPUT_DIR} -name srs.xml` ${REPORT_DIR}/

test:
	pytest -vv --html=${REPORT_DIR}/report.html --self-contained-html --junitxml=${REPORT_DIR}/report.xml

clean:
	rm -rf ${DOXYGEN_OUTPUT_DIR}
	rm -rf ${REPORT_DIR}
