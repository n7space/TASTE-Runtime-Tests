/* Body file for function Actuator
 * Generated by TASTE on 2022-10-07 13:40:16
 * You can edit this file, it will not be overwritten
 * Provided interfaces : ping
 * Required interfaces : pong
 * User-defined properties for this function:
 *   |_ Taste::Startup_Priority = 1
 * Timers              : 
 */

#include "actuator.h"
//#include <stdio.h>


void actuator_startup(void)
{
   // Write your initialisation code, but DO NOT CALL REQUIRED INTERFACES
   // puts ("[Actuator] Startup");
}

void actuator_PI_ping
      (const asn1SccMyInteger *IN_ping)

{
   static asn1SccMyInteger doubled = 0;
   doubled = *IN_ping * 2;

   actuator_RI_pong(&doubled);
}

