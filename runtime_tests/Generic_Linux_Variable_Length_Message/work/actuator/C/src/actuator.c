/* Body file for function Actuator
 * Generated by TASTE on 2021-11-29 13:58:01
 * You can edit this file, it will not be overwritten
 * Provided interfaces : task_a, task_b
 * Required interfaces : result
 * User-defined properties for this function:
 *   |_ TASTE::Is_Component_Type = false
 * Timers              : 
 */

#include "actuator.h"

static asn1SccLargeUint32 response;

void actuator_startup(void)
{
    response = 0;
}

static void calculate_sum(const asn1SccBigParameter *IN_large_data)
{
    response = IN_large_data->x;
    int i;
    for(i = 0; i < 262144; ++i)
    {
        response += IN_large_data->y.arr[i];
    }
}

void actuator_PI_task_a_native
      (const asn1SccBigParameter *IN_large_data)

{
   calculate_sum(IN_large_data);
   actuator_RI_result(&response);
}
void actuator_PI_task_b_native
      (const asn1SccSmallParameter *IN_small_data)

{
    response = IN_small_data->x + IN_small_data->y;
    actuator_RI_result(&response);
}

void actuator_PI_task_a_uper
      (const asn1SccBigParameter *IN_large_data)

{
    calculate_sum(IN_large_data);
    actuator_RI_result(&response);
}
void actuator_PI_task_b_uper
      (const asn1SccSmallParameter *IN_small_data)

{
    response = IN_small_data->x + IN_small_data->y;
    actuator_RI_result(&response);
}
void actuator_PI_task_a_acn
      (const asn1SccBigParameter *IN_large_data)

{
    calculate_sum(IN_large_data);
    actuator_RI_result(&response);
}
void actuator_PI_task_b_acn
      (const asn1SccSmallParameter *IN_small_data)

{
    response = IN_small_data->x + IN_small_data->y;
    actuator_RI_result(&response);
}
