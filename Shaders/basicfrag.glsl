float gold = 0.618033988749895;
vec3 getGoldenRatio( float i, float s, float v )
{
    float h = gold * i;
    h       = mod( $rand$ + h, 1.0 );
    return hsv2rgb( vec3( h, s * 0.3 + 0.7, v * 0.2 + 0.8 ) ) ;
}

//
// Generated code
//

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2  tc = fragCoord / iResolution.xy;
    tc.x = $neg:tc.x$;
    tc.y = $neg:tc.y$;

    vec2  tc2 = (tc - vec2( 0.5));
    float l, l2 = length( tc2 );

    float t  = iGlobalTime * 0.1;
    t = $neg:t$;

    float t2 = t;
    $func:t2$;
    float t3 = t;
    $func:t3$;

    tc2 *= vec2( $mix:rand$, $mix:rand$ ) + vec2( 0.5 );
    tc2 = ( tc2 + $nrand$ * vec2( $mix:rand$, $mix:rand$ ) );// * 2.0;
    l = length( tc2 );
    $rotate:tc2$
    $vec2func:tc2$;
    l2 = length( tc2 );

    vec3 inpos = vec3( tc2, t3 );//vec3( tc2 + vec2( $mix:rand$, $mix:rand$ ) ), t  );
    vec3 color, pos = inpos;
    $domain:color$
    $finalise:color$
    fragColor = vec4( color, 1.0 );
}

#ifndef D_SHADERTOY
    void main (void )
    {
        vec4 fragColor;
        mainImage( fragColor, gl_FragCoord.xy );
        gl_FragColor = fragColor;
    }
#endif