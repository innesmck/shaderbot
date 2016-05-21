grammar = {
	"int"       : [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ],
	"int1"      : [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ],
	"int27"     : [ "2", "3", "4", "5", "6", "7" ],
	"int39"     : [ "3", "4", "5", "6", "7", "8", "9" ],
	"int14"     : [ "1", "2", "3", "4" ],
	"int24"     : [ "2", "3", "4" ],
	"int5"      : [ "5", "6", "7", "8", "9" ],
	"dec"       : [ "$int$$int$$int$$int$$int$" ],
	"op"        : [ "*", "+", "/" ],
	"rand1"     : [ "$int1$.$dec$" ],
	"rand00"    : [ "$int$$int$.$dec$", "$int$.$dec$", "0.$dec$" ],
	"rand0"     : [ "$int$.$dec$", "0.$int5$$dec$" ],
	"rand"      : [ "0.$dec$" ],
	"nrand"      : [ "$rand$", "-$rand$"  ],
	"scale"      : [ "$int14$.$dec$", " 0.$int1$dec$" ],
	"rand01"     : [ "0.1$dec$", "0.1$dec$", "0.2$dec$"],
	"rand05"     : [ "0.5$dec$", "0.6$dec$", "0.7$dec$"],
	"rand19"     : [ "$int1$.$dec$" ],
	"rand27"     : [ "$int27$.$dec$" ],
	"modcoords" : [ "( lCoords $op$ vec2( $rand$, $rand$ ) ) $op$ vec2( $rand$, $rand$ )" ], 
	"color"		: [ #"getRandomHue( $rand$, $rand$, $rand$ )", 
				 	"getRandomHue(       $rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomDarkHue(   $rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomBrightHue( $rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomBrightHue( $rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomHue(       $mix:rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomBrightHue( $mix:rand$, $mix:rand$, $mix:rand$ )", 
				 	"getRandomBrightHue( $mix:rand$, $mix:rand$, $mix:rand$ )", 
				 	#"getRandomHue( $mix:rand$, $mix:rand$, $mix:rand$ )", 
				 	#"getRandomHue( $mix:rand$, $mix:rand$, $mix:rand$ )", 
				 	"getGoldenRatio( $int$.0, $rand$, $rand$ )",
				 	"getGoldenRatio( $int$.0, $mix:rand$, $mix:rand$ )" 
				 	],

	"neg"        : { "param0" : "@x", "vals" : [ "@x", "(1.0 - @x)" ] },		 	

	"recolor" : { "param0" : "@x", "param1" : "@color",
					"vals"   : [ 
						"float z=clamp(@x,0.0,1.0); float b2=clamp((z-0.2)/0.25,0.0,1.0), b1=clamp(z/0.0001,0.0,1.0); @color = mix( $color$, mix($color$,$color$,b2), b1);",
						"float z=clamp(@x,0.0,1.0); float b2=clamp((z-0.2)/0.25,0.0,1.0), b1=clamp(z/0.0001,0.0,1.0); @color = $color$; @color = mix( @color*0.3, mix(@color*0.9,vec3(1.0),b2), b1);",
						"if( @x > $rand$ ) @color *= @x; else @color *= 1.0 - @x;",
						"if( @x > $mix:rand$ ) { @color = $mix:color$ * @x; } else { @color = $mix:color$ * (1.0 - @x); }",
						"if( @x > 0.3 ) { @color = $mix:color$ * @x; } else { @color = $mix:color$ * (@x * 3.33 ); }",
						"if( @x > 0.3 ) { @color = $mix:color$ * @x; } else { @color = $mix:color$ * (1.0 - @x * 3.33 ); }",
						"if( @x > 0.3 ) { @color = $mix:color$ * (@x - 0.3) * 1.43; } else { @color = $mix:color$ * (1.0 - @x * 3.33 ); }",
						"if( @x > 0.3 ) { @color = $mix:color$ * (@x - 0.3) * 1.43; } else { @color = $mix:color$ * (1.0 - @x * 3.33 ); }",
						"if( @x > 0.3 ) { @color = $mix:color$ * @x; } else { @color = $mix:color$ * (1.0 - @x); }",
						"if( @x > 0.5 ) { @color = $mix:color$ * @x; } else { @color = $mix:color$ * (1.0 - @x); }",
						"@color *= $neg:@x$;",
						"@color *= $neg:@x$;",
						"@color *= $neg:@x$; @color += $mix:color$;",
						"@color  = mix( $mix:color$, $mix:color$, $neg:@x$ );",
						"@color  = mix( $mix:color$, $mix:color$, $func2:@x$ );",
						"@color  = vec3( $neg:@x$ );",
						] },

	"rotate" : { "param0" : "@x", 
					"vals"   : [ 
						"", "",
						"@x = rotate( $nrand$ * l * 20.0, @x );"
						"@x = rotate( $nrand$ * l * t2 * 30.0, @x );"
						"@x = rotate( $nrand$ * t2 * 6.0, @x );"
						"@x = rotate( $nrand$ * $func2:t$ * 6.0, @x );"
					    "@x = rotate( t2 * 6.0, @x );"
						"@x = rotate( $nrand$ * $mixer$ * 6.0, @x );"
						"@x = rotate( $mix:nrand$ * $func2:t$ * 6.0, @x );"
						] },

	"vec2func" : { "param0" : "@x", 
					"vals"   : [ 
						"", "", "", "", "", "", "", "",
						"$func:@x.x$; $func:@x.y$;", 
						"@x = $func2:@x$; $func:@x.x$; $func:@x.y$;", 
						"@x = $func2:@x$", 
						"@x = $func2:@x$ * $func2:@x$", 
						"@x = $func2:@x$;   @x = $func2:@x$", 
						"@x = vec2( $rand$ ) - @x;  @x = $func2:@x$", 
						"@x = vec2( $rand0$ ) / @x; @x = $func2:@x$" 
						] },

	"func2"     : { "param0" : "@x", 
					"vals"   : [ 
						"@x*@x", 
						"@x*@x*@x", 
						"abs(@x)", 
						"ss($rand$,$rand$,@x)", 
	                	"sin( @x * $rand$ * $rand27$ )", 
	                	"( @x * $mix:rand0$ )", 
	                	"clamp( @x, -0.$dec$, 0.$int5$$dec$ )", 
	                	"worm(0.$int14$$dec$, 0.$int5$$dec$, @x )", 
	                	"vnoise( @x * 0.0$dec$ )", 
	                	"pixelate(@x,$int1$$int$.0)" ,
	                	"mix( $func2:@x$, $func2:@x$, tc.x )",
	                	] },
	
	"func"      : { "param0" : "@x", 
					"vals"   : [ 
						"", "",
						"@x = mix( $func2:@x$, $func2:@x$, $mixer$ )", 
						"@x = mix( $func2:@x$, $func2:@x$, $mixer$ )", 
						"@x = mix( $func2:@x$, $func2:@x$, $mixer$ )", 
						"@x = $func2:@x$", 
						"@x = $func2:@x$", 
						"@x = $func2:@x$ * $func2:@x$", 
						"@x = $func2:@x$;   @x = $func2:@x$", 
						"@x = $rand$ - @x;  @x = $func2:@x$", 
						"@x = $rand0$ / @x; @x = $func2:@x$" 
						] },

	"posfunc"   : { "param0" : "@x", 
					"vals"   : [ 
						"", "", "", "", "", "", "", "","", "",
						"$func:@x$;", 
						"$func:@x$;", 
						"$func:@x$;", 
						"if( i % $int24$ == 0 ) { $func:@x$; } else { $func:@x$; }" 
					] },

	"finalise"   : { "param0" : "@x", 
					 "vals"   : [ 
						"", "", "", "", "", "",
						"$finalise:@x$;$finalise:@x$;",
						"$finalise:@x$;$finalise:@x$;",
						"$finalise:@x$;$finalise:@x$;$finalise:@x$;",
						"@x = 1.0 - @x;", 
						"@x = 1.0 - @x;", 
						"@x = 1.0 - @x;", 
						"@x = (1.0 - @x) * (1.0 - @x);",
						"@x = $func2:@x$;"
						"@x = $func2:@x$;"
						"@x = $func2:@x$;"
						"@x = $func2:@x$;"
						] },

	"mixerv"	: [ "1.0", "0.0",# "0.0", "1.0", 
					"($func2:tc$).y", "($func2:tc$).x",# "length( $func2:tc2$ )", "length( $func2:tc2$ )",
					"tc2.x * tc2.y", "min( abs( tc2.x ), abs( tc2.y ) )", "max( abs( tc2.x ), abs( tc2.y ) )",
					"tc.x * tc.y", "min( tc.x, tc.y )", "max( tc.x, tc.y )",
					"t", "t", "t2", "t2", "$func2:t$", "$func2:t$",
					"tc.x", "1.0 - tc.x", "tc.y", "1.0 - tc.y", "$func2:tc.x$", "$func2:tc.y$",
					"tc2.x", "1.0 - tc2.x", "tc2.y", "1.0 - tc2.y",
					"$rand$", "$rand$", #"$rand$", "$rand$", "$rand$", 
					"l * l", "l2 * l2", "$func2:l$", "$func2:l$", "$func2:l2$"
					 ],

	"mixer"		: [ "clamp( $mixerv$, 0.0, 1.0 )", 
					"clamp($mixerv$ * t, 0.0, 1.0)", 
					"clamp($mixerv$ * t2, 0.0, 1.0)" ],

	"mix"		: { "param0" : "@r", 
					"vals"   : [
						"mix( $@r$, $@r$, $mixer$ )",
						"mix( $@r$, $@r$, $mixer$ )",
						"mix( $@r$, $@r$, $mixer$ )",
						"mix( mix( $@r$, $@r$, $mixer$ ), $@r$, $mixer$ )",
						"mix( mix( $@r$, $@r$, $mixer$ ), mix( $@r$, $@r$, $mixer$ ), $mixer$ )"  ] },

	"amp"       : [ "$rand$", "0.5", "0.4$dec$", "0.5$dec$", "0.6$dec$" ],
	"lac"       : [ "2.0", "1.$dec$", "2.$dec$", "0.$int5$$dec$" ],
	"col"       : [ "$rand$", "1.$int14$$dec$" ],
	"coordfunc" : [ "", "", "" ],
	"vec3"      : [ "vec3( $rand00$ )", "vec3( vec2( $rand00$ ), $rand00$ )", "vec3( $rand00$, $rand00$, $rand00$ )" ],
	"scalevec2" : [ "vec2( $rand1$ )", "vec2( $rand1$, $rand1$ )", "vec2( 1.0 )", "vec2( $rand0$ )", "vec2( $rand0$, $rand0$ )" ],

	"posstep" : { "param0" : "@p", 
			  "vals"   : [  
			  		"@p.xy *= $lac$;",
			  		"@p.xy *= $lac$;",
			  		"@p    *= $lac$;",
			  		"@p.xy *= $mix:lac$;",
			  		"@p    *= $mix:lac$;",
			  		"@p.x  *= $mix:lac$; @p.y *= $mix:lac$;"
  				] },

	"fbm" : { "param0" : "@p", "param1" : "@c",
			  "vals"   : [  '''
			  	{
					float s = 0.0, m = 0.0, a = 1.0;
					for( int i=0; i < $int39$; i++ ){
				    	float x = snoise( @p );
				    	$posfunc:x$
						s += a * x;
					    m += a;
					    a  = a * $mix:amp$;
					    $posstep:@p$
					}
					@c = s/m;
				}
			'''] },

	"warppos" : { "param0" : "@p", "param1" : "@x", "param2" : "@y",
			  "vals"   : [  
			  		"@p = vec3( @x * $int39$.$dec$, @y * 4.0, $mixer$ );",
			  		"@p = vec3( @x * $int39$.$dec$, @y * 4.0, $mixer$ );",
			  		"@p = vec3( ( @x * @y ) * $int39$.$dec$, @y * 4.0, $mixer$ );",
			  		"@p = vec3( @x * $int39$.$dec$, @y * 4.0, (@x + @y) * $int39$.$dec$ );",
			  		"@p = vec3( @x * @x * $int39$.$dec$, @y * @y * 4.0, $mixer$ );",
  				] },

	"warp" : { "param0" : "@p", "param1" : "@q", "param2" : "@x",
			  "vals"   : [  '''
			  	{
			  		float y = 0.0;
				    @p = @q + vec3( 100.0 * $int1$ );
				    $fbm:@q:@x$
				    $fbm:@p:y$
			    	$warppos:@p:@x:y$
		    	    $fbm:@p:@x$;
				}
			'''] },

	"warp2" : { "param0" : "@p", "param1" : "@q", "param2" : "@x",
		  "vals"   : [  '''
		  	{
		  		float r = 0.0, s = 0.0;
		  		$warp:@p:@q:r$
		  		$warp:@p:@q:s$
		  		$warppos:@p:r:s$
    			$fbm:@p:@x$
			}
		'''] },

	"noise" : { "param0" : "@p", "param1" : "@q", "param2" : "@x",
			  "vals"   : [ 
			  	"$warp:@p:@q:@x$",
			  	"$warp:@p:@q:@x$",
			  	"$warp:@p:@q:@x$",
			  	"$warp2:@p:@q:@x$",
			  	"$fbm:@p:@x$",
			  	"$fbm:@p:@x$",
			  	"$fbm:@p:@x$",
			  	"$fbm:@p:@x$",
			  	"$fbm:@p:@x$",
			  	"$fbm:@p:@x$",
			  ] },

	"shape" : { "param0" : "@pos", "param1" : "@x",
		  "vals"   : [
		  		"", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
		  		"@x = @pos.x * $rand27$ + sin( @pos.x * $rand27$ ) + @pos.y * $rand27$ + sin( @pos.y * $rand27$ ) + @x; @x = abs( sin( @x * 3.145 ));",
		  		"@x = @pos.x * $rand27$ + @pos.y * $rand27$ + @x; @x = abs( sin( @x * 3.145 ));",
		  		"@x = max( @pos.x * $rand27$, @pos.y * $rand27$ ) + @x; @x = abs( sin( @x * 3.145 ));",
		  		"@x = ($neg:@pos.x$) * $rand27$ + ($neg:@pos.y$) * $rand27$ + @x; @x = sin( @x * 3.145 ) * 0.5 + 0.5;",
		  		"@x = l * $rand27$ + @x; @x = abs( sin( @x * 3.145 ));",
		  		"@x = l * $rand27$ + @x; @x = ( sin( @x * 3.145 )) * 0.5 + 0.5;",
		  		'''float v = @x; 
		  		   float w = $rand19$; 
		  		   pos2.xy = vec2( w ) - @pos.xy * w;
		  		   $noise:pos2:inpos:v$
		  		   @pos.x = @pos.x * $rand27$ + 0.3 * @x;
		  		   @pos.y = @pos.y * $rand27$ + 0.3 * v;
		  		   @x = abs( sin( -@pos.y * 3.145 ) + sin( @pos.x  * 3.145 )) ;
		  		'''
		  	] },

	"donoise" : { "param0" : "@color",
		  "vals"   : [  '''
		  	{
		  	    float x = 0.0;
		        @color  = $mix:color$;
		        vec3 pos2 = pos;
		        pos2.xy *= $rand19$;    
		        $noise:pos2:inpos:x$
		        $shape:pos:x$
		        $recolor:x:@color$
			}
		'''] },

	"domain" : { "param0" : "@color",
		  "vals"   : [  
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; float f = length( @color ) * length( color2 ); $recolor:f:@color$",
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; float f = length( @color * color2 ); $recolor:f:@color$",
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; @color = @color + color2;",
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; if( length( @color ) > 0.5 ) @color = @color + color2;",
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; color = color * color2;",
		  	"vec3 color2 = color; $donoise:color$ $donoise:color2$; color = color * 0.75 + color2 * 0.75;",
		  	"$donoise:color$",
		  	"$donoise:color$",
		  	"$donoise:color$",
		  	"$donoise:color$",
		  	"float test = $mixer$; if( $func2:test$ > $rand$ ){$donoise:color$}else{$donoise:color$}",
		  	"float test = $mixer$; vec3 col1; $donoise:color$ $donoise:col1$ color = mix( col1, color, test );",
		  	"float test = $mixer$; vec3 col1; $donoise:color$ $donoise:col1$ color = mix( col1, color, test );"
		  	 ] },
}
