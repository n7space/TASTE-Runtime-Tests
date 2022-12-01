-- This file was generated automatically by OpenGEODE: DO NOT MODIFY IT !

with System.IO;
use System.IO;

with Ada.Unchecked_Conversion;
with Ada.Numerics.Generic_Elementary_Functions;

package body Pinger is
   procedure Pong(pongArg: in out asn1SccMyInteger) is
      begin
         case ctxt.state is
            when asn1Sccwait =>
               ctxt.pongarg := pongArg;
               Execute_Transition (1);
            when others =>
               Execute_Transition (CS_Only);
         end case;
      end Pong;
      

   procedure Tick is
      begin
         case ctxt.state is
            when asn1Sccwait =>
               Execute_Transition (2);
            when others =>
               Execute_Transition (CS_Only);
         end case;
      end Tick;
      

   procedure Execute_Transition (Id : Integer) is
      trId : Integer := Id;
      begin
         while (trId /= -1) loop
            case trId is
               when 0 =>
                  --  counter := 0 (10,13)
                  ctxt.counter := 0;
                  --  NEXT_STATE Wait (12,18) at 398, 129
                  trId := -1;
                  ctxt.State := asn1SccWait;
                  goto Continuous_Signals;
               when 1 =>
                  --  get_sender(sender) (1,5)
                  RI_0_get_sender(ctxt.sender);
                  --  writeln("Pong: ", pongArg) (18,17)
                  Put ("Pong: ");
                  Put (asn1SccMyInteger'Image (ctxt.pongArg));
                  New_Line;
                  --  NEXT_STATE Wait (20,22) at 743, 195
                  trId := -1;
                  ctxt.State := asn1SccWait;
                  goto Continuous_Signals;
               when 2 =>
                  --  get_sender(sender) (1,5)
                  RI_0_get_sender(ctxt.sender);
                  --  Ping(counter) (27,19)
                  RI_0_Ping(ctxt.counter);
                  --  counter := counter + 1 (29,17)
                  ctxt.counter := (ctxt.counter + 1);
                  --  NEXT_STATE Wait (31,22) at 549, 250
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
end Pinger;