/* Header file for function Controller
 * Generated by TASTE (kazoo/templates/skeletons/c-header/function.tmplt)
 * DO NOT EDIT THIS FILE, IT WILL BE OVERWRITTEN DURING THE BUILD
 */

#pragma once

#include "dataview-uniq.h"

#ifdef __cplusplus
extern "C" {
#endif

#include <stdlib.h>
#include <stdio.h>

void controller_startup(void);

/* Provided interfaces */
void controller_PI_pong( const asn1SccMyInteger * );


void controller_PI_tick( void );

/* Required interfaces */
extern void controller_RI_ping( const asn1SccMyInteger * );


#ifdef __cplusplus
}
#endif