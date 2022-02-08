TEMPLATE = lib
CONFIG -= qt
CONFIG += generateC

DISTFILES += Generic_Linux_Variable_Lengtth_Message.asn \
    deploymentview.dv.xml
DISTFILES += Generic_Linux_Variable_Lengtth_Message.acn
DISTFILES += Generic_Linux_Variable_Lengtth_Message.msc
DISTFILES += interfaceview.xml
DISTFILES += work/binaries/*.msc
DISTFILES += work/binaries/coverage/index.html
DISTFILES += work/binaries/filters
#include(handleAsn1AcnBuild.pri)
include(work/taste.pro)
message($$DISTFILES)

