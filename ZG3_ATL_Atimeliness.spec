
-- A_TIMELINESS
atl "Atimeliness"
<<>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A"
<<Ah>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B"
<<Ah, Bh>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_Horloge"
<<Ah, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B_Horloge"
<<Ah, Bh, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_Reseau_Horloge"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B_Reseau_Horloge"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B"
<<Bh>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B_Horloge"
<<Bh, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B_Reseau_Horloge"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_Reseau"
<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_Reseau_Horloge"
<<reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_Horloge"
<<Horloge>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

