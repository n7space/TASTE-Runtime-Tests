-- This file was generated automatically by OpenGEODE: DO NOT MODIFY IT !

with System.IO;
use System.IO;

with Ada.Unchecked_Conversion;
with Ada.Numerics.Generic_Elementary_Functions;

package body Ponger is
   procedure Ping(pingArg: in out asn1SccMyInteger) is
      begin
         case ctxt.state is
            when asn1Sccwait =>
               ctxt.pingarg := pingArg;
               Execute_Transition (1);
            when others =>
               Execute_Transition (CS_Only);
         end case;
      end Ping;
      

   procedure Execute_Transition (Id : Integer) is
      trId : Integer := Id;
      begin
         while (trId /= -1) loop
            case trId is
               when 0 =>
                  --  counter := 0 (10,13)
                  ctxt.counter := 0;
                  --  NEXT_STATE Wait (12,18) at 367, 125
                  trId := -1;
                  ctxt.State := asn1SccWait;
                  goto Continuous_Signals;
               when 1 =>
                  --  get_sender(sender) (1,5)
                  RI_0_get_sender(ctxt.sender);
                  --  counter := pingArg * 2 (18,17)
                  ctxt.counter := (ctxt.pingArg * 2);
                  --  Pong(counter) (20,19)
                  RI_0_Pong(ctxt.counter);
                  --  NEXT_STATE Wait (22,22) at 503, 242
                  trId := -1;
                  ctxt.State := asn1SccWait;
                  goto Continuous_Signals;
               when CS_Only =>
                  trId := -1;
                  goto Continuous_Signals;
               when others =>
                  null;
            end case;
            <<Continuous_Signals>>
            <<Next_Transition>>
         end loop;
      end Execute_Transition;
      

   procedure Startup is
      begin
         Execute_Transition (0);
         ctxt.Init_Done := True;
      end Startup;
   begin
      Startup;
end Ponger;