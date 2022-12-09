#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import common
import pytest


@pytest.fixture
def taste_project(request):
    test_name = request.param
    common.do_clean_build(test_name)
    yield test_name
    common.do_clean_build(test_name)


##
# \brief SamV71_Multiple_Interfaces
# \SRS ETB-FUN-6010
# \SRS ETB-FUN-6020
# \SRS ETB-FUN-7010
# \SRS ETB-FUN-7020
# \SRS ETB-IF-210
@pytest.mark.parametrize('taste_project',
                         ['SamV71_Multiple_Interfaces'],
                         indirect=True)
def test_samv71_multiple_interfaces(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

    timeout = 30
    expected = [
        '[TASTE] Initialization completed for function Controller',
        'task_a OK',
        'task_b OK',
    ]
    errors = common.do_execute(taste_project, expected, timeout)
    assert not errors, '\n'.join(errors)


##
# \brief SamV71_Multiple_Interfaces
# \SRS ETB-FUN-6030
# \SRS ETB-FUN-7030
# \SRS ETB-IF-210
# \SRS ETB-DES-20
@pytest.mark.parametrize('taste_project',
                         ['SamV71_Variable_Length_Message'],
                         indirect=True)
def test_samv71_variable_length_message(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

    timeout = 26
    expected = [
        ['[TASTE] Initialization completed for function Actuator',
         '[TASTE] Initialization completed for function Controller'],
        'LARGE PARAMETER NATIVE: OK',
        'SMALL PARAMETER NATIVE: OK',
        'LARGE PARAMETER UPER: OK',
        'SMALL PARAMETER UPER: OK',
        'LARGE PARAMETER ACN: OK',
        'SMALL PARAMETER ACN: OK',
    ]

    errors = common.do_execute(taste_project, expected, timeout)
    assert not errors, '\n'.join(errors)


##
# \brief SamV71_HWAS
# \SRS ETB-FUN-5010
# \SRS ETB-FUN-5020
# \SRS ETB-FUN-5030
# \SRS ETB-FUN-5040
# \SRS ETB-FUN-5050
@pytest.mark.parametrize('taste_project',
                         ['SamV71_HWAS'],
                         indirect=True)
def test_samv71_hwas(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

    timeout = 10
    expected = [
        '[TASTE] Initialization completed for function Ground',
        'TEST STARTED',
        'TEST SUCCESS',
    ]

    errors = common.do_execute(taste_project, expected, timeout)
    assert not errors, '\n'.join(errors)

##
# \brief SamV71_Ada
# \SRS ETB-DES-40
@pytest.mark.parametrize('taste_project',
                         ['SamV71_Ada'],
                         indirect=True)
def test_samv71_ada(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

##
# \brief SamV71_Ada_OG
# \SRS ETB-DES-50
@pytest.mark.parametrize('taste_project',
                         ['SamV71_Ada_OG'],
                         indirect=True)
def test_samv71_ada_og(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

##
# TASTE SAMV71 runtime supports deployment of TASTE models containing at least 8 TASTE functions (including
# at least 4 EDS based). This is validated by the demonstration application (DemoSat2) which contains 8 EDS functions,
# and 5 C-based functions deployed onto TASTE SAMV71 Runtime.
# \SRS  ETB-PER-10
@pytest.mark.parametrize('taste_project',
                         ['Demo-Sat-2/src/DemoSat2'],
                         indirect=True)
def test_TasteSamV71RuntimeSupportsAtLeastEightFunctions(taste_project):
    build = common.do_build(taste_project, ['hw', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)
    pass

##
# Date: 2022.12.09
# Result: Hwas XML is included in chapter 5.1.4.1 of ETB-N7S-ADD-001.
# \SRS  ETB-IF-220
def test_HwasProvidedAsSeds():
    pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, TASTE SAMV71 runtime targets ATSAMV71Q21 MCU, by using a set of drivers
# tailored to this platform.
# \SRS  ETB-RES-20
def test_TasteSamV71RuntimeTargetsATSAMV71Q21Mcu():
    pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, Hardware Access SEDS implementation targets ATSAMV71Q21 MCU.
# \SRS  ETB-RES-60
def test_HwasTargetsATSAMV71Q21Mcu():
    pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, TASTE SAMV71 runtime is based on a FreeRTOS port.
# \SRS  ETB-DES-10
def test_TasteSamv71RuntimeBasedOnFreeRtos():
    pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, TASTE SAMV71 runtime uses Sdramc driver to configure SDRAM attached to the MCU.
# \SRS  ETB-DES-12
def test_TasteSamv71RuntimeUsesSdram():
    pass

##
# TASTE SAMV71 runtime shall use DMA in UART implementation as specified in ETB-N7S-ADD-001 document.
# As per chapter 5.1 of ETB-N7S-ADD-001, TASTE SAMV71 runtime uses Xdmac driver to configure DMA for UART communication.
# \SRS  ETB-DES-14
def test_TasteSamv71RuntimeUsesDma():
    pass

##
# HWAS, as described in chapter 5.1.4.1 of ETB-N7S-ADD-001, declares the following interfaces:
# \* InterruptSubscriptionManagementInterfaceType
# \* InterruptSubscriptionInterfaceType
# \* InterruptManagementInterfaceType
# \* RawMemoryAccessInterfaceType
# Each of the interfaces has the “level” attribute set to “subnetwork”.
# \SRS  ETB-DES-150
def test_HwasSetInterfaceLevelToSubnetwork():
    pass

##
# Subnetwork Memory Access Service, as described in CCSDS-852.0-M-1, which is a non-binding recommended practice,
# defines the following items:
# \* memory access service access point address,
# \* destination address,
# \* transaction identifier,
# \* memory id,
# \* start memory address,
# \* size,
# \* mask,
# \* data,
# \* channel,
# \* priority.
#
# As Hwas is responsible for exposing local memory to a local entity, memory access service access point address,
# destination address and channel are considered unnecessary. As the local memory access is immediate and synchronous,
# transaction identifier and priority are considered unnecessary. As SAMV71 exposes the directly readable/writeable
# memories of interest (registers, SRAM and SDRAM) in a single linear address space, memory id is considered
# unnecessary. Start memory address, size, mask and data are used in RawMemoryAccessInterfaceType. While start, size
# and data constitute a minimal usable set of parameters for memory access, mask is considered to be very useful for
# manipulating registers, and is therefore included in ReadWord and WriteWord of the aforementioned interface type.
#
# Subnetwork Memory Access Service, defines the following operations (in form of associated requests and  indications):
# \* read,
# \* write,
# \* read/modify/write.
#
# Read and write are defined in RawMemoryAccessInterfaceType. Read/modify/write was not immediately useful, as the
# intended Hwas use was to access the MCU hardware, while e.g. resource access could be synchronized by higher-level
# constructs present in the relevant TASTE runtime (protected/sporadic interfaces). However, as ETB-FUN-5030 explicitly
# requires this functionality, the existing Hwas definition is to be extended with an appropriate construct.
#
# Subnetwork Memory Access Service does not define any constructs dedicated to handling hardware events.
#
# In conclusion, Subnetwork Memory Access Service was analysed for applicability and usefulness.
# RawMemoryAccessInterfaceType was defined by extracting most relevant concepts, while
# InterruptSubscriptionManagementInterfaceType, InterruptSubscriptionInterfaceType and InterruptManagementInterfaceType
# were designed from scratch, as no relevant constructs were found in the reference recommended practice.
# \SRS  ETB-DES-160
def test_HwasBaseOnSubnetworkMemoryAccessServiceRecommendedPractice():
    pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, HWAS implementation is included in TASTE SAMV71 runtime.
# \SRS  ETB-DES-170
def test_TasteSamv71RuntimeProvidesImplementation():
    pass

##
# Date: 2022.12.09
# Result: TASTE SAMV71 runtime code is distributed across the following repositories:
# \* https://github.com/n7space/TASTE-SAMV71-Drivers
# \* https://github.com/n7space/TASTE-SAMV71-Runtime
# \* https://github.com/n7space/SAMV71-BSP
# \* https://gitrepos.estec.esa.int/taste/kazoo
# ESA’s Kazoo repository is the main repository, containing the templates and capable of downloading the rest of
# the code from publicly accessible GitHub repositories.
# \SRS  ETB-CFG-20
def test_TasteSamv71SourceIsOnEsaTasteRepository():
    pass

##
# Date: 2022.12.09
# Result: TASTE SAMV71 runtime SUM is available on the TASTE Wiki
# https://taste.tuxfamily.org/wiki/index.php?title=Technical_topic:_SAMV71_Runtime
# \SRS  ETB-CFG-40
def test_TasteSamv71RuntimeSumPresentOnTasteWiki():
    pass

##
# Date: 2022.12.09
# Result: TASTE SAMV71 runtime installation script is provided in the ESA’s TASTE repository under the following address:
# https://gitrepos.estec.esa.int/taste/taste-setup/-/blob/feature-samv71-runtime/add-ons/install-samv71-runtime.sh
# \SRS  ETB-INST-20
def test_Samv71RuntimeInstallationScript():
    pass
