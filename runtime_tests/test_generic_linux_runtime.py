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
# \brief Generic Linux Runitem Large Packet
@pytest.mark.parametrize('taste_project',
                         ['Generic_Linux_Runtime_Large_Packet'],
                         indirect=True)
def test_generic_linux_runtime_large_packet(taste_project):
    build = common.do_build(taste_project, [])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

    timeout = 12
    expected = [
        ['[TASTE] Initialization completed for function Actuator',
         '[TASTE] Initialization completed for function Controller'],
        'Controller - sending work',
        'Actuator - got work',
        'Actuator - result sent',
        'Controller - got result',
        'Controller - sending work',
        'Actuator - got work',
        'Actuator - result sent',
        'Controller - got result'
    ]
    errors = common.do_execute(taste_project, expected, timeout)
    assert not errors, '\n'.join(errors)


##
# \brief Generic_Linux_Variable_Length_Message
# \SRS ETB-FUN-7030
@pytest.mark.parametrize('taste_project',
                         ['Generic_Linux_Variable_Length_Message'],
                         indirect=True)
def test_generic_linux_variable_length_message(taste_project):
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
# \brief Generic_Linux_Multiple_Interfaces
# \SRS ETB-FUN-7010
# \SRS ETB-FUN-7020
@pytest.mark.parametrize('taste_project',
                         ['Generic_Linux_Multiple_Interfaces'],
                         indirect=True)
def test_generic_linux_multiple_interfaces(taste_project):
    build = common.do_build(taste_project, ['deploymentview', 'debug'])

    # Check expected compilation output
    stderr = build.stderr.decode('utf-8')
    assert build.returncode == 0, 'Compilation errors: \n{}'.format(stderr)

    timeout = 6
    expected = [
        ['[TASTE] Initialization completed for function Actuator',
         '[TASTE] Initialization completed for function Controller'],
        'task_a OK',
        'task_b OK',
    ]
    errors = common.do_execute(taste_project, expected, timeout)
    assert not errors, '\n'.join(errors)
