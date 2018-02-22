
-- VIABILITE
atl "viabilite"
<<>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A"
<<Ah>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B"
<<Ah, Bh>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_Horloge"
<<Ah, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B_Horloge"
<<Ah, Bh, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_Reseau_Horloge"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B_Reseau_Horloge"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B"
<<Bh>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B_Horloge"
<<Bh, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B_Reseau_Horloge"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_Reseau"
<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_Reseau_Horloge"
<<reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_Horloge"
<<Horloge>> F(EORa & EORk_a & EOOb & EOOk_b);

