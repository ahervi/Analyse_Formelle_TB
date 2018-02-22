
-- NON_REPUDIATION de A
atl "A_non_repudiation"
~<< >> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B"
~<<Bh >> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B_reseau"
~<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B_Horloge"
~<<Bh, Horloge>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B_reseau_Horloge"
~<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_reseau"
~<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_reseau_Horloge"
~<<reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_Horloge"
~<<Horloge >> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));


