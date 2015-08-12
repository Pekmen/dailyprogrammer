#!/usr/bin/env python3

import random
import string



def encode(s, key):
    encoded = [[ch for ch in s[col::key]] for col in range(0, key)]
    return("".join("".join(k) for k in encoded))

def decode(s, key):
    cols = len(s) // key
    decoded = [[ch for ch in s[col::cols]] for col in range(cols)]
    return("".join("".join(k) for k in decoded))

def sneaky_decode(s, clue):
    for i in range(1, len(s)):
        if ("".join([ch for ch in s[::i]][:len(clue)])) == clue:
            print(len(s))
    return(decode(s, len(s) // 8))


def main():
    message = "I_rso_wotTe,taef_h__hl__socaeihtemonraaheamd_svemsp_l_ems_ayiN___Anofeadt.yueo_oh_..__leaA_.iaastnY.snw__do__d_nyeuhl_foor_eiaotushlvrr.'oapee.avnv_d__he,ey_gOf___oiunrbpaunieeer_r_l_geos_ctoingoloyfq_rcam__ilainpotlimadufhjv_llt_emiw_aevsdnrsdriengieysr_p_tc_,tlfteuc_uitwrrawavzo_irhlez_ftrelszloyyry_bir__e_huv_no_eadeauuyvsbs_mtoe_l.rb_urat_eeh_y_pOsreg_fjnp,rocucee___otn_cpgbmujltaayprgiayr_uepfb_btt,velyahe_s,eogeraq__ue__ncysr.hcdzoo__ar_duftTcioi'tahkmnarwxeeeegeae_r__j" 
    key = 3
    clue = "It_seems"
    for i in range((len(message) % key) - 1):
        message += random.choice(string.ascii_letters)
  
    print(sneaky_decode(message, clue))


if __name__ == "__main__":
    main()