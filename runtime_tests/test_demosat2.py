#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Date: 2022.12.13
# Result: Mission scenario for the demonstration was established and it can be found in the TASTE-Runtime-Tests
# repository (https://github.com/n7space/TASTE-Runtime-Tests) in the file ‘demosat2_mission_scenario.txt’
#
# \SRS ETB-OPER-10
def test_MissionScenarioWasEstablished():
  pass

##
# Date: 2022.12.13
# Result: All of the SEDS based sensors and actuators: 
# \* AFEC Hwas 
# \* SunSensor 
# \* PIO HWAS 
# \* UART HWAS 
# \* TfLuna 
# \* MP6500 
# \* LIDAR 
# \* Propulsion 
# were exercised in the mission scenario. 
#
# \SRS ETB-OPER-20
def test_MissionScenarioExercisesAllSedsBasedSensorsAndActuators():
  pass

##
# Date: 2022.12.13 Result: All of the inter-node interfaces: 
# \* tc 
# \* tm 
# \* hk 
# \* debug_hk 
# were exercised in the mission scenario. 
#
# \SRS ETB-OPER-30
def test_MissionScenarioExercisesAllInterNodeInterfaces():
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

