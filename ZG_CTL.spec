-- propriétés CTL associées aux programmes ZG1.rm et ZG2.rm

atl "terminaison_possible"
E F(STOPa & STOPb);

atl "terminaison_inévitable"
A F(STOPa & STOPb);

atl "viabilité_possible"
E F(EORa & EORk_a & EOOb & EOOk_b);

atl "viabilité_inévitable"
A F(EORa & EORk_a & EOOb & EOOk_b);

atl "timeliness_possible_A"
E F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "timeliness_inévitable_A"
A F(STOPa & (~(EORa & EORk_a) => (~E F(EOOb & EOOk_b))));

atl "timeliness_possible_B"
E F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a)))) ;

atl "timeliness_inévitable_B"
A F(STOPb & (~(EOOb & EOOk_b) => (~E F(EORa & EORk_a))));

atl "non_repudiation_possible_A_1"
~A F(EOOb & EOOk_b & ~E F(EORa & EORk_a));

atl "non_repudiation_possible_A_2"
~E F(EOOb & EOOk_b & ~E F(EORa & EORk_a));

atl "non_repudiation_inévitable_A_1"
~A F(EOOb & EOOk_b & ~A F(EORa & EORk_a));

atl "non_repudiation_inévitable_A_2"
~E F(EOOb & EOOk_b & ~A F(EORa & EORk_a));

atl "non_repudiation_possible_B_1"
~A F(EORa & EORk_a & ~E F(EOOb & EOOk_b));

atl "non_repudiation_possible_B_2"
~E F(EORa & EORk_a & ~E F(EOOb & EOOk_b));

atl "non_repudiation_inévitable_B_1"
~A F(EORa & EORk_a & ~A F(EOOb & EOOk_b));

atl "non_repudiation_inévitable_B_2"
~E F(EORa & EORk_a & ~A F(EOOb & EOOk_b));
