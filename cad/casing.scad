wall = 1;
width = 180;
length = 90;
bottomwallheight = 10;

keyplanesupport = 3;

cube([width, length, wall]);
translate([width-3*wall-keyplanesupport, length-3*wall-keyplanesupport, wall])
    cube([keyplanesupport, keyplanesupport, keyplanesupport]);
translate([width-3*wall-keyplanesupport, 3*wall+20, wall])
    cube([keyplanesupport, keyplanesupport, keyplanesupport]);

translate([0,-wall,0])
    cube([width, wall, bottomwallheight]);
translate([0,length,0])
    cube([width, wall, bottomwallheight]);
translate([-wall,-wall,0])
    cube([wall, length+2*wall, bottomwallheight]);
translate([width,-wall,0])
    cube([wall, length+2*wall, bottomwallheight]);