
void FUN_14000ac30(int param_1,ushort *param_2,uint param_3,longlong *param_4,uint *param_5,
                  undefined *param_6)

{
  longlong lVar1;
  ushort uVar2;
  code *pcVar3;
  byte bVar4;
  undefined2 uVar6;
  byte bVar7;
  ushort *puVar8;
  uint uVar9;
  ulonglong uVar10;
  longlong lVar11;
  ulonglong uVar12;
  ulonglong uVar13;
  ulonglong uVar14;
  uint uVar15;
  ulonglong uVar16;
  int iVar17;
  uint uVar18;
  uint uVar19;
  uint uVar20;
  uint uVar21;
  byte bVar22;
  uint uVar23;
  bool bVar24;
  bool bVar25;
  undefined auStack_f8 [32];
  undefined4 local_d8;
  uint local_d0;
  uint local_c8;
  uint local_c4;
  int local_c0;
  undefined *local_b8;
  undefined *local_b0;
  undefined *local_a8;
  longlong *local_a0;
  ushort *local_98;
  uint *local_90;
  ushort auStack_88 [16];
  ushort auStack_68 [16];
  ulonglong local_48;
  char cVar5;
  
  local_48 = DAT_14003f040 ^ (ulonglong)auStack_f8;
  uVar16 = 0;
  local_90 = param_5;
  local_a8 = param_6;
  uVar10 = (ulonglong)param_3;
  uVar13 = uVar16;
  do {
    local_c0 = param_1;
    local_a0 = param_4;
    local_98 = param_2;
    if (0x1f < uVar13 * 2) {
      FUN_14000b414();
      pcVar3 = (code *)swi(3);
      (*pcVar3)();
      return;
    }
    uVar20 = (int)uVar13 + 1;
    auStack_88[uVar13] = 0;
    uVar13 = (ulonglong)uVar20;
  } while (uVar20 < 0x10);
  puVar8 = param_2;
  if (param_3 != 0) {
    do {
      auStack_88[*puVar8] = auStack_88[*puVar8] + 1;
      uVar10 = uVar10 - 1;
      puVar8 = puVar8 + 1;
    } while (uVar10 != 0);
  }
  uVar20 = 0xd;
  uVar10 = 0xf;
  do {
    uVar19 = (uint)uVar10;
    if (auStack_88[uVar10] != 0) goto LAB_14000ad3a;
    if (auStack_88[uVar20 + 1] != 0) {
      uVar19 = uVar19 - 1;
      goto LAB_14000ad3a;
    }
    if (auStack_88[uVar20] != 0) {
      uVar19 = uVar19 - 2;
      goto LAB_14000ad3a;
    }
    if (auStack_88[uVar20 - 1] != 0) {
      uVar19 = uVar19 - 3;
      goto LAB_14000ad3a;
    }
    if (auStack_88[uVar20 - 2] != 0) {
      uVar19 = uVar19 - 4;
      goto LAB_14000ad3a;
    }
    uVar10 = (ulonglong)(uVar19 - 5);
    uVar20 = uVar20 - 5;
  } while (uVar19 - 5 != 0);
  uVar19 = 0;
LAB_14000ad3a:
  uVar20 = uVar19;
  if (*param_5 <= uVar19) {
    uVar20 = *param_5;
  }
  if (uVar19 == 0) {
    local_d8 = 0x140;
    *(undefined4 *)*param_4 = 0x140;
    *param_4 = *param_4 + 4;
    *(undefined4 *)*param_4 = 0x140;
    *param_4 = *param_4 + 4;
    *param_5 = 1;
  }
  else {
    uVar21 = 1;
    if (1 < uVar19) {
      puVar8 = auStack_88;
      do {
        puVar8 = puVar8 + 1;
        if (*puVar8 != 0) break;
        uVar21 = uVar21 + 1;
      } while (uVar21 < uVar19);
    }
    uVar10 = 1;
    local_c4 = uVar21;
    if (uVar21 <= uVar20) {
      local_c4 = uVar20;
    }
    iVar17 = 1;
    do {
      iVar17 = iVar17 * 2 - (uint)auStack_88[uVar10];
      if (iVar17 < 0) goto LAB_14000b19c;
      uVar20 = (int)uVar10 + 1;
      uVar10 = (ulonglong)uVar20;
    } while (uVar20 < 0x10);
    if ((iVar17 < 1) || ((param_1 != 0 && (uVar19 == 1)))) {
      auStack_68[1] = 0;
      lVar11 = 0xe;
      uVar10 = uVar16;
      do {
        *(short *)((longlong)auStack_68 + uVar10 + 4) =
             *(short *)((longlong)auStack_88 + uVar10 + 2) +
             *(short *)((longlong)auStack_68 + uVar10 + 2);
        uVar10 = uVar10 + 2;
        lVar11 = lVar11 + -1;
      } while (lVar11 != 0);
      puVar8 = param_2;
      uVar10 = uVar16;
      if (param_3 != 0) {
        do {
          if (*puVar8 != 0) {
            *(short *)(param_6 + (ulonglong)auStack_68[*puVar8] * 2) = (short)uVar10;
            auStack_68[*puVar8] = auStack_68[*puVar8] + 1;
          }
          uVar20 = (int)uVar10 + 1;
          puVar8 = puVar8 + 1;
          uVar10 = (ulonglong)uVar20;
        } while (uVar20 < param_3);
      }
      uVar10 = 0;
      lVar11 = *param_4;
      bVar7 = (byte)local_c4;
      uVar20 = local_c4;
      if (param_1 == 0) {
        uVar12 = 0x14;
        local_b8 = param_6;
        local_b0 = param_6;
        uVar16 = 0;
        local_d0 = 0x14;
        uVar23 = 1 << (bVar7 & 0x1f);
        uVar18 = 0xffffffff;
        local_c8 = uVar23 - 1;
        uVar13 = 0;
      }
      else {
        if (param_1 == 1) {
          local_d0 = 0x101;
          local_b0 = &DAT_140032240;
          uVar23 = 1 << (bVar7 & 0x1f);
          local_b8 = &DAT_140032280;
          local_c8 = uVar23 - 1;
        }
        else {
          uVar23 = 1 << (bVar7 & 0x1f);
          local_b0 = &DAT_1400322c0;
          uVar18 = 0xffffffff;
          local_b8 = &DAT_140032300;
          local_c8 = uVar23 - 1;
          local_d0 = 0;
          if (param_1 != 1) {
            local_b0 = &DAT_1400322c0;
            local_d0 = 0;
            local_b8 = &DAT_140032300;
            if (param_1 == 2) {
              local_b0 = &DAT_1400322c0;
              uVar12 = 0;
              local_b8 = &DAT_140032300;
              local_d0 = 0;
              uVar13 = uVar12;
              uVar10 = uVar16;
              if (0x250 < uVar23) goto LAB_14000b19c;
            }
            else {
              uVar12 = 0;
              uVar13 = 0;
              uVar16 = 0;
            }
            goto LAB_14000afa0;
          }
        }
        uVar18 = 0xffffffff;
        if (0x354 < uVar23) goto LAB_14000b19c;
        uVar12 = (ulonglong)local_d0;
        uVar13 = 0;
        uVar16 = 0;
      }
LAB_14000afa0:
      cVar5 = (char)uVar21;
      bVar22 = (byte)uVar10;
      bVar4 = cVar5 - bVar22;
      uVar2 = *(ushort *)(param_6 + uVar13 * 2);
      uVar9 = (uint)uVar12;
      if (uVar2 + 1 < uVar9) {
        local_d8 = (uint)CONCAT21(uVar2,bVar4) << 8;
      }
      else {
        local_d8._1_3_ = (uint3)bVar4;
        if (uVar2 < uVar9) {
          local_d8 = CONCAT31(local_d8._1_3_,0x60);
          uVar6 = 0;
        }
        else {
          lVar1 = (ulonglong)(uVar2 - uVar9) * 2;
          local_d8._0_2_ = CONCAT11(bVar4,local_b8[lVar1]);
          uVar6 = *(undefined2 *)(local_b0 + lVar1);
        }
        local_d8 = CONCAT22(uVar6,(undefined2)local_d8);
      }
      iVar17 = 1 << (cVar5 - bVar22 & 0x1f);
      uVar15 = (uint)uVar16;
      uVar9 = 1 << ((byte)uVar20 & 0x1f);
      uVar16 = (ulonglong)((uVar15 >> (bVar22 & 0x1f)) + uVar9);
      uVar14 = (ulonglong)uVar9;
      do {
        uVar16 = (ulonglong)(uint)((int)uVar16 - iVar17);
        *(int *)(lVar11 + uVar16 * 4) = local_d8;
        uVar9 = uVar9 - iVar17;
      } while (uVar9 != 0);
      for (uVar9 = 1 << (cVar5 - 1U & 0x1f); (uVar15 & uVar9) != 0; uVar9 = uVar9 >> 1) {
      }
      if (uVar9 == 0) {
        uVar16 = 0;
      }
      else {
        uVar16 = (ulonglong)((uVar15 & uVar9 - 1) + uVar9);
      }
      uVar13 = (ulonglong)((int)uVar13 + 1);
      puVar8 = auStack_88 + uVar21;
      *puVar8 = *puVar8 - 1;
      if (*puVar8 == 0) {
        if (uVar21 == uVar19) {
          if ((uint)uVar16 != 0) {
            local_d8._1_3_ = (uint3)((uint)local_d8 >> 8) & 0xff;
            local_d8 = CONCAT31(local_d8._1_3_,0x40);
            *(int *)(lVar11 + uVar16 * 4) = local_d8;
          }
          *param_4 = *param_4 + (ulonglong)uVar23 * 4;
          *param_5 = local_c4;
          goto LAB_14000b19c;
        }
        uVar21 = (uint)param_2[*(ushort *)(param_6 + uVar13 * 2)];
      }
      uVar12 = (ulonglong)local_d0;
      if (local_c4 < uVar21) {
        uVar9 = local_c8 & (uint)uVar16;
        if (uVar9 != uVar18) {
          lVar11 = lVar11 + uVar14 * 4;
          if ((int)uVar10 == 0) {
            uVar10 = (ulonglong)local_c4;
          }
          uVar20 = uVar21 - (int)uVar10;
          uVar18 = uVar21;
          for (iVar17 = 1 << ((byte)uVar20 & 0x1f);
              (uVar18 < uVar19 &&
              (uVar12 = (ulonglong)uVar18, 0 < (int)(iVar17 - (uint)auStack_88[uVar12])));
              iVar17 = (iVar17 - (uint)auStack_88[uVar12]) * 2) {
            uVar20 = uVar20 + 1;
            uVar18 = uVar18 + 1;
          }
          uVar23 = uVar23 + (1 << ((byte)uVar20 & 0x1f));
          if (param_1 == 1) {
            bVar24 = uVar23 < 0x354;
            bVar25 = uVar23 == 0x354;
LAB_14000b119:
            if (!bVar24 && !bVar25) goto LAB_14000b19c;
          }
          else if (param_1 == 2) {
            bVar24 = uVar23 < 0x250;
            bVar25 = uVar23 == 0x250;
            goto LAB_14000b119;
          }
          lVar1 = (ulonglong)uVar9 * 4;
          *(byte *)(lVar1 + *param_4) = (byte)uVar20;
          *(byte *)(lVar1 + 1 + *param_4) = bVar7;
          *(short *)(lVar1 + 2 + *param_4) = (short)(lVar11 - *param_4 >> 2);
          uVar12 = (ulonglong)local_d0;
          uVar18 = uVar9;
        }
      }
      goto LAB_14000afa0;
    }
  }
LAB_14000b19c:
  FUN_14000b2e0(local_48 ^ (ulonglong)auStack_f8);
  return;
}

