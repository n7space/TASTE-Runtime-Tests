TEMPLATE = lib
CONFIG -= qt
CONFIG += generateC

DISTFILES +=  $(HOME)/tool-inst/share/taste-types/taste-types.asn \
    deploymentview.dv.xml
DISTFILES += SamV71_Ada_OG.msc
DISTFILES += interfaceview.xml
DISTFILES += work/binaries/*.msc
DISTFILES += work/binaries/coverage/index.html
DISTFILES += work/binaries/filters
DISTFILES += work/system.asn

DISTFILES += SamV71_Ada_OG.asn
DISTFILES += SamV71_Ada_OG.acn
include(work/taste.pro)
message($$DISTFILES)

