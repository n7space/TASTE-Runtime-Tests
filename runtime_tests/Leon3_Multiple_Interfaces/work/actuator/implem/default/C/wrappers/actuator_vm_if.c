/* Body file for function Actuator
 * Generated by TASTE (kazoo/templates/glue/language_wrappers/vm-if-body/function.tmplt)
 */
#include "actuator_vm_if.h"
#include "C_ASN1_Types.h"




unsigned actuator_initialized = 0;
void init_actuator(void)
{
   if (0 == actuator_initialized) {
      actuator_initialized = 1;
      // Call user code startup function
      extern void actuator_startup(void);
      actuator_startup();
      actuator_initialized = 2;
   }
}
void actuator_ping
      (const char *IN_ping, size_t IN_ping_len)

{
   
   static asn1SccMyInteger IN_PING;

   if (0 != Decode_UPER_MyInteger (&IN_PING, (void *)IN_ping, IN_ping_len)) {
      return;
   }

   //  Declare user code function as external (it may not have a .h if it is in Ada)
   extern void actuator_PI_ping
      (const asn1SccMyInteger *);





   // Call user code
   actuator_PI_ping (&IN_PING);

}
