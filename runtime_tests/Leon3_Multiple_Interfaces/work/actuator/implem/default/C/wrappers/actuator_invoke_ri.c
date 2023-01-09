// Implementation of the glue code in C handling required interfaces

#include <stdlib.h>
#include "C_ASN1_Types.h"
#include "dataview-uniq.h"

extern unsigned actuator_initialized;

void actuator_RI_pong
      (const asn1SccMyInteger *IN_pong);
void actuator_RI_pong
      (const asn1SccMyInteger *IN_pong)
{
   // Encode parameter pong using ASN.1 UPER
   
   static char IN_buf_pong[asn1SccMyInteger_REQUIRED_BYTES_FOR_ENCODING] = {0};
   int size_IN_buf_pong =
      Encode_UPER_MyInteger
        ((void *)&IN_buf_pong,
          asn1SccMyInteger_REQUIRED_BYTES_FOR_ENCODING,
          (asn1SccMyInteger *)IN_pong);
   if (-1 == size_IN_buf_pong) {
      // Crash the application due to message loss
      abort();
   }


   // Send the message via the middleware API
   extern void vm_actuator_pong
     (void *, size_t);

   vm_actuator_pong
     ((void *)&IN_buf_pong, (size_t)size_IN_buf_pong);


}

