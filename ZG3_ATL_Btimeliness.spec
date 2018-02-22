
-- B_TIMELINESS
atl "Btimeliness" 
<<>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A" 
<<Ah>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B" 
<<Ah, Bh>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_Reseau" 
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_Horloge" 
<<Ah, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B_Horloge"
<<Ah, Bh, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_Reseau_Horloge"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B_Reseau_Horloge"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B"
<<Bh>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B_Horloge"
<<Bh, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B_Reseau_Horloge"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers,Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_Reseau"
<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_Reseau_Horloge"
<<reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_Horloge"
<<Horloge>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));
