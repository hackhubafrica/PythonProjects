
void FUN_14000b5b0(void)

{
  code *pcVar1;
  bool bVar2;
  char cVar3;
  int iVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  undefined7 extraout_var;
  
  FUN_140019ba0(1);
  uVar5 = FUN_14000bb34();
  _set_fmode((int)uVar5);
  uVar5 = FUN_140005590();
  puVar6 = FUN_14001ac40();
  *puVar6 = (int)uVar5;
  uVar5 = __scrt_initialize_onexit_tables(1);
  if ((char)uVar5 != '\0') {
    FUN_14000bdac();
    atexit(FUN_14000bdf0);
    uVar5 = FUN_14000bb2c();
    iVar4 = _configure_wide_argv((int)uVar5);
    if (iVar4 == 0) {
      FUN_14000bb3c();
      bVar2 = FUN_14000bb78();
      if ((int)CONCAT71(extraout_var,bVar2) != 0) {
        FUN_140019c0c(0x140005590);
      }
      _guard_check_icall();
      _guard_check_icall();
      uVar5 = FUN_140005590();
      _configthreadlocale((int)uVar5);
      cVar3 = FUN_14000bb50();
      if (cVar3 != '\0') {
        thunk_FUN_14001a030();
      }
      FUN_140005590();
      uVar5 = thunk_FUN_140005590();
      if ((int)uVar5 == 0) {
        return;
      }
    }
  }
  FUN_14000bb9c(7);
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}

