/* Body file for function Controller
 * Generated by TASTE on 2021-12-07 14:26:22
 * You can edit this file, it will not be overwritten
 * Provided interfaces : result, trigger
 * Required interfaces : task_a_acn, task_a_native, task_a_uper, task_b_acn, task_b_native, task_b_uper
 * User-defined properties for this function:
 *   |_ TASTE::Is_Component_Type = false
 * Timers              :
 */

#include "controller.h"
#include <stdio.h>
#include <stdbool.h>

enum InternalState {
    WAITING,
    TEST_TASK_A_NATIVE,
    TEST_TASK_B_NATIVE,
    TEST_TASK_A_UPER,
    TEST_TASK_B_UPER,
    TEST_TASK_A_ACN,
    TEST_TASK_B_ACN,
};

#define BIG_PARAMETER_Y_SIZE 128

static enum InternalState state;
static bool waitForResult;
static asn1SccBigParameter bigParameter;
static asn1SccSmallParameter smallParameter;

static void prepareBigParameter(unsigned int value)
{
    int i;
    bigParameter.x = value;
    for(i = 0; i < BIG_PARAMETER_Y_SIZE; ++i)
    {
        bigParameter.y.arr[i] = value;
    }
}

static void prepareSmallParameter(unsigned int value)
{
    smallParameter.x = value;
    smallParameter.y = value;
}

void controller_startup(void)
{
    state = WAITING;
    waitForResult = FALSE;
}

void controller_PI_result
      (const asn1SccLargeUint32 *IN_code)

{
    printf("HELLO FROM RESULT\n");

    if(!waitForResult)
    {
        printf("Unexpected result message: %lu\n", *IN_code);
        return;
    }
    switch(state)
    {
    case WAITING:
        printf("Unexpected result in state waiting: %lu\n", *IN_code);
        return;
    case TEST_TASK_A_NATIVE:
        if(*IN_code == BIG_PARAMETER_Y_SIZE + 1)
        {
            printf("LARGE PARAMETER NATIVE: OK\n");
        }
        else
        {
            printf("LARGE PARAMETER NATIVE: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_B_NATIVE;
        break;
    case TEST_TASK_B_NATIVE:
        if(*IN_code == 2)
        {
            printf("SMALL PARAMETER NATIVE: OK\n");
        }
        else
        {
            printf("SMALL PARAMETER NATIVE: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_A_UPER;
        break;
    case TEST_TASK_A_UPER:
        if(*IN_code == BIG_PARAMETER_Y_SIZE * 2 + 2)
        {
            printf("LARGE PARAMETER UPER: OK\n");
        }
        else
        {
            printf("LARGE PARAMETER UPER: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_B_UPER;
        break;
    case TEST_TASK_B_UPER:
        if(*IN_code == 4)
        {
            printf("SMALL PARAMETER UPER: OK\n");
        }
        else
        {
            printf("SMALL PARAMETER UPER: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_A_ACN;
        break;
    case TEST_TASK_A_ACN:
        if(*IN_code == BIG_PARAMETER_Y_SIZE * 3 + 3)
        {
            printf("LARGE PARAMETER ACN: OK\n");
        }
        else
        {
            printf("LARGE PARAMETER ACN: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_B_ACN;
        break;
    case TEST_TASK_B_ACN:
        if(*IN_code == 6)
        {
            printf("SMALL PARAMETER ACN: OK\n");
        }
        else
        {
            printf("SMALL PARAMETER ACN: FAIL %lu\n", *IN_code);
        }
        state = TEST_TASK_A_NATIVE;
        break;
    }

    waitForResult = FALSE;
}
void controller_PI_trigger(void)
{
    printf("TRIGGER!!!\n");
    printf("%d\n", state);

    if(waitForResult)
    {
        return;
    }
    switch(state)
    {
    case WAITING:
        printf("PING!!!\n");
        controller_RI_ping();
        return;
    case TEST_TASK_A_NATIVE:
        printf("TASK_A_NATIVE\n");
        prepareBigParameter(1);
        controller_RI_task_a_native(&bigParameter);
        printf("AFTER RI\n");
        break;
    case TEST_TASK_B_NATIVE:
        printf("TASK_B_NATIVE\n");
        prepareSmallParameter(1);
        controller_RI_task_b_native(&smallParameter);
        break;
    case TEST_TASK_A_UPER:
        prepareBigParameter(2);
        controller_RI_task_a_uper(&bigParameter);
        break;
    case TEST_TASK_B_UPER:
        prepareSmallParameter(2);
        controller_RI_task_b_uper(&smallParameter);
        break;
    case TEST_TASK_A_ACN:
        prepareBigParameter(3);
        controller_RI_task_a_acn(&bigParameter);
        break;
    case TEST_TASK_B_ACN:
        prepareSmallParameter(3);
        controller_RI_task_b_acn(&smallParameter);
        break;
    }
    printf("SET TRUE\n");
    waitForResult = TRUE;
    printf("FAJRANT\n");
}

void controller_PI_pong()
{
    printf("PONG!!!!\n");
    state = TEST_TASK_A_NATIVE;
}