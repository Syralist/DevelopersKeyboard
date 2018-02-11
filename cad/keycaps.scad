include<key.scad>;

DCS_ROW_0 = 0;
DCS_ROW_1 = 1;
DCS_ROW_2 = 2;
DCS_ROW_2_SPACEBAR = 10;
DCS_ROW_3 = 3;
DCS_ROW_4 = 4;
DCS_ROW_4_SPACEBAR = 11;

DSA = 5;

SA_ROW_1 = 6;
SA_ROW_2 = 7;
SA_ROW_3 = 8;
SA_ROW_4 = 9;

GSA_ROW_1 = 12;
GSA_ROW_2 = 13;
GSA_ROW_3 = 14;
GSA_ROW_4 = 15;
GSA_ROW_5 = 16;

GSA_ROW_2_1x2 = 17;
GSA_ROW_1_1_5x1 = 18;
GSA_ROW_2_1_5x1 = 19;
GSA_ROW_3_1_5x1 = 20;
GSA_ROW_4_1_5x1 = 21;
GSA_ROW_5_1_5x1 = 22;

GSA_ROW_2_1x1_5 = 23;
GSA_ROW_4_1x1_5 = 24;

module PlayButton()
{
    PlayButtonSize = 3.5;
    difference()
    {
        blank_key( key_row = DCS_ROW_1 );
        rotate([0,0,270])
            translate([-1.5,-1.*PlayButtonSize,6.75])
                #linear_extrude()
                {
                    polygon(points=[[-PlayButtonSize,0],
                                    [PlayButtonSize,0],
                                    [0,2*PlayButtonSize]]);
                }
    }
}

module StopButton()
{
    StopButtonSize = 5.0;
    difference()
    {
        blank_key( key_row = DCS_ROW_1 );
        translate([-.01*StopButtonSize,.25*StopButtonSize,6.75])
            rotate([0,0,45])
                #linear_extrude()
                {
                    polygon(points=[[-StopButtonSize,0],
                                    [0,StopButtonSize],
                                    [StopButtonSize,0],
                                    [0,-StopButtonSize]]);
                }
    }
}




StopButton();

