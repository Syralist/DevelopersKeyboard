// Thing # 468651
// Parametric Cherry MX/Alps Keycap for Mechanical Keyboards
// http://www.thingiverse.com/thing:468651
// by rsheldiii

// Row 5? Cherry MX key
//change to round things better
$fn = 64;

//scale of inner to outer shape
key_wall_thickness_width =  .8;
key_wall_thickness_height = .8;
key_wall_thickness_depth =  .8;

//connector brim
//enable brim for connector
has_brim = 0;
//brim radius. 11 ensconces normal keycap stem in normal keycap
brim_radius = 11;
//brim depth
brim_depth = .3;



//whether stabilizer connectors are enabled
stabilizers = 0;

//stabilizer distance
stabilizer_distance_x = 0;
stabilizer_distance_y = 12;

// invert dishing. mostly for spacebar
inverted_dish = 0;

//keycap type, [0..11]
key_profile = 0;

//profile specific stuff

/*god, I would love a class right here
 here we have, for lack of a better implementation, an array
 that defines the more intimate aspects of a key.
 order is thus:
 1. Bottom Key Width: width of the immediate bottom of the key
 2. Bottom Key Height: height of the immediate bottom of the key
 3. Top Key Width Difference: mm to subtract from bottom key width to create top key width
 4. Top Key Height Difference: mm to subtract from bottom key height to create top key height
 5. total Depth: how tall the total in the switch is before dishing
 6. Top Tilt: X rotation of the top. Top and dish obj are rotated
 7. Top Skew: Y skew of the top of the key relative to the bottom. DCS has some, DSA has none (its centered)
 8. Dish Type: type of dishing. currently sphere and cylinder
 9. Dish Depth: how many mm to cut into the key with
 10. Dish Radius: radius of dish obj, the Sphere or Cylinder that cuts into the keycap
 11. Length of unit of key in X direction. 1 normally, 1.5 for tab.
 12. Length of unit of key in Y direction. 1 normally, 2 for the keypad enter.
*/

