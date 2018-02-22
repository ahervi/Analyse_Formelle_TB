
-- TERMINAISON de Ah et Bh
atl "terminaison" 
<<>> F(STOPa & STOPb);

atl "terminaison_A" 
<<Ah>> F(STOPa & STOPb);

atl "terminaison_A_B"
<<Ah, Bh>> F(STOPa & STOPb);

atl "terminaison_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & STOPb);

atl "terminaison_A_Horloge"
<<Ah, Horloge>> F(STOPa & STOPb);

atl "terminaison_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & STOPb);

atl "terminaison_A_B_Horloge"
<<Ah, Bh, Horloge>> F(STOPa & STOPb);

atl "terminaison_A_Reseau_Horloge"
<<Ah, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & STOPb);

atl "terminaison_A_B_Reseau_Horloge"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B_Tiers, Horloge>> F(STOPa & STOPb);

atl "terminaison_B"
<<Bh>> F(STOPa & STOPb);

atl "terminaison_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & STOPb);

atl "terminaison_B_Horloge"
<<Bh, Horloge>> F(STOPa & STOPb);

atl "terminaison_B_Reseau_Horloge"
<<Bh, reseau_delai_fini_non_fiable_A_B_Tiers,Horloge>> F(STOPa & STOPb);

atl "terminaison_Reseau"
<<reseau_delai_fini_non_fiable_A_B_Tiers>> F(STOPa & STOPb);

atl "terminaison_Reseau_Horloge"
<<reseau_delai_fini_non_fiable_A_B_Tiers,Horloge>> F(STOPa & STOPb);

atl "terminaison_Horloge"
<<Horloge>> F(STOPa & STOPb);
