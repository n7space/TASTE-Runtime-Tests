#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
# DemoSat2 SAMV71-based node contains 2 actuators - LIDAR motor and LEDs - described using SEDS models.
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
# DemoSat2 Linux-based node contains 4 interfaces for communication with SAMV71-based node:
# \* tc
# \* tm
# \* hk
# \* debug_hk
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

