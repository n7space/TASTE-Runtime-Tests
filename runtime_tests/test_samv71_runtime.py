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
