TEMPLATE = lib
CONFIG -= qt
CONFIG += generateC

DISTFILES += Generic_Linux_Multiple_Interfaces.asn \
    deploymentview.dv.xml
DISTFILES += Generic_Linux_Multiple_Interfaces.acn
DISTFILES += Generic_Linux_Multiple_Interfaces.msc
DISTFILES += interfaceview.xml
DISTFILES += work/binaries/*.msc
DISTFILES += work/binaries/coverage/index.html
DISTFILES += work/binaries/filters
#include(handleAsn1AcnBuild.pri)
include(work/taste.pro)
message($$DISTFILES)

