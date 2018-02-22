

-- NON_REPUDIATION de B
atl "B_non_repudiation"
~<< >> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A"
~<<Ah >> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A_reseau"
~<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A_Horloge"
~<<Ah, Horloge>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A_reseau_Horloge"
~<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_reseau"
~<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_reseau_Horloge"
~<<reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_Horloge"
~<<Horloge>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

