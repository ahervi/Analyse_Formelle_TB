-- proprietes ATL associees au programme ZG3



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

