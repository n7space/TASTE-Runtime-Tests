VISUAL?=kate

all: compile-linux

clean:
	rm -rf obj
edit:
	echo "project tmp_ponger is For Source_Dirs use (\"src\", \"../../dataview/Ada/\"); end tmp_ponger;" > tmp_ponger.gpr
	gnat-gps -P tmp_ponger.gpr
	rm tmp_ponger.gpr

compile-linux:
	mkdir -p obj && cd obj && ADA_INCLUDE_PATH=../../../dataview/Ada gnat make ../src/ponger