key_profiles = [

	//DCS Profile

	[ //DCS ROW 5 - index 0
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6,   // Top Key Width Difference
		4,   // Top Key Height Difference
		11.5, // total Depth
		-6,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		0,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
		1    // Key Length Y
	],
	[ //DCS ROW 1
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6,   // Top Key Width Difference
		4,   // Top Key Height Difference
		8.5, // total Depth
		-1,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		0,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
		1    // Key Length Y
	],
	[ //DCS ROW 2
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6.2,   // Top Key Width Difference
		4,   // Top Key Height Difference
		7.5, // total Depth
		3,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		0,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
		1    // Key Length Y
	],
	[ //DCS ROW 3
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6,   // Top Key Width Difference
		4,   // Top Key Height Difference
		6.2, // total Depth
		7,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		0,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
		1    // Key Length Y
	],
	[ //DCS ROW 4 - index 4
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6,   // Top Key Width Difference
		4,   // Top Key Height Difference
		6.2, // total Depth
		16,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		0,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
		1    // Key Length Y
	],

	//DSA Profile

	[ //DSA ROW 3 - index 5
	  18.4,  // Bottom Key Width
	  18.4,  // Bottom Key Height
	  5.7, // Top Key Width Difference
	  5.7, // Top Key Height Difference
	  7.4, // total Depth
	  0,   // Top Tilt
	  0,   // Top Skew

	  //Dish Profile

	  1,   // Dish Type
	  1.2, // Dish Depth
	  0,   // Dish Skew X
	  0,   // DIsh Skew Y

	  1,   // Key Length X
 	  1    // Key Length Y
	],

	//SA Proile

	[ //SA ROW 1 - index 6
		18.4,  // Bottom Key Width
	  18.4,  // Bottom Key Height
	  5.7, // Top Key Width Difference
	  5.7, // Top Key Height Difference
	  13.73, // total Depth, fudged
	  -14,   // Top Tilt
	  0,   // Top Skew

	  //Dish Profile

	  1,   // Dish Type
	  1.2, // Dish Depth
	  0,   // Dish Skew X
	  0,    // DIsh Skew Y

	  1,   // Key Length X
	  1    // Key Length Y
	],
	[ //SA ROW 2 - index 7
		18.4,  // Bottom Key Width
	  18.4,  // Bottom Key Height
	  5.7, // Top Key Width Difference
	  5.7, // Top Key Height Difference
	  11.73, // total Depth
	  -7,   // Top Tilt
	  0,   // Top Skew

	  //Dish Profile

	  1,   // Dish Type
	  1.2, // Dish Depth
	  0,   // Dish Skew X
	  0,   // DIsh Skew Y

	  1,   // Key Length X
	  1    // Key Length Y
	],
	[ //SA ROW 3 - index 8
		18.4,  // Bottom Key Width
	  18.4,  // Bottom Key Height
	  5.7, // Top Key Width Difference
	  5.7, // Top Key Height Difference
	  11.73, // total Depth
	  0,   // Top Tilt
	  0,   // Top Skew

	  //Dish Profile

	  1,   // Dish Type
	  1.2, // Dish Depth
	  0,   // Dish Skew X
	  0,   // DIsh Skew Y

	  1,   // Key Length X
	  1    // Key Length Y
	],
	[ //SA ROW 4 - index 9
		18.4,  // Bottom Key Width
	  18.4,  // Bottom Key Height
	  5.7, // Top Key Width Difference
	  5.7, // Top Key Height Difference
	  11.73, // total Depth
	  7,   // Top Tilt
	  0,   // Top Skew

	  //Dish Profile

	  1,   // Dish Type
	  1.2, // Dish Depth
	  0,   // Dish Skew X
	  0,    // DIsh Skew Y

	  1,   // Key Length X
	  1    // Key Length Y
	],
	[ //DCS ROW 2 SPACEBAR - index 10
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6.2,   // Top Key Width Difference
		4,   // Top Key Height Difference
		7.5, // total Depth
		3,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		2,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,    // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //DCS ROW 4 SPACEBAR (ORIGINAL) - index 11
		18.16,  // Bottom Key Width
		18.16,  // Bottom Key Height
		6,   // Top Key Width Difference
		4,   // Top Key Height Difference
		6.2, // total Depth
		16,  // Top Tilt
		1.75,// Top Skew

		//Dish Profile

		2,   // Dish Type
		1,   // Dish Depth
		0,   // Dish Skew X
		0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 1 - index 12
		18.4,  // Bottom Key Width
		18.4,  // Bottom Key Height
		5.7, // Top Key Width Difference
		5.7, // Top Key Height Difference
		13.73, // total Depth, fudged
		-20,   // Top Tilt
		0,   // Top Skew

	  	//Dish Profile

		1,   // Dish Type
	 	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 2 - index 13
		18.4,  // Bottom Key Width
	  	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	8.73, // total Depth
	  	-10,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	  	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	 	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 3 - index 14
		18.4,  // Bottom Key Width
	  	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	6.73, // total Depth
	  	0,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	  	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 4 - index 15
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	8.73, // total Depth
	  	10,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 5 - index 16
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	13.73, // total Depth
	  	20,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 2&3 1x2 - index 17
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	7.73, // total Depth
	  	-6,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	2    // Key Length Y
	],
	[ //GSA ROW 1 - 1.5x1 - index 18
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	13.73, // total Depth
	  	-20,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1.5,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 1 - 1.5x1 - index 19
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	8.73, // total Depth
	  	-10,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1.5,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 1 - 1.5x1 - index 20
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	6.73, // total Depth
	  	0,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1.5,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 4 - 1.5x1 - index 21
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	8.73, // total Depth
	  	10,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1.5,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 5 - 1.5x1 - index 22
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	13.73, // total Depth
	  	20,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1.5,   // Key Length X
	  	1    // Key Length Y
	],
	[ //GSA ROW 2&3 - 1x1.5 - index 23
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	7.93, // total Depth
	  	-8,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1.5  // Key Length Y
	],
	[ //GSA ROW 3&4 - 1x1.5 - index 24
		18.4,  // Bottom Key Width
	 	18.4,  // Bottom Key Height
	  	5.7, // Top Key Width Difference
	  	5.7, // Top Key Height Difference
	  	7.93, // total Depth
	  	8,   // Top Tilt
	  	0,   // Top Skew

	  	//Dish Profile

	 	1,   // Dish Type
	  	1.2, // Dish Depth
	  	0,   // Dish Skew X
	  	0,   // DIsh Skew Y

		1,   // Key Length X
	  	1.5  // Key Length Y
	],
];


