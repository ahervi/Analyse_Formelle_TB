-- propriétés ATL associées au programme ZG2

-- TERMINAISON de Ah et Bh
atl "terminaison" 
<<>> F(STOPa & STOPb);

atl "terminaison_A" 
<<Ah>> F(STOPa & STOPb);

atl "terminaison_A_B"
<<Ah, Bh>> F(STOPa & STOPb);

atl "terminaison_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B>> F(STOPa & STOPb);

atl "terminaison_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPa & STOPb);

atl "terminaison_B"
<<Bh>> F(STOPa & STOPb);

atl "terminaison_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPa & STOPb);

atl "terminaison_Reseau"
<<reseau_delai_fini_non_fiable_A_B>> F(STOPa & STOPb);


-- VIABILITE
atl "viabilite"
<<>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A"
<<Ah>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B"
<<Ah, Bh>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B"
<<Bh>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilite_Reseau"
<<reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & EOOb & EOOk_b);


-- A_TIMELINESS
atl "Atimeliness"
<<>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A"
<<Ah>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B"
<<Ah, Bh>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_Reseau"
<<Ah, reseau_delai_fini_non_fiable_A_B>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B"
<<Bh>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "Atimeliness_Reseau"
<<reseau_delai_fini_non_fiable_A_B>> F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));


-- B_TIMELINESS
atl "Btimeliness" 
<<>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A" 
<<Ah>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B" 
<<Ah, Bh>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_Reseau" 
<<Ah, reseau_delai_fini_non_fiable_A_B>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_A_B_Reseau"
<<Ah, Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B"
<<Bh>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_B_Reseau"
<<Bh, reseau_delai_fini_non_fiable_A_B>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "Btimeliness_Reseau"
<<reseau_delai_fini_non_fiable_A_B>> F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));


-- NON_REPUDIATION de A
atl "A_non_repudiation"
~<< >> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B"
~<<Bh >> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_B_reseau"
~<<Bh, reseau_delai_fini_non_fiable_A_B>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));

atl "A_non_repudiation_reseau"
~<<reseau_delai_fini_non_fiable_A_B>> F(EOOb & EOOk_b & ~<<Ah>> F(EORa & EORk_a));


-- NON_REPUDIATION de B
atl "B_non_repudiation"
~<< >> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A"
~<<Ah >> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_A_reseau"
~<<Ah, reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));

atl "B_non_repudiation_reseau"
~<<reseau_delai_fini_non_fiable_A_B>> F(EORa & EORk_a & ~<<Bh>> F(EOOb & EOOk_b));
