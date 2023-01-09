// Implementation of the glue code in C handling required interfaces

#include <stdlib.h>
#include <stdio.h>
#include "PrintTypesAsASN1.h"
#include "timeInMS.h"
#include "C_ASN1_Types.h"
#include "dataview-uniq.h"

extern unsigned controller_initialized;

void controller_RI_ping
      (const asn1SccMyInteger *IN_ping);
void controller_RI_ping
      (const asn1SccMyInteger *IN_ping)
{
   // Log MSC data on Linux when environment variable is set
   static int innerMsc = -1;
   if (-1 == innerMsc)
      innerMsc = (NULL != getenv("TASTE_INNER_MSC"))?1:0;
   if (1 == innerMsc) {
      long long msc_time = getTimeInMilliseconds();
      // Log message to Actuator (corresponding PI: ping)
      printf ("INNER_RI: controller,actuator,ping,ping,%lld\n", msc_time);
      fflush(stdout);
   }
   // Encode parameter ping using ASN.1 UPER
   
   static char IN_buf_ping[asn1SccMyInteger_REQUIRED_BYTES_FOR_ENCODING] = {0};
   int size_IN_buf_ping =
      Encode_UPER_MyInteger
        ((void *)&IN_buf_ping,
          asn1SccMyInteger_REQUIRED_BYTES_FOR_ENCODING,
          (asn1SccMyInteger *)IN_ping);
   if (-1 == size_IN_buf_ping) {
      puts ("[ERROR] ASN.1 Encoding failed in controller_RI_ping, parameter ping");
      // Crash the application due to message loss
      abort();
   }


   // Send the message via the middleware API
   extern void vm_controller_ping
     (void *, size_t);

   vm_controller_ping
     ((void *)&IN_buf_ping, (size_t)size_IN_buf_ping);


}