// cherry MX or Alps stem [0..1]
stem_profile=0;

// how inset the stem is from the bottom of the key. experimental
stem_inset=0;

//libraries. they generate geometry
//that is used by other things to generate features

//centered
module roundedRect(size, radius) {
	x = size[0];
	y = size[1];
	z = size[2];

	translate([-x/2,-y/2,0])
	linear_extrude(height=z)
	hull() {
		translate([radius, radius, 0])
		circle(r=radius);

		translate([x - radius, radius, 0])
		circle(r=radius);

		translate([x - radius, y - radius, 0])
		circle(r=radius);

		translate([radius, y - radius, 0])
		circle(r=radius);
	}
}


//bottom we can use to anchor things
module inside(key_profile)
{
	difference(){
		translate([0,0,50])
		cube([100,100,100],center=true);

		translate([0,0,-.1])
		shape(key_profile, 3);
	}
}

module cherry_stem( stem_rotation,
       		    horizontal_cross_width = 1.4,
       		    vertical_cross_width = 1.4,
		    ){
	// cross length
	cross_length = 4.4;
	//dimensions of connector
	// outer cross extra length in x
	extra_outer_cross_width = 2.10;
	// outer cross extra length in y
	extra_outer_cross_height = 1.0;
	// dimensions of cross
	// horizontal cross bar width
	//horizontal_cross_width = 1.4; // was 1.4, but the fit was way too tight            7->1.5, 8->1.6
	// vertical cross bar width
	//vertical_cross_width = 1.3; // was 1.3, but the fit was way too tight              7->1.4, 8->1.5
	//extra vertical cross length - the extra length of the up/down bar of the cross
	extra_vertical_cross_length = 1.1;
	// cross depth, stem height is 3.4mm
	cross_depth = 4;

	rotate([0,0,stem_rotation]){
	difference(){
		union(){
			translate(
				[
		 			-(cross_length+extra_outer_cross_width)/2,
		 			-(cross_length+extra_outer_cross_height)/2,
		 			stem_inset
				]
			)
			cube( // the base of the stem, the part the cruciform digs into
				[
					cross_length+extra_outer_cross_width,
					cross_length+extra_outer_cross_height,
					50
				]
			);
			if (has_brim == 1){ cylinder(r=brim_radius,h=brim_depth); }
		}
		//the cross part of the steam
		translate([0,0,(cross_depth)/2 + stem_inset])
		{
	            cube([vertical_cross_width,cross_length+extra_vertical_cross_length,cross_depth], center=true );//remove +2 to print with cross
	            cube([cross_length,horizontal_cross_width,cross_depth], center=true );
	        }
	}
	}
}

module alps_stem(){
	cross_depth = 40;
	width = 4.45;
	height = 2.25;

	base_width = 12;
	base_height = 15;

	//translate([0,0,cross_depth + 50/2]) cube([base_width, base_height, 50], center=true);
	translate([0,0,cross_depth/2 + stem_inset]){
		cube([width,height,cross_depth], center = true);
	}


}

//whole connector
module connector(key_profile,has_brim,stem_rotation){
	difference(){
		//TODO can I really not do an array index here?
		if(stem_profile==0) cherry_stem(stem_rotation=stem_rotation);
		if(stem_profile==1) alps_stem();
		inside(key_profile);
	}
}

//stabilizer connectors 
module stabilizer_connectors(key_profile,has_brim,stem_rotation){
	translate([stabilizer_distance_x,stabilizer_distance_y,0])
	connector(key_profile, has_brim,stem_rotation);

	translate([-stabilizer_distance_x,-stabilizer_distance_y,0])
	connector(key_profile, has_brim,stem_rotation);
}

//i h8 u scad
module shape(key_profile, thickness){

	bottom_key_width = key_profile[0] ;
	bottom_key_height = key_profile[1];
	top_key_width_difference = key_profile[2];
	top_key_height_difference = key_profile[3];
	total_depth = key_profile[4] - thickness;
	top_tilt = key_profile[5];
	top_skew = key_profile[6];

