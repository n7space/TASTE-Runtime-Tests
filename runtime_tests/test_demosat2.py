#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Date: 2022.12.09
# Result: DemoSat2 is LIDAR instrument with:
# \* COTS laser rangefinder communicating via UART
# \* Stepper motor driven via PIO
# \* Limit sensors read via PIO
# \* Auxiliary light sensor read via ADC
# \* Auxiliary LED "enginemocks"/"data indicators" driven via PIO
# \* Auxiliary “deployment”servos driven via PIO + PWM.
#
# \SRS ETB-OPER-10
def test_ProvideDemonstrationApplication():
  pass

##
# Date: 2022.12.09
# Result: Mission scenario exercises all high-level SEDS functions:
# \* LIDAR (sensor, but with integrated actuator)
# \* Servos (actuator)
# \* Light Sensor (sensor)
# \* LED mocks (actuator)
#
# ETB-OPER-20
def test_ExerciseAllHighLevelSedsFunctions():
  pass

##
# Date: 2022.12.09
# Result: Mission scenario exercises additional TASTE Functions (ModeManager and Housekeeping) and communication
# (1 TC interface and 2 TM interfaces).
#
# ETB-OPER-30
def test_ExerciseAllInterNodeInterfaces():
  pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, DemoSat2 is based on the TASTE SAMV71 runtime and as such it too targets
# ATSAMV71Q21 MCU
#
# \SRS ETB-RES-30
def test_DemoTargetsATSAMV71Q21Mcu():
  pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, DemoSat2 targets ATSAMV71Q21 MCU which features 2MB of SDRAM.
#
# \SRS ETB-RES-40
def test_DemoTargetsPlatformWith2MbSdram():
  pass

##
# As per chapter 5.1 of ETB-N7S-ADD-001, DemoSat2 targets ATSAMV71Q21 MCU which features 2MB of embedded flash.
#
# \SRS ETB-RES-50
def test_DemoTargetsPlatformWith2MbFlash():
  pass

##
# DemoSat2 contains a deployment hw.dv.xml which includes a node "SAM_V71_FreeRTOS_N7S_1"
# of type ocarina_processors_arm::samv71.freertos
#
# \SRS ETB-DES-80
def test_DemoIncludesSamv71BasedNode():
  pass

##
# DemoSat2 SAMV71-based node contains 2 sensors - LIDAR and light sensor - described using SEDS models.
#
# \SRS ETB-DES-90
def test_DemoIncludesTwoSedsDescribedSensors():
  pass

##
# DemoSat2 SAMV71-based node contains 2 actuators - servos and LEDs - described using SEDS models.
#
# \SRS ETB-DES-100
def test_DemoIncludesTwoSedsDescribedActuators():
  pass

##
# DemoSat2 contains 14 TASTE functions:
# \* EGSE
# \* Manager
# \* ObjectDetector
# \* SunSensorProxy
# \* SunSensorDriver
# \* LidarDriver
# \* PropulsionDriver
# \* TfLunaDriver
# \* MP6500Driver
# \* UartHwasDriver
# \* PioHwasDriver
# \* AfecHwasDriver
# \* InterruptProxy
# \* HWAS
#
# \SRS ETB-DES-110
def test_DemoIncludesAtLeast8TasteFunctions():
  pass

##
# DemoSat2 contains a deployment hw.dv.xml which includes a node "x86_Linux_CPP_1"
# of type ocarina_processors_x86::x86.generic_linux
#
# \SRS ETB-DES-120
def test_DemoIncludesLinuxBasedNode():
  pass

##
# DemoSat2 Linux-based node contains 3 interfaces for communication with SAMV71-based node:
# \* tc
# \* tm
# \* hk
#
# \SRS ETB-DES-130
def test_DemoLinuxNodeCommunicatesUsingAtLeastThreeInterfaces():
  pass

##
# Sensors and actuators use those HWAS functions for accessing hardware:
# \* HWAS
# \* PioHwasDriver
# \* UartHwasDriver
# \* AfecHwasDriver
#
# \SRS ETB-DES-180
def test_DemoSensorsAndActuatorsAccessesHardwareUsingHwas():
  pass

