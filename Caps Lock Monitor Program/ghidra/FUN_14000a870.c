
/* WARNING: Function: _guard_dispatch_icall replaced with injection: guard_dispatch_icall */

undefined8 FUN_14000a870(longlong param_1,uint param_2,char *param_3,int param_4)

{
  longlong lVar1;
  longlong *plVar2;
  longlong lVar3;
  code *pcVar4;
  longlong *plVar5;
  undefined8 uVar6;
  int iVar7;
  undefined8 uVar8;
  
  if (((param_3 == (char *)0x0) || (*param_3 != '1')) || (param_4 != 0x58)) {
    return 0xfffffffa;
  }
  if (param_1 == 0) {
    return 0xfffffffe;
  }
  pcVar4 = *(code **)(param_1 + 0x30);
  uVar8 = 0;
  *(undefined8 *)(param_1 + 0x20) = 0;
  iVar7 = 0;
  if (pcVar4 == (code *)0x0) {
    pcVar4 = FUN_14000b1d0;
    *(undefined8 *)(param_1 + 0x40) = 0;
    *(code **)(param_1 + 0x30) = FUN_14000b1d0;
    uVar6 = uVar8;
  }
  else {
    uVar6 = *(undefined8 *)(param_1 + 0x40);
  }
  if (*(longlong *)(param_1 + 0x38) == 0) {
    *(code **)(param_1 + 0x38) = FUN_14000b1e0;
  }
  plVar5 = (longlong *)(*pcVar4)(uVar6,1,0x1bf0);
  if (plVar5 == (longlong *)0x0) {
    return 0xfffffffc;
  }
  *(longlong **)(param_1 + 0x28) = plVar5;
  *plVar5 = param_1;
  plVar5[8] = 0;
  *(undefined4 *)(plVar5 + 1) = 0x3f34;
  if (((*(longlong *)(param_1 + 0x30) != 0) && (*(longlong *)(param_1 + 0x38) != 0)) &&
     ((plVar2 = *(longlong **)(param_1 + 0x28), plVar2 != (longlong *)0x0 &&
      ((*plVar2 == param_1 && (*(int *)(plVar2 + 1) - 0x3f34U < 0x20)))))) {
    lVar3 = *(longlong *)(param_1 + 0x28);
    if ((int)param_2 < 0) {
      if ((int)param_2 < -0xf) goto LAB_14000aac5;
      param_2 = -param_2;
    }
    else {
      iVar7 = (param_2 >> 4) + 5;
      if ((int)param_2 < 0x30) {
        param_2 = param_2 & 0xf;
      }
    }
    if ((param_2 == 0) || (param_2 - 8 < 8)) {
      if ((*(longlong *)(lVar3 + 0x40) != 0) && (*(uint *)(lVar3 + 0x30) != param_2)) {
        (**(code **)(param_1 + 0x38))(*(undefined8 *)(param_1 + 0x40));
        *(undefined8 *)(lVar3 + 0x40) = 0;
      }
      *(int *)(lVar3 + 0x10) = iVar7;
      *(uint *)(lVar3 + 0x30) = param_2;
      if ((((*(longlong *)(param_1 + 0x30) != 0) && (*(longlong *)(param_1 + 0x38) != 0)) &&
          (plVar2 = *(longlong **)(param_1 + 0x28), plVar2 != (longlong *)0x0)) &&
         ((*plVar2 == param_1 && (*(int *)(plVar2 + 1) - 0x3f34U < 0x20)))) {
        lVar3 = *(longlong *)(param_1 + 0x28);
        *(undefined8 *)(lVar3 + 0x34) = 0;
        *(undefined4 *)(lVar3 + 0x3c) = 0;
        if (((*(longlong *)(param_1 + 0x30) == 0) || (*(longlong *)(param_1 + 0x38) == 0)) ||
           ((plVar2 = *(longlong **)(param_1 + 0x28), plVar2 == (longlong *)0x0 ||
            ((*plVar2 != param_1 || (0x1f < *(int *)(plVar2 + 1) - 0x3f34U)))))) {
          uVar8 = 0xfffffffe;
        }
        else {
          lVar3 = *(longlong *)(param_1 + 0x28);
          *(undefined4 *)(lVar3 + 0x24) = 0;
          *(undefined4 *)(param_1 + 0x1c) = 0;
          *(undefined4 *)(param_1 + 0xc) = 0;
          *(undefined8 *)(param_1 + 0x20) = 0;
          if (*(uint *)(lVar3 + 0x10) != 0) {
            *(uint *)(param_1 + 0x4c) = *(uint *)(lVar3 + 0x10) & 1;
          }
          lVar1 = lVar3 + 0x550;
          *(undefined8 *)(lVar3 + 8) = 0x3f34;
          *(longlong *)(lVar3 + 0x88) = lVar1;
          *(longlong *)(lVar3 + 0x68) = lVar1;
          *(longlong *)(lVar3 + 0x60) = lVar1;
          *(undefined4 *)(lVar3 + 0x14) = 0;
          *(undefined4 *)(lVar3 + 0x18) = 0xffffffff;
          *(undefined4 *)(lVar3 + 0x1c) = 0x8000;
          *(undefined8 *)(lVar3 + 0x28) = 0;
          *(undefined8 *)(lVar3 + 0x48) = 0;
          *(undefined4 *)(lVar3 + 0x1be0) = 1;
          *(undefined4 *)(lVar3 + 0x1be4) = 0xffffffff;
        }
        if ((int)uVar8 == 0) {
          return uVar8;
        }
        goto LAB_14000aaca;
      }
    }
  }
LAB_14000aac5:
  uVar8 = 0xfffffffe;
LAB_14000aaca:
  (**(code **)(param_1 + 0x38))(*(undefined8 *)(param_1 + 0x40),plVar5);
  *(undefined8 *)(param_1 + 0x28) = 0;
  return uVar8;
}