	if (inverted_dish == 1){
		difference(){
			union(){
				shape_hull(key_profile, thickness, 1);
				dish(key_profile, thickness);
			}
			outside(key_profile, thickness);
		}
	}
	else{
		difference(){
			shape_hull(key_profile, thickness, 1);	
			dish(key_profile, thickness);
		}
	}
}

//conicalish clipping shape to trim things off the outside of the keycap
module outside(key_profile, thickness){
	difference(){
		cube([100000,100000,100000],center = true);
		shape_hull(key_profile, thickness, 2);
	}
}

//super basic hull shape without dish
module shape_hull(key_profile, thickness, modifier){
	bottom_key_width = key_profile[0] ;
	bottom_key_height = key_profile[1];
	top_key_width_difference = key_profile[2];
	top_key_height_difference = key_profile[3];
	total_depth = key_profile[4] - thickness;
	top_tilt = key_profile[5];
	top_skew = key_profile[6];
	key_x_length = key_profile[11];
	key_y_length = key_profile[12];

	hull(){
		roundedRect([bottom_key_width*key_x_length - thickness,bottom_key_height*key_y_length - thickness,.001],1.5);

		translate([0,top_skew,total_depth * modifier])
		rotate([-top_tilt,0,0])
		roundedRect([bottom_key_width*key_x_length - thickness -top_key_width_difference * modifier,bottom_key_height*key_y_length - thickness -top_key_height_difference * modifier,.001],1.5);
	}
}
//end libraries

//dish selector
module dish(key_profile){ //this thing is a monster
	// names, so I don't go crazy
	total_key_width = key_profile[0];
	total_key_height = key_profile[1];
	width_difference = key_profile[2];
	height_difference = key_profile[3];
	total_depth = key_profile[4];
	top_tilt = key_profile[5];
	top_skew = key_profile[6];
	dish_type = key_profile[7];
	dish_depth = key_profile[8];
	dish_skew_x = key_profile[9];
	dish_skew_y = key_profile[10];
	key_x_length = key_profile[11];
	key_y_length = key_profile[12];


	//dependant variables
	key_width = total_key_width * key_x_length - width_difference;
	key_height = total_key_height * key_y_length - height_difference;

	if(dish_type == 0){ // cylindrical dish
		/* we do some funky math here
		 * basically you want to have the dish "dig in" to the keycap x millimeters
		 * in order to do that you have to solve a small (2d) system of equations
		 * where the chord of the spherical cross section of the dish is
		 * the width of the keycap.
		 */
		// the distance you have to move the dish up so it digs in dish_depth millimeters
		chord_length = (pow(key_width, 2) - 4 * pow(dish_depth, 2)) / (8 * dish_depth);
		//the radius of the dish
		rad = (pow(key_width, 2) + 4 * pow(dish_depth, 2)) / (8 * dish_depth);

		if (inverted_dish == 1){
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
			rotate([90-top_tilt,0,0])
			translate([0,-chord_length,0])
			cylinder(h=100,r=rad, $fn=1024, center=true);
		}
		else{
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
			rotate([90-top_tilt,0,0])
			translate([0,chord_length,0])
			cylinder(h=100,r=rad, $fn=1024, center=true);
		}
	}
	else if (dish_type == 1) { // spherical dish
		//same thing here, but we need the corners to just touch - so we have to find the hypotenuse of the top
		chord = pow((pow(key_width,2) + pow(key_height, 2)),0.5); //getting diagonal of the top

		// the distance you have to move the dish up so it digs in dish_depth millimeters
		chord_length = (pow(chord, 2) - 4 * pow(dish_depth, 2)) / (8 * dish_depth);
		//the radius of the dish
		rad = (pow(chord, 2) + 4 * pow(dish_depth, 2)) / (8 * dish_depth);

		if (inverted_dish == 1){
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
            rotate([-top_tilt,0,0])
			translate([0,0,-chord_length])
			sphere(r=rad, $fn=256);
		}
		else{
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
            rotate([-top_tilt,0,0])
			translate([0,0,chord_length])
			sphere(r=rad, $fn=256);
		}
	}
	else if (dish_type == 2){// SIDEWAYS cylindrical dish - used for spacebar

		chord_length = (pow(key_height, 2) - 4 * pow(dish_depth, 2)) / (8 * dish_depth);
		rad = (pow(key_height, 2) + 4 * pow(dish_depth, 2)) / (8 * dish_depth);

		if (inverted_dish == 1){
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
			rotate([90,top_tilt,90])
			translate([0,-chord_length,0])
			cylinder(h=key_width + 20,r=rad, $fn=1024, center=true); // +20 just cuz
		}
		else{
			translate([dish_skew_x, top_skew + dish_skew_y, total_depth])
			rotate([90,top_tilt,90])
			translate([0,chord_length,0])
			cylinder(h=key_width + 20,r=rad, $fn=1024, center=true);
		}
	}
}

