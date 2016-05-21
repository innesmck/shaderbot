//
// Utility functions
//

float snoise( float v ) { return snoise( vec3( v ) ); }

float vnoise( float v ) { return snoise( vec3( v, v + 100.0, v + 10000.0 ) ); }
vec2  vnoise( vec2 v )  { return vec2( vnoise( v.x ), vnoise( v.y ) ); }
vec3  vnoise( vec3 v )  { return vec3( vnoise( v.x ), vnoise( v.y ), vnoise( v.z ) ); }

float worm( float low, float high, float x ) { if( x < min(low,high) || x > max(low,high) ) return 0.0; return x; }
vec2  worm( float low, float high, vec2 x )  { if( ( x.x + x.y ) / 2.0 < min(low,high) || ( x.x + x.y ) / 2.0  > max(low,high) ) return vec2( 0.0 ); return vec2( x ); }
vec3  worm( float low, float high, vec3 x )  { if( ( x.x + x.y + x.z ) / 3.0 < min(low,high) || ( x.x + x.y + x.z ) / 3.0  > max(low,high) ) return vec3( 0.0 ); return vec3( x ); }

float ss( float low, float high, float x ) { return smoothstep( min(low,high), max(low,high), x ); }
vec2  ss( float low, float high, vec2 x )  { return smoothstep( min(low,high), max(low,high), x ); }
vec3  ss( float low, float high, vec3 x )  { return smoothstep( min(low,high), max(low,high), x ); }

float pixelate( float x, float y ) { return ceil( x * y ) / y; }
vec3  pixelate( vec3 x, float y )  { return ceil( x * y ) / y; }
vec2  pixelate( vec2 x, float y )  { return ceil( x * y ) / y; }

vec2 rotate( float a, vec2 x ) { mat2 m = mat2( cos( a ), -sin( a ), sin( a ), cos( a ) ); return m * x; }

vec3 neg( vec3 x ) { return vec3( 1.0 ) - x; }
vec3 inv( vec3 x ) { return vec3( 1.0 ) / x; }

vec3 rgb2hsv( vec3 c )
{
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb( vec3 c )
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec3 getRandomHue( float h, float s, float v )
{
    return hsv2rgb( vec3( fract( h ), s, v * 0.1 + 0.9 ) ) ;
}

vec3 getRandomBrightHue( float h, float s, float v )
{
    return hsv2rgb( vec3( fract( h ), s * 0.3 + 0.7, v * 0.6 + 0.4 ) ) ;
}

vec3 getRandomDarkHue( float h, float s, float v )
{
    return hsv2rgb( vec3( fract( h ), s * 0.5, v * 0.2 ) ) ;
}