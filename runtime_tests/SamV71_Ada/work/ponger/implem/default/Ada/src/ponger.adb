--  Body file for function Ponger
--  Generated by TASTE (kazoo/templates/skeletons/ada-body/function.tmplt)
--  You can edit this file, it will not be overwritten
--
--  !! IMPORTANT                                                        !!
--  !! When you modify your design (interface view), you must update    !!
--  !! the procedures corresponding to the provided interfaces in this  !!
--  !! file. The up-to-date signatures can be found in the .ads file.   !!


package body Ponger is

    storageVar : asn1SccMyInteger := 0;

    procedure Ping (pingArg : in out asn1SccMyinteger) is
    begin
        storageVar := pingArg * 2;
        Ponger_RI.Pong(storageVar);
    end Ping;

    begin
        null;

end Ponger;

