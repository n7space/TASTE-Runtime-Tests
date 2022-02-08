TEMPLATE = lib
CONFIG -= qt
CONFIG += generateC

DISTFILES += deploymentview.dv.xml \
    SamV71_HWAS.asn \
    SamV71_HWAS.msc \
    SamV71_HWAS.acn
DISTFILES += interfaceview.xml
DISTFILES += work/binaries/*.msc
DISTFILES += work/binaries/coverage/index.html
DISTFILES += work/binaries/filters
#include(handleAsn1AcnBuild.pri)
include(work/taste.pro)
message($$DISTFILES)

