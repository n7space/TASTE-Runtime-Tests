-- This file was generated automatically by OpenGEODE: DO NOT MODIFY IT !

with Interfaces,
     Interfaces.C.Strings,
     Ada.Characters.Handling;

use Interfaces,
    Interfaces.C.Strings,
    Ada.Characters.Handling;

with SAMV71_ADA_OG_DATAVIEW;
use SAMV71_ADA_OG_DATAVIEW;
with TASTE_BasicTypes;
use TASTE_BasicTypes;
with System_Dataview;
use System_Dataview;
with adaasn1rtl;
use adaasn1rtl;
with Pinger_Datamodel; use Pinger_Datamodel;

with Pinger_RI;
package Pinger with Elaborate_Body is
   
   ctxt : aliased asn1SccPinger_Context :=
      (Init_Done => False,
       sender => asn1Sccenv,
      others => <>);
   self : constant asn1SccPID := asn1Sccpinger;
   function Get_State return Chars_Ptr is (Pinger_RI.To_C_Pointer (asn1SccPinger_States'Image (ctxt.State))) with Export, Convention => C, Link_Name => "pinger_state";
   procedure Startup with Export, Convention => C, Link_Name => "Pinger_startup";
   --  Provided interface "Pong"
   procedure Pong(pongArg: in out asn1SccMyInteger);
   pragma Export(C, Pong, "pinger_PI_Pong");
   --  Provided interface "Tick"
   procedure Tick;
   pragma Export(C, Tick, "pinger_PI_Tick");
   --  Required interface "Ping"
   procedure RI_0_Ping(pingArg : in out asn1SccMyInteger; Dest_PID : asn1SccPID := asn1SccEnv) renames Pinger_RI.Ping;
   --  Synchronous Required Interface "get_sender"
   procedure RI_0_get_sender (sender : out asn1SccPID; Dest_PID : asn1SccPID := asn1SccEnv) renames Pinger_RI.get_sender;
   procedure Execute_Transition (Id : Integer);
   CS_Only : constant := 3;
end Pinger;