//actual full key with space carved out and keystem/stabilizer connectors
module key( key_profile, slice = false, stem_rotation = 0 )
{
       difference()
       {
	union()
	{
		difference()
		{	
			shape(key_profile, 0);

			translate([0,0,-.1])
			shape(key_profile, 3);
		}
		
		connector(key_profile,has_brim,stem_rotation=stem_rotation);
		if (stabilizers == 1)
		{
			stabilizer_connectors(key_profile,has_brim,stem_rotation=stem_rotation);
		}
	}


        // Cross-section
        if ( slice )
	{
		translate([0,-10,0]) cube( 20, 20, 20);
	}
       }
}





///////////////////

// Thing # 468651 - comment by deltapenguin on April fools 2016.
// http://www.thingiverse.com/thing:468651/#comments
//
// This file contains the module to render letters on keys.
//
// geodynamics:
//	- Added automatic depth, exactly 1mm bellow the top. 
// 	- Angled the letter to follow the key profile angle.


module blank_key( key_row, stem_rotation = 0 )
{
    totalDepth = key_profiles[key_row][4];
    rotationAngle = -key_profiles[key_row][5];
    topDepthDiff = key_profiles[key_row][8];

    union()
    {
        key(key_profiles[key_row], stem_rotation = stem_rotation);
        if(bump)
        {
            translate([0, 0, totalDepth - topDepthDiff - 1])
            rotate([rotationAngle, 0, 0])
            translate([x-font_size/4, y-font_size/2-2, 0])
            #cube([font_size/2, 1, 2]);
        }
    }
}

include<strings.scad>; // http://www.thingiverse.com/thing:526023



// With letters
module generate_keycap( font_name,	// Name of font
                        font_size,	// Font size in mm
                        key_row,	// The key profile
                        letter,		// The unicode string (including \n as line separator)
                        x, y,		// X-Y positioning on top of the key
			bump = false,	// The little bump on "J" and "K" and KeyPad 5.
			slice = false,  // Cut the keycap in half to expose the inner structure.
			stem_rotation = 0, // rotation of the connector
			letter_rotation = 0 )  // Letter rotation angle.
{
    difference()
    {
        totalDepth = key_profiles[key_row][4];
        rotationAngle = -key_profiles[key_row][5];
        topDepthDiff = key_profiles[key_row][8];

        union()
        {
            key(key_profiles[key_row], stem_rotation = stem_rotation);
            if(bump)
            {
                translate([0, 0, totalDepth - topDepthDiff - 1])
                rotate([rotationAngle, 0, 0])
                translate([x-font_size/4, y-font_size/2-2, 0])
                #cube([font_size/2, 1, 2]);
            }
        }
	
        // Cross-section for debugging
	if ( slice )
	{
	    translate([0,-50,0]) cube( 100, 100, 100);
    }

	rows = split(letter, "\n");
	num_rows = len(rows);
	//font_size = font_size / num_rows;
	
	for (i = [0 : num_rows])
	{
		// Translate to half of the top thickness
 	        translate([0, 0, totalDepth - topDepthDiff])

		// Rotate the letter to the same as the key top
        	rotate([rotationAngle, 0, 0])
        	{
			// Translate to the correct row position
			translate([x, y-font_size*i, 0])

			// Rotate the letter around the center
			rotate([0, 0, letter_rotation])
		
			#linear_extrude(height = topDepthDiff * 2, center = true, convexity = 10, twist = 0)
        		text(rows[i], size=font_size, font=font_name, halign = "center", valign = "center" );
        	}
	}
    }
}